import streamlit as st
import os
from utils import load_and_split, create_vectorstore, create_qa_chain

st.set_page_config(page_title="Simple RAG App")

st.title("📄 RAG App with LangChain + HuggingFace")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    st.success("File uploaded successfully!")

    with st.spinner("Processing document..."):
        docs = load_and_split("temp.pdf")
        vectorstore = create_vectorstore(docs)
        qa_chain = create_qa_chain(vectorstore)

    st.session_state.qa_chain = qa_chain

if "qa_chain" in st.session_state:
    query = st.text_input("Ask a question")

    if query:
        with st.spinner("Thinking..."):
            response = st.session_state.qa_chain.run(query)

        st.write("### Answer:")
        st.write(response)