import os
from llama_index.core import PromptTemplate
from llama_index.llms.ollama import Ollama
# from llama_index.llms.groq import Groq  - If we want to test Groq LLM here

llm = Ollama(
    model="deepseek-r1:latest",
    base_url="http://localhost:11434",  # Explicit URL
    request_timeout=300.0,               # Longer timeout
    temperature=0)

template_str = (
    "You are an expert AI assistant.\n"
    "Use ONLY the use provided context to answer the user's question. "
    "If the context is insufficient or does not mention the answer, reply exactly: "
    "'Not enough information.'\n\n"
    "Context:\n{context_str}\n\n"
    "User Question: {query_str}\n\n"
    "Answering Rules:\n"
    "1) Be concise and precise (3–6 sentences, unless the question requires more).\n"
    "2) Use bullet points for lists.\n"
    "3) At the end, include a 'Sources:' section with short snippets or filenames from the context you used.\n\n"
    "Final Answer:"
)
prompt_template = PromptTemplate(template_str)
context = (
    "Machine learning is a subset of artificial intelligence (AI) that focuses on "
    "the development of algorithms and statistical models that enable computers to "
    "perform specific tasks without explicit instructions. It involves training "
    "models on large datasets to recognize patterns and make predictions or decisions "
    "based on new data."
)
query = "What is machine learning and how is it used in real-world applications?"
formatted_prompt = prompt_template.format(context_str=context, query_str=query)
print("Formatted Prompt:")
print(formatted_prompt)
print("\n" + "="*50 + "\n")
response = llm.complete(formatted_prompt)
print(response)
print("\n" + "="*50 + "\n")
context = (
    "Quantum computing is an area of computing focused on developing computer technology "
    "based on the principles of quantum theory, which explains the behavior of energy and "
    "material on the atomic and subatomic levels. Quantum computers use quantum bits or qubits"
    "that can exist in multiple states simultaneously, enabling them to process complex "
    "calculations much faster than classical computers for certain tasks."
)
query = "Explain quantum computing in simple terms."

formatted_prompt = prompt_template.format(context_str=context, query_str=query)
response = llm.complete(formatted_prompt)
print(response)
print("\n" + "="*50 + "\n")




