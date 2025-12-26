import os
from llama_index.llms.openai import OpenAI
from llama_index.core.llms import ChatMessage

os.environ["OPENAI_API_KEY"] = "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"

llm = OpenAI(
    model="gpt-3.5-turbo", 
    temperature=0)

messages = [
    ChatMessage(role="system", content="You are a helpful assistant."),
    ChatMessage(role="user", content="What is the largest galaxy in the universe?"),
]

response = llm.chat(
    messages)
print(response)

print("="*100)

from llama_index.llms.google_genai import GoogleGenAI

os.environ["GOOGLE_API_KEY"] = "AIzaSyCSgV0Iz-YDeu_317J7QIRvYXrw-p-lslQ"

llm = GoogleGenAI(
    model="gemini-2.5-flash", 
    temperature=0)

response = llm.complete(
    "What is quantum computing?")
print(response.text)

print("="*100)

from llama_index.llms.groq import Groq

os.environ["GROQ_API_KEY"] = "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"

llm = Groq(
    model="llama-3.3-70b-versatile", 
    temperature=0)

response = llm.complete(
    "What are the symptoms of GERD")
print(response.text)

print("="*100)

from llama_index.llms.ollama import Ollama

llm = Ollama(
    model="deepseek-r1:latest", 
    base_url="http://localhost:11434",  # Explicit URL
    request_timeout=120.0,               # Longer timeout, default timeout was not working. Langchain was fine with default timeout.
    temperature=0)

response = llm.complete(
    "Tell me a programming joke")
print(response.text)