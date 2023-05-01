import os 
from apikey import apikey

import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.memory import ConversationBufferMemory


os.environ["OPENAI_API_KEY"] = apikey




#App framework
st.title("Security GPT🦜️🔗")
prompt = st.text_input("Enter a prompt: Start by listing the technology you are using.")



#Prompt templates
title_template = PromptTemplate(
    input_variables= ["technology"],
    template = "I am using {technology} will these work well together from a security aspect."
)

sec_template = PromptTemplate(
    input_variables=['high_lvl'],
    template="Give me a detailed list of 5 high level suggestions to secure the for each of the technologies mentioned {high_lvl}"
)



#Memory
memory = ConversationBufferMemory(input_key="technology", memory_key='chat_memory')


#LLM
llm = OpenAI(temperature=0.9)
title_chain= LLMChain(llm=llm, prompt=title_template, verbose=True, output_key="tech", memory=memory)
sec_chain= LLMChain(llm=llm, prompt=sec_template, verbose=True, output_key="high_lvl_")

sequential_chain = SequentialChain(chains=[title_chain, sec_chain], input_variables=['technology',"high_lvl"],output_variables=['tech','high_lvl_'] ,verbose=True)







#Show stuff to screen if there is a prompt
if prompt:
    response = sequential_chain({"technology":prompt, "high_lvl":prompt})
    st.write(response['tech'])
    st.write(response["high_lvl_"])
    
    
    with st.expander('Message History'):
        st.info(memory.buffer)






