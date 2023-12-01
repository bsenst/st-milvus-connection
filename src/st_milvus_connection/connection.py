import os
import streamlit as st
from streamlit.connections import BaseConnection
from streamlit.runtime.caching import cache_data

from pymilvus import (
    connections,
    utility,
    Collection
)

class MilvusConnection(BaseConnection[connections]):
    def _connect(self, **kwargs) -> connections:

        # The following code passage has been adapted from
        # https://github.com/gerardrbentley/st-openai-embeddings-connection/blob/e440ff92ec8187a6bc17025c6f6c50c3e37ed108/src/st_openai_embeddings_connection/connection.py
        if "milvus_uri" in kwargs:
            milvus_uri = kwargs.pop("milvus_uri")
        elif "milvus_uri" in self._secrets:
            milvus_uri = self._secrets["milvus_uri"]
        else:
            milvus_uri = os.environ.get("milvus_uri")
            if milvus_uri is None:
                raise Exception("milvus_uri not in kwargs, secrets or environment")

        if "milvus_token" in kwargs:
            milvus_token = kwargs.pop("milvus_token")
        elif "milvus_token" in self._secrets:
            milvus_token = self._secrets["milvus_token"]
        else:
            milvus_token = os.environ.get("milvus_token")
            if milvus_token is None:
                raise Exception("milvus_token not in kwargs, secrets or environment")
        
        return connections.connect("default", uri=milvus_uri, token=milvus_token)
    
    def has_collection(self, collection_name) -> bool:
        return utility.has_collection(collection_name)
    
    def list_collections(self) -> list:
        return utility.list_collections()
    
    def get_collection(self, collection_name) -> Collection:
        return Collection(collection_name)
