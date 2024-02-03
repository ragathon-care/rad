import logging
import os

from typing import Any, Dict, List, Optional, Sequence

import requests

from llama_index.indices import BaseManagedIndex
from llama_index.query_engine import BaseQueryEngine
from llama_index.retrievers import BaseRetriever
from llama_index.data_structs.data_structs import IndexDict
from llama_index.response_synthesizers import (
    get_response_synthesizer,
    BaseSynthesizer
)
from llama_index.service_context import ServiceContext
from llama_index.storage.storage_context import StorageContext

from llama_index.schema import BaseNode, Document
from openai import OpenAI

_logger = logging.getLogger(__name__)


class DiffBotQueryEngine(BaseManagedIndex):
    def __init__(
        self,
        diffbot_api_key: Optional[str] = None,
        nodes: Optional[Sequence[BaseNode]] = None,
        index_struct: Optional[IndexDict] = None,
        service_context: Optional[ServiceContext] = None,
        storage_context: Optional[StorageContext] = None,
        show_progress: bool = False,
        **kwargs: Any
    ):
        super().__init__(
            nodes=nodes,
            index_struct=index_struct,
            service_context=service_context,
            storage_context=storage_context,
            show_progress=show_progress,
            **kwargs,
        )
        self._diffbot_api_key = diffbot_api_key or os.environ.get("DIFFBOT_API_KEY")
        if (
            self._diffbot_api_key is None
        ):
            _logger.warning("Can't find Diffbot credentials in environment.")
            raise ValueError("Missing Diffbot credentials")
        
        self._session = requests.Session()  # to reuse connections
        adapter = requests.adapters.HTTPAdapter(max_retries=3)
        self._session.mount("https://", adapter)
        self._api_timeout = 90
        self._api_max_items = 5

    def _get_post_headers(self) -> dict:
        return {
            "Content-Type": "application/json",
            "accept": "application/json"
        }

    def _get_api_key(self) -> dict:
        return {"token": self._diffbot_api_key}
        
    def as_retriever(self, **kwargs: Any) -> BaseRetriever:
        """Return a Retriever for this managed index."""
        from rad.diffbot.retriever import DiffbotRetriever

        return DiffbotRetriever(self, **kwargs)

    def as_query_engine(self, **kwargs: Any) -> BaseQueryEngine:
        if kwargs.get("summary_enabled", True):
            from rad.diffbot.query import DiffbotQueryEngine
            
            kwargs["summary_enabled"] = True
            # ignores retriever and uses diffbot's openai interface
            return DiffbotQueryEngine.from_args(diffbot_api_key=self._diffbot_api_key, **kwargs)  
        
        else:
            from llama_index.query_engine.retriever_query_engine import (
                RetrieverQueryEngine,
            )

            kwargs["retriever"] = self.as_retriever(**kwargs)
            return RetrieverQueryEngine.from_args(**kwargs)
