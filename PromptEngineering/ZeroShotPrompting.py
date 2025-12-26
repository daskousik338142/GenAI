import os
from dotenv import load_dotenv
from llama_index.core import PromptTemplate
from llama_index.llms.groq import Groq

os.environ["GROQ_API_KEY"] = "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"

llm = Groq(
    model="llama-3.3-70b-versatile",
    temperature=0)

def run_llm_zeroshot(context: str, query: str) -> str:

    llm = Groq(
    model="llama-3.3-70b-versatile",
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

    formatted_prompt = PromptTemplate(template_str).format(context_str=context, query_str=query)
    response = llm.complete(formatted_prompt)
    output = response.text
    return output

context = (
    "Transformers use a self-attention mechanism that allows each token "
    "to attend to all other tokens in the sequence. This helps capture "
    "long-range dependencies without recurrence."
)

query = "How do Transformers handle long-range dependencies?"

print(run_llm_zeroshot(context, query))