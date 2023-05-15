import streamlit as st
from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader
#from gpt_index import GPTSimpleVectorIndex
from langchain import OpenAI
import sys
import os

# API key
os.environ["OPENAI_API_KEY"] = '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'

# Trained data
#everindex = GPTSimpleVectorIndex.load_from_disk('medical.json')
documents = SimpleDirectoryReader('medical.json').load_data()
everindex = GPTVectorStoreIndex.from_documents(documents)

st.header("""Q&A""")

st.text("""Medical Information""")

st.text("")
        
def user_input_features():
    input = st.text_area('')
    if len(input) > 3:
        query_engine = everindex.as_query_engine()
        response = query_engine.query('tomato flu')
        print(str(response))
        st.write(response)
        return response

def main():
    answer = user_input_features()
    st.write(answer)

if __name__ == "__main__":
    main()