# llamaindex-github-repo-demo

Demo LlamaIndex (GPT Index) with GitHub Repo.  
Index GitHub repo with ChatGPT. After indexing it, you can ask a question for the repo using ChatGPT.

## Usage

### Tool versions

- Python 3.10.4
- pip 3.10
- langchain 0.0.132
- llama_index 0.5.11

### Install libraries

```
pip install -r requirements.txt
```

### Set environment variables

- `OPENAI_API_KEY`: Your API Key for Open AI
- `GITHUB_TOKEN`: GitHub "classic" psersonal token with the `repo` scope. See [here](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) for instructions.

### Index GitHub repo

Make an index like this.

```
python make_index.py --owner jerryjliu --repo llama_index
```

### Ask with the GitHub repo

```
python ask.py --query "What abount llama_index repo?"
```
