import os
import streamlit as st
import pickle
import time
from langchain_openai import OpenAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredURLLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
import threading

from dotenv import load_dotenv
load_dotenv() # Add your openai api key in a .env file (OPENAI_API_KEY="OPENAI_API_KEY")



st.title("InsightExtractor AI-Powered Article Analyzer 📈")
st.sidebar.title("Article URLs")

urls = []
for i in range(3):
    url = st.sidebar.text_input(f"URL {i+1}")
    urls.append(url)


process_url_clicked = st.sidebar.button("Process URL")




main_placeholder = st.empty()
llm = OpenAI(temperature=0.9, max_tokens=500)

if process_url_clicked:
   
    loader = UnstructuredURLLoader(urls=urls)
    main_placeholder.text("Data Loading...Started...✅✅✅")
    data = loader.load()
    
    text_splitter = RecursiveCharacterTextSplitter(
        separators=['\n\n', '\n', '.', ','],
        chunk_size=1000
    )
    main_placeholder.text("Text Splitter...Started...✅✅✅")
    docs = text_splitter.split_documents(data)

    embeddings = OpenAIEmbeddings()
    vectorstore_openai = FAISS.from_documents(docs, embeddings)
    main_placeholder.text("Embedding Vector Started Building...✅✅✅")
    time.sleep(2)

    main_placeholder.text("Data Loaded and Processed Successfully...✅✅✅")



query = main_placeholder.text_input("Question: ")
if query:       
        chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=vectorstore_openai.as_retriever())
        result = chain({"question": query}, return_only_outputs=True)
        
        st.header("Answer")
        st.write(result["answer"])

        
        sources = result.get("sources", "")
        if sources:
            st.subheader("Sources:")
            sources_list = sources.split("\n")  
            for source in sources_list:
                st.write(source)
