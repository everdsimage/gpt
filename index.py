import streamlit as st
from gpt_index import SimpleDirectoryReader, GPTListIndex, GPTSimpleVectorIndex, LLMPredictor, PromptHelper, ServiceContext
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