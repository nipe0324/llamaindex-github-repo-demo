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


def make_index_from_github_repo(owner, repo, branch, filter_directories, filter_file_extensions):
    print("Making index for repo: {}/{} with {} branch".format(owner, repo, branch))
    print("Filtering directories: {}".format(filter_directories))
    print("Filtering file extensions: {}".format(filter_file_extensions))

    # ref: https://llamahub.ai/l/github_repo
    github_client = GithubClient(os.getenv("GITHUB_TOKEN"))
    loader = GithubRepositoryReader(
        github_client,
        owner =                  owner,
        repo =                   repo,
        filter_directories =     (filter_directories, GithubRepositoryReader.FilterType.INCLUDE),
        filter_file_extensions = (filter_file_extensions, GithubRepositoryReader.FilterType.INCLUDE),
        verbose =                True,
        concurrent_requests =    10,
    )

    docs = loader.load_data(branch="main")

    index = GPTSimpleVectorIndex.from_documents(
        docs,
        service_context=get_service_context(),
    )
    index.save_to_disk("index.json")
    print("Index saved to index.json")

def get_service_context():
    llm_predictor = LLMPredictor(llm=OpenAI(temperature=0, model_name="text-davinci-003"))
    return ServiceContext.from_defaults(llm_predictor=llm_predictor)


def main(args):
    make_index_from_github_repo(
        args.owner,
        args.repo,
        args.branch,
        args.filter_directories,
        args.filter_file_extensions,
    )

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Make index file for a GitHub repo")
    parser.add_argument("--owner", help="GitHub repo owner", required=True)
    parser.add_argument("--repo", help="GitHub repo name", required=True)
    parser.add_argument("--branch", help="GitHub repo branch", default="main")
    parser.add_argument("--filter-directories", help="Directories to filter", default=["README.md", "docs"])
    parser.add_argument("--filter-file-extensions", help="File extensions to filter", default=[".md"])
    args = parser.parse_args()
    main(args)
