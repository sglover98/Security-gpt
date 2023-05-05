# Security-gpt

## Project Description

Security-GPT is a tool that utilizes the OPENAI api to provide your own personal cybersecurity reference bot. Refrerence Bots are a very recent tool being implemented on technical teams within companies. This code allows you to have this power on your own machine. 

# Note that this is in very early stages and will be going through many changes 

<img width="979" alt="Screenshot 2023-05-01 at 6 06 29 PM" src="https://user-images.githubusercontent.com/88252222/235692923-e36d60de-3714-493c-940d-c9f38394372e.png">


# Install 

1. pip install streamlit langchain openai wikipedia chromadb tiktoken pinecone
2. cd security-gpt 
3. open apikey.py
4. Generate and Insert Openai key inside of quotes (Follow link https://platform.openai.com/account/api-keys)
5. Save apikey.pi
3. Input into terminal***** stearmlit run main.py

#Future Changes
- Implementing vector database using Pincone.
- Add prompt template switches to allow for more flexability.
- Figure out controls annonymize input data.

# Change Log
- Added temporary memory to store output of query. (May 04, 2023)
- Added .env-sample file with instructions. (May 04, 2023)
- Added Wikipedia API (May 04, 2023)
