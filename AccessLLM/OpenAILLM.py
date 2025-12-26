import os
os.environ["OPENAI_API_KEY"] = "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"

from openai import OpenAI

client = OpenAI()

# response = client.responses.create(
#     model="gpt-4.1-2025-04-14",
#     input= "Tell me a joke about programming."
# )
# print(response.output[0].content[0].text)

chat_history=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is Machine Learning?"}
    ]
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages = chat_history
)
response = completion.choices[0].message.content
print(response)

chat_history.append({"role": "assistant", "content": response})
chat_history.append({"role": "user", "content": "Explain it in simple terms."})
completion1 = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages = chat_history
)
response = completion1.choices[0].message.content
print(response)

