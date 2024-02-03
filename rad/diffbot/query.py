from typing import Any, Dict, List, Optional, Sequence, Type

from llama_index.schema import QueryBundle
from llama_index.callbacks.schema import CBEventType, EventPayload
from llama_index.callbacks.base import CallbackManager
from llama_index.postprocessor.types import BaseNodePostprocessor
from llama_index.core.response.schema import RESPONSE_TYPE, Response
from llama_index.query_engine import BaseQueryEngine
from llama_index.service_context import ServiceContext

from rad.diffbot.retriever import DiffbotRetriever

class DiffbotQueryEngine(BaseQueryEngine):
    def __init__(
        self,
        retriever: DiffbotRetriever,
        service_context: Optional[ServiceContext] = None,
        summary_enabled: bool = False,
        node_postprocessors: Optional[List[BaseNodePostprocessor]] = None,
        callback_manager: Optional[CallbackManager] = None,
    ) -> None:
        self._retriever = retriever
        self._summary_enabled = summary_enabled
        self._node_postprocessors = node_postprocessors or []
        self._service_context = service_context or ServiceContext.from_defaults()

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
            summary_enabled=summary_enabled,
            **kwargs
        )
    
    def _diffbot_chat(self, query_bundle: QueryBundle) -> RESPONSE_TYPE:

        client = OpenAI(api_key=self._diffbot_api_key, base_url="https://llm.diffbot.com/rag/v1/")
        response = client.chat.completions.create(
            model="diffbot-medium",
            messages=[
                {
                    "role": "user",
                    "content": query_bundle.query_str
                }
            ],
            stream=False,
        )

        return response["data"]

    def _query(self, query_bundle: QueryBundle) -> RESPONSE_TYPE:
        with self.callback_manager.event(
            CBEventType.QUERY, payload={EventPayload.QUERY_STR: query_bundle.query_str}
        ) as query_event:
            if self._retriever is None:
                nodes, response = self._diffbot_chat(query_bundle)
            else:
                nodes, response = self._retriever._query_enhanced_search(query_bundle)
            query_event.on_end(payload={EventPayload.RESPONSE: response})
        return Response(response=response, source_nodes=nodes)