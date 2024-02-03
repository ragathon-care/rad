from typing import Any, Dict, List, Optional, Sequence

from llama_index.core.base_retriever import BaseRetriever
from rad.diffbot.index import DiffbotIndex

class DiffbotRetriever(BaseRetriever):
  def __init__(
      self,
      index: DiffbotIndex,
      **kwargs: Any
  ):
    pass

  def _query_enhanced_search()