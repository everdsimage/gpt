import streamlit as st
from llama_index import GPTSimpleVectorIndex
from langchain import OpenAI
import sys
import os

# API key
os.environ["OPENAI_API_KEY"] = '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'

# Trained data
everindex = GPTSimpleVectorIndex.load_from_disk('medical.json')


st.header("""Q&A""")

st.text("""Medical Information""")

st.text("")

def user_input_features():
    input = st.text_area('')
    if input != '':
        response = everindex.query(input)
        return response

def main():
    answer = user_input_features()
    st.write(answer)

if __name__ == "__main__":
    main()