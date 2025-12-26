import os
from dotenv import load_dotenv
from llama_index.core.llms import ChatMessage, MessageRole
from llama_index.llms.groq import Groq

# Load environment variables from .env file
load_dotenv()

llm = Groq(
    model="llama-3.3-70b-versatile", temperature=0.1)



def chat():
    chat_history = [
        ChatMessage(role=MessageRole.SYSTEM, content="You are a helpful assistant.")
    ]

    print("Langchain Chat with Groq LLM. Type 'exit' to quit.")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ("exit", "quit"):
            break
        if not user_input:
            continue

        chat_history.append(ChatMessage(role=MessageRole.USER, content=user_input))

        resp = llm.chat(chat_history)
        answer = resp.message.content

        print(f"Bot:, {answer})\n")

        print("="*50)

        chat_history.append(ChatMessage(role=MessageRole.ASSISTANT, content=answer))


chat()