# st-milvus-connection
Connect your streamlit app to milvus database.

Install the library with:
```
pip install st_milvus_connection
```

Run the example script:
```
import os
import streamlit as st

from st_milvus_connection import MilvusConnection

os.environ["milvus_uri"] = YOUR_MILVUS_ENDPOINT
os.environ["milvus_token"] = YOUR_MILVUS_TOKEN

conn = st.connection("milvus", type=MilvusConnection)

collections_list = conn.list_collections()

for i, collection in enumerate(collections_list):
    print(f"{i} {collection} contains {conn.count_entities(collection)} entities")
```
