import argparse
import os
import sys

from langchain.llms import OpenAI
from llama_index import download_loader, GPTSimpleVectorIndex, LLMPredictor, ServiceContext
download_loader("GithubRepositoryReader")

from llama_index.readers.llamahub_modules.github_repo import GithubClient, GithubRepositoryReader

if os.environ.get("OPEN_API_KEY") == "":
    print("'OPEN_API_KEY' not set", file=sys.stderr)
    sys.exit(1)

if os.environ.get("GITHUB_TOKEN") == "":
    print("'GITHUB_TOKEN' not set", file=sys.stderr)
    sys.exit(1)


def make_index_from_github_repo(owner, repo, branch):
    print("Making index for repo: {}/{} with {} branch".format(owner, repo, branch))

    # ref: https://llamahub.ai/l/github_repo
    github_client = GithubClient(os.getenv("GITHUB_TOKEN"))
    loader = GithubRepositoryReader(
        github_client,
        owner =                  owner,
        repo =                   repo,
        # filter_directories =     (["README.md", "docs", "examples"], GithubRepositoryReader.FilterType.INCLUDE),
        filter_directories =     (["README.md"], GithubRepositoryReader.FilterType.INCLUDE),
        filter_file_extensions = ([".md"], GithubRepositoryReader.FilterType.INCLUDE),
        verbose =                True,
        concurrent_requests =    10,
    )

    docs = loader.load_data(branch="main")

    index = GPTSimpleVectorIndex.from_documents(
        docs,
        service_context=get_service_context(),
    )
    index.save_to_disk("index.json")

def get_service_context():
    llm_predictor = LLMPredictor(llm=OpenAI(temperature=0, model_name="text-davinci-003"))
    return ServiceContext.from_defaults(llm_predictor=llm_predictor)


def main(args):
    make_index_from_github_repo(args.owner, args.repo, args.branch)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Make index file for a GitHub repo")
    parser.add_argument("--owner", help="GitHub repo owner", required=True)
    parser.add_argument("--repo", help="GitHub repo name", required=True)
    parser.add_argument("--branch", help="GitHub repo branch", default="main")
    args = parser.parse_args()
    main(args)
