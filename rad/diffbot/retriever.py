import json
import logging
from typing import Any, Dict, List, Optional, Tuple

from llama_index.core.base_retriever import BaseRetriever
from llama_index.schema import NodeWithScore, QueryBundle
from llama_index.service_context import ServiceContext
from llama_index.callbacks.base import CallbackManager

from rad.diffbot.index import DiffbotIndex
_logger = logging.getLogger(__name__)

class DiffbotRetriever(BaseRetriever):
    def __init__(
        self,
        index: DiffbotIndex,
        service_context: Optional[ServiceContext] = None,
        callback_manager: Optional[CallbackManager] = None,
        object_map: Optional[dict] = None,
        verbose: bool = False,
        **kwargs: Any
    ):
        self._service_context = service_context or index.service_context
        self._index = index
        super().__init__(
            callback_manager=callback_manager, object_map=object_map, verbose=verbose
        )

    def _search_dql(self, query):
        request: Dict[str, Any] = {}
        request["type"] = "query"
        request["query"] = query
        request["size"] = self._api_max_items
        request["cluster"] = "best"

        api_url = "https://api.vectara.io/v1/index"

        response = self._index._session.post(
            headers=self._get_post_headers(),
            url=api_url,
            params=self._get_api_key(),
            data=json.dumps(request),
            timeout=self._api_timeout,
            verify=True
        )

        status_code = response.status_code

        result = response.json()
        return result
            
    def _enhance(self, query):
        pass

    def _query_enhanced_search(
        self, 
        query_bundle: QueryBundle,
        **kwargs: Any,
    ) -> Tuple[List[NodeWithScore], str]:
        response = self._search_dql(query_bundle.query_str)

        if response.status_code != 200:
            _logger.error(
                "Query failed %s",
                f"(code {response.status_code}, reason {response.reason}, details "
                f"{response.text})",
            )
            return [], ""

    def _retrieve(
        self,
        query_bundle: QueryBundle,
        **kwargs: Any,
    ) -> List[NodeWithScore]:
        return self._query_enhanced_search(query_bundle, **kwargs)[0]  # return top_nodes only