import os
from langchain_openai import ChatOpenAI

os.environ["OPENAI_API_KEY"] = "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"

llm = ChatOpenAI(
    model="gpt-3.5-turbo", 
    temperature=0)

response = llm.invoke(
    "Explain the theory of relativity in simple terms.")
print(response.content)

print("="*100)

from langchain_google_genai import ChatGoogleGenerativeAI

os.environ["GOOGLE_API_KEY"] = "AIzaSyCSgV0Iz-YDeu_317J7QIRvYXrw-p-lslQ"

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash", 
    temperature=0)

response = llm.invoke(
    "What is quantum computing?")
print(response.content)

print("="*100)

from langchain_groq import ChatGroq

os.environ["GROQ_API_KEY"] = "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"

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