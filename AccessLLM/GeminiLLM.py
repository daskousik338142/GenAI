import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

from google import genai;
client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Tell me a joke about oceans."
)
print(response.text)

chat = client.chats.create(
    model="gemini-2.5-flash")

response = chat.send_message(
    "How many planets are there in the solar system?"
)
print(response.text)

print("-"*40)

response = chat.send_message("How many of them has atmosphere?")
print(response.text)

# chat_history=[
#         {"role": "system", "content": "You are a helpful assistant."},
#         {"role": "user", "content": "What is Machine Learning?"}
#     ]
# completion = client.chat.completions.create(
#     model="gemini-1.5-pro",
#     messages = chat_history
# )
# response = completion.choices[0].message.content
# print(response)
# chat_history.append({"role": "assistant", "content": response})
# chat_history.append({"role": "user", "content": "Explain it in simple terms."})
# completion1 = client.chat.completions.create(
#     model="gemini-1.5-pro",
#     messages = chat_history
# )
# response = completion1.choices[0].message.content
# print(response)
