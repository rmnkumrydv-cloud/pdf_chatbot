import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.memory import ConversationBufferMemory
from langchain.chains.conversational_retrieval.base import ConversationalRetrievalChain
from langchain_groq import ChatGroq
from langchain.callbacks.base import BaseCallbackHandler
import os


class StreamHandler(BaseCallbackHandler):
    def __init__(self, container):
        self.container = container
        self.text = ""

    def on_llm_new_token(self, token: str, **kwargs):
        self.text += token
        self.container.markdown(self.text)


def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted
    return text


def get_text_chunks(raw_text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    return text_splitter.split_text(raw_text)


def get_vectorstore(text_chunks):
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    return FAISS.from_texts(texts=text_chunks, embedding=embeddings)


def get_conversation_chain(vectorstore):
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )

    llm = ChatGroq(
        groq_api_key=os.getenv("GROQ_API_KEY"),
        model_name="llama-3.3-70b-versatile",
        streaming=True
    )

    return ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )


def handle_userinput(user_question):
    with st.chat_message("user"):
        st.markdown(user_question)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        stream_handler = StreamHandler(message_placeholder)

        response = st.session_state.conversation(
            {"question": user_question},
            callbacks=[stream_handler]
        )

    st.session_state.chat_history = response["chat_history"]


def main():
    load_dotenv()
    st.set_page_config(page_title="Chat with multiple PDFs", page_icon="📚")
    st.title("Chat with multiple PDFs 📚")

    if "conversation" not in st.session_state:
        st.session_state.conversation = None

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    if st.session_state.chat_history:
        for i, message in enumerate(st.session_state.chat_history):
            if i % 2 == 0:
                with st.chat_message("user"):
                    st.markdown(message.content)
            else:
                with st.chat_message("assistant"):
                    st.markdown(message.content)

    user_question = st.chat_input("Ask a question about your documents")

    if user_question:
        if st.session_state.conversation:
            handle_userinput(user_question)
        else:
            st.warning("Upload and process documents first.")

    with st.sidebar:
        st.subheader("Your Documents")

        pdf_docs = st.file_uploader(
            "Upload your PDFs and click Process",
            accept_multiple_files=True
        )

        if st.button("Process"):
            if pdf_docs:
                with st.spinner("Processing..."):
                    raw_text = get_pdf_text(pdf_docs)
                    text_chunks = get_text_chunks(raw_text)
                    vectorstore = get_vectorstore(text_chunks)
                    st.session_state.conversation = get_conversation_chain(vectorstore)
                st.success("Documents processed successfully!")
            else:
                st.warning("Please upload at least one PDF.")


if __name__ == "__main__":
    main()
