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
    print(f"{i} {collection}")
```

# Example Application
This Streamlit Connection was created as part of the Streamlit Connections Hackathon in August 2023.

[github.com/bsenst/Connections-Hackathon](https://github.com/bsenst/Connections-Hackathon)

![image](https://github.com/bsenst/st-milvus-connection/assets/8211411/ab4d996d-d514-4655-9e1b-93379133942d)
