import os
import openai

from llama_index.query_engine.retriever_query_engine import RetrieverQueryEngine
from llama_index.callbacks.base import CallbackManager
from llama_index import (
    LLMPredictor,
    ServiceContext,
    StorageContext,
    load_index_from_storage,
)
from langchain.chat_models import ChatOpenAI
import chainlit as cl

from llama_index import VectorStoreIndex, SimpleDirectoryReader, ServiceContext
from llama_index.llms import OpenAI


try:
    # rebuild storage context
    storage_context = StorageContext.from_defaults(persist_dir="./storage_forms")
    # load index
    index = load_index_from_storage(storage_context)
except:
    from llama_index import VectorStoreIndex, SimpleDirectoryReader, ServiceContext
    service_context = ServiceContext.from_defaults(
        llm=OpenAI(model="gpt-3.5-turbo-0613")
    )    
    reader = SimpleDirectoryReader(input_dir="./final_artifacts/pdf_forms/")
    data = reader.load_data()
    index = VectorStoreIndex.from_documents(data, service_context=service_context)
    index.storage_context.persist(persist_dir="./storage_forms")

@cl.on_chat_start
async def factory():
    chat_engine = index.as_chat_engine(chat_mode="openai", verbose=True)    
    cl.user_session.set("chat_engine", chat_engine)

@cl.on_message
async def main(message: cl.Message):
    chat_engine = cl.user_session.get("chat_engine")  # type: RetrieverQueryEngine
    def q(content):
        return f'Use the tool to answer: {content}'
    response = await cl.make_async(chat_engine.chat)(q(message.content))
    response_message = cl.Message(content="")
    source_format = [s.metadata['file_name'] for s in response.source_nodes]
    response_message.content = response.response + '\n\n\n' + 'Sources are from \n'.join(source_format)
    await response_message.send()
