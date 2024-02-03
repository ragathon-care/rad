import logging
import json

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
    
    def _search_dql(self, query):
        request: Dict[str, Any] = {}
        request["type"] = "query"
        request["query"] = query
        request["size"] = self._api_max_items
        request["cluster"] = "best"

        api_url = "https://api.vectara.io/v1/index"

        response = self._session.post(
            headers=self._get_post_headers(),
            url=api_url,
            params=self._get_api_key(),
            data=json.dumps(request),
            timeout=self._api_timeout,
            verify=True
        )

        status_code = response.status_code

        result = response.json()

        status_str = result["status"]["code"] if "status" in result else None
        if status_code == 422:
            return "UNPROCESSABLE_CONTENT"
        elif status_code == 400:
            return "BAD_REQUEST"
        elif status_code == 500:
            return "INTERNAL_ERROR"
        else:
            return "OK"
        
    def as_retriever(self, **kwargs: Any) -> BaseRetriever:
        """Return a Retriever for this managed index."""
        from llama_index.indices.managed.vectara.retriever import VectaraRetriever

        return VectaraRetriever(self, **kwargs)

    def as_query_engine(self, **kwargs: Any) -> BaseQueryEngine:
        if kwargs.get("summary_enabled", True):
            from llama_index.indices.managed.vectara.query import VectaraQueryEngine
            
            client = OpenAI(api_key=self._diffbot_api_key, base_url="https://llm.diffbot.com/rag/v1/")
            response = client.chat.completions.create(
                model="diffbot-medium",
                messages=[
                    {
                        "role": "user",
                        "content": "Who is the CEO of Twitter?"
                    }
                ],
                stream=False,
            )

            kwargs["summary_enabled"] = True
            retriever = self.as_retriever(**kwargs)
            return VectaraQueryEngine.from_args(retriever, **kwargs)  # type: ignore
        else:
            from llama_index.query_engine.retriever_query_engine import (
                RetrieverQueryEngine,
            )

            kwargs["retriever"] = self.as_retriever(**kwargs)
            return RetrieverQueryEngine.from_args(**kwargs)

    def custom_query(self, query_str: str) -> STR_OR_RESPONSE_TYPE:
        nodes = self.retriever.retrieve(query_str)
        response_obj = self.response_synthesizer.synthesize(query_str, nodes)
        return response_obj