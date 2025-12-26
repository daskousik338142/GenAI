import ollama

stream = ollama.chat(
    model="deepseek-r1:latest",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is Reinforcement Learning?"},
    ],
    stream=True
)

for chunk in stream:
    print(chunk["message"]["content"], end="", flush=True)