import argparse
import os
import sys

from langchain.llms import OpenAI
from llama_index import GPTSimpleVectorIndex, LLMPredictor, ServiceContext

PROMPT_TEMPLATE = """
Answer the question below based on the book as if you were the author.

Question: {question}

Answer to the question in the same language as the question.
"""

if os.environ.get("OPEN_API_KEY") == "":
    print("'OPEN_API_KEY' not set", file=sys.stderr)
    sys.exit(1)

def chat_for_github_repo():
    index = load_index()

    print("Question: ", end="", flush=True)

    try:
        while question := next(sys.stdin).strip():
            prompt = PROMPT_TEMPLATE.format(question=question)
            output = index.query(prompt, similarity_top_k=5)
            print("Answer: ", end="")
            print(output)
            print("")
            print("Question: ", end="", flush=True)
    except KeyboardInterrupt:
        print("Bye!")
        pass

def load_index():
    print("Loading index...\n")
    return GPTSimpleVectorIndex.load_from_disk(
        "index.json",
        service_context=get_service_context(),
    )

def get_service_context():
    llm_predictor = LLMPredictor(llm=OpenAI(temperature=0, model_name="text-davinci-003"))
    return ServiceContext.from_defaults(llm_predictor=llm_predictor)

def main():
    chat_for_github_repo()

if __name__ == "__main__":
    main()
