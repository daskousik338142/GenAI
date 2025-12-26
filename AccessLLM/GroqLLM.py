import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

from groq import Groq

client = Groq()

chat_completion = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is deep Learning?"},
        {"role": "assistant", "content": "Deep Learning is a subset of machine learning that uses neural networks with many layers to analyze various types of data. It is particularly effective for tasks such as image and speech recognition."},
        {"role": "user", "content": "Give me some example"},
    ]
)
response = chat_completion.choices[0].message.content
print(response)