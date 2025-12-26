import os
from typing import List, Dict
from dotenv import load_dotenv
from llama_index.core import PromptTemplate
from llama_index.llms.groq import Groq

os.environ["GROQ_API_KEY"] = "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"

llm = Groq(
    model="llama-3.3-70b-versatile",
    temperature=0)

def run_llm_zeroshot(context: str, query: str, shots: List[Dict[str, str]]) -> str:

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

    formatted_prompt = PromptTemplate(template_str).format(context_str=context, query_str=query, examples=shots)
    response = llm.complete(formatted_prompt)
    output = response.text
    return output

shots = [
    {
        "context": "Positional encodings inject order information into sequences.",
        "question": "Why are positional encodings needed?",
        "answer": (
            "They give the model a sense of word order.\n"
            "- Without them, the model treats tokens as a bag of words.\n"
            "- Encodings ensure the sequence structure is preserved.\n"
            "Sources: lecture_notes.txt"
        )
    },
    {
        "context": "Multi-head attention projects queries, keys, and values into multiple subspaces.",
        "question": "What is the benefit of multi-head attention?",
        "answer": (
            "It lets the model learn from different representation subspaces.\n"
            "- Captures diverse relationships.\n"
            "- Improves contextual understanding.\n"
            "Sources: attention_paper.pdf"
        )
    },
]

context = (
    "Context from attention_mechanism.pdf"
    "In the attention mechanism, softmax is used on the similarity scores "
    "between queries and keys to produce attention weights."
)

query = "What does softmax do in attention?"

print(run_llm_zeroshot(context, query, shots))