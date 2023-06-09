# Bring in deps
import os 
from app import framework
import pinecone
from apikey import apikey
import streamlit as st 
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain 
from langchain.vectorstores import pinecone
from langchain.memory import ConversationBufferMemory
from langchain.utilities import WikipediaAPIWrapper 
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings

#module imports
import sys
sys.path.insert(0,'security-gpt/app/framework.py')



#import apikey
os.environ['OPENAI_API_KEY'] = apikey

# App framework
framework.title()
prompt=framework.input_bar()


# Prompt templates
discovery_template = PromptTemplate(
    input_variables = ['technology'], 
    template="I am using {technology} will these work well together from a security aspect would you swap out any of the other technologies to have more optimal security solution."
)

overview_template = PromptTemplate(
    input_variables = ['overview', 'wikipedia_research'], 
    template='Provide me 5 best practices for each technology referenced and a list of the most necessary security practices for each technology Overview: {overview} while leveraging this wikipedia research:{wikipedia_research} '
)

# Memory 
discovery_memory = ConversationBufferMemory(input_key='technology', memory_key='chat_history')
overview_memory = ConversationBufferMemory(input_key='overview', memory_key='chat_history')


# Llms
llm = OpenAI(temperature=0.9) 
discovery_chain = LLMChain(llm=llm, prompt=discovery_template, verbose=True, output_key='tech', memory=discovery_memory)
overview_chain = LLMChain(llm=llm, prompt=overview_template, verbose=True, output_key='ovr', memory=overview_memory)

wiki = WikipediaAPIWrapper()


# Show stuff to the screen if there's a prompt
if prompt: 
    discovery = discovery_chain.run(prompt)
    wiki_research = wiki.run(prompt) 
    overview = overview_chain.run(discovery=discovery, wikipedia_research=wiki_research, overview=prompt)

    st.write(discovery) 
    st.write(overview) 

    with st.expander('Technology Discovery History'): 
        st.info(discovery_memory.buffer)

    with st.expander('Overview History'): 
        st.info(overview_memory.buffer)

    with st.expander('Wikipedia Research'): 
        st.info(wiki_research)

# vector store
#text_splitter = RecursiveCharacterTextSplitter(
#    chunk_size=100,
#    chunk_overlap=0,
#)

#texts = text_splitter.create_documents([prompt])


# embeddings
#embeddings = OpenAIEmbeddings(model='ada')
#query_results = embeddings.query(texts, texts, n=5)