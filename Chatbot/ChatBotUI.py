from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq

# Load environment variables from .env file
load_dotenv()


st.set_page_config(
    page_title="Generative AI Chatbot",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="auto"
)

st.title("🤖 Generative AI ChatBot")

# Initiate chat history

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for entry in st.session_state.chat_history:
    with st.chat_message(entry["role"]):
        st.markdown(entry["content"])

llm = ChatGroq(
    model="llama-3.3-70b-versatile", temperature=0.1)

user_prompt = st.text_input("You: ", placeholder="Type your message here...")

if user_prompt:
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})
    with st.chat_message("user"):
        st.markdown(user_prompt)

    chat_history = [("system", "You are a helpful assistant.")]
    for entry in st.session_state.chat_history:
        chat_history.append((entry["role"], entry["content"]))

    response = llm.invoke(chat_history)
    answer = response.content

    st.session_state.chat_history.append({"role": "assistant", "content": answer})
    with st.chat_message("assistant"):
        st.markdown(answer)