from typing import Any, Dict, List, Optional, Sequence, Type

from llama_index.schema import QueryBundle
from llama_index.callbacks.schema import CBEventType, EventPayload
from llama_index.callbacks.base import CallbackManager
from llama_index.postprocessor.types import BaseNodePostprocessor
from llama_index.core.response.schema import RESPONSE_TYPE, Response
from llama_index.query_engine import BaseQueryEngine

from rad.diffbot.retriever import DiffbotRetriever

class DiffbotQueryEngine(BaseQueryEngine):
    def __init__(
        self,
        retriever: DiffbotRetriever,
        summary_enabled: bool = False,
        node_postprocessors: Optional[List[BaseNodePostprocessor]] = None,
        callback_manager: Optional[CallbackManager] = None,
    ) -> None:
        self._retriever = retriever
        self._summary_enabled = summary_enabled
        self._node_postprocessors = node_postprocessors or []
        super().__init__(callback_manager=callback_manager)

    @classmethod
    def from_args(
        cls,
        retriever: DiffbotRetriever,
        summary_enabled: bool = False,
        **kwargs: Any,
    ) -> "DiffbotQueryEngine":
       
        return cls(
            retriever=retriever,
            summary_enabled=summary_enabled
        )

    def _query(self, query_bundle: QueryBundle) -> RESPONSE_TYPE:
        with self.callback_manager.event(
            CBEventType.QUERY, payload={EventPayload.QUERY_STR: query_bundle.query_str}
        ) as query_event:
            kwargs = (
                {
                    "summary_response_lang": self._summary_response_lang,
                    "summary_num_results": self._summary_num_results,
                    "summary_prompt_name": self._summary_prompt_name,
                }
                if self._summary_enabled
                else {}
            )
            nodes, response = self._retriever._query_enhanced_search(query_bundle, **kwargs)
            query_event.on_end(payload={EventPayload.RESPONSE: response})
        return Response(response=response, source_nodes=nodes)