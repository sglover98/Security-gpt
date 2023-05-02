import streamlit as st 
from langchain.prompts import PromptTemplate

def title():
    st.title('🦜🔗 Security GPT')

def input_bar():
    input_bar = st.text_input('Plug in your prompt here and lets get secure')    
    return input_bar     

def selector():
    st.s