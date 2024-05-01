## Integrate our code OpenAI API
import os
from constants import openai_keys
from langchain.llms import openai

import streamlit as st

os.environ["OPENAI_API_KEY"]=openai_keys

# streamlit framework

st.title('Langchain Demo with OPENAI API')
input_text=st.text_input("Search the topic you want")

## OPENAI LLMS
llm=openai(temperature=0.8)


if input_text: 
    st.write(llm(input_text))