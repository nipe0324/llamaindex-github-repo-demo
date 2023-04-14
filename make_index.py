import argparse

def make_index_from_github_repo(repo_url):
    print("Making index for repo: {}".format(repo_url))

def main(args):
    make_index_from_github_repo(args.repo_url)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Make index file for a GitHub repo")
    parser.add_argument("--repo-url", help="GitHub repo url", required=True)
    args = parser.parse_args()
    main(args)
