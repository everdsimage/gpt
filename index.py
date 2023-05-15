import streamlit as st
from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader
from llama_index import StorageContext, load_index_from_storage
#from gpt_index import GPTSimpleVectorIndex
from langchain import OpenAI
import sys
import os

# API key
os.environ["OPENAI_API_KEY"] = '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'

# Trained data
storage_context = StorageContext.from_defaults(persist_dir='Store')
index = load_index_from_storage(storage_context)

st.header("""Q&A""")

st.text("""Medical Information""")

st.text("")
        
def user_input_features():
    input = st.text_area('')
    if len(input) > 3:
        query_engine = index.as_query_engine()
        response = query_engine.query(input)
        return response

def main():
    answer = user_input_features()
    st.write(answer)

if __name__ == "__main__":
    main()