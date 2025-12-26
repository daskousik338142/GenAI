import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load environment variables from .env file
load_dotenv()

llm = ChatOpenAI(
    model="gpt-3.5-turbo", 
    temperature=0)

response = llm.invoke(
    "Explain the theory of relativity in simple terms.")
print(response.content)

print("="*100)

from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash", 
    temperature=0)

response = llm.invoke(
    "What is quantum computing?")
print(response.content)

print("="*100)

from langchain_groq import ChatGroq

llm = ChatGroq(
    model="llama-3.3-70b-versatile", 
    temperature=0)

response = llm.invoke(
    "What are the symptoms of GERD")
print(response.content)

print("="*100)

from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="deepseek-r1:latest", 
    temperature=0)

response = llm.invoke(
    "Tell me a programming joke")
print(response.content)