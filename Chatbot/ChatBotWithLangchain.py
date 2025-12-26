import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq

# Load environment variables from .env file
load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile", temperature=0.1)

parser = StrOutputParser()

def chat():
    chat_history = [
        ("system", "You are a helpful assistant."),
    ]

    print("Langchain Chat with Groq LLM. Type 'exit' to quit.")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "exit":
            break

        chat_history.append(("user", user_input))

        prompt = ChatPromptTemplate.from_messages(chat_history)

        chain = prompt | llm | parser

        response = chain.invoke({})

        print("Bot:", response)

        print("="*50)

        chat_history.append(("assistant", response))



chat()