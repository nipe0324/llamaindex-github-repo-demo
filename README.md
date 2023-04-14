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

### Index GitHub repo

Make an index like this.

```
python make_index.py --repo-url https://github.com/jerryjliu/llama_index
```

### Ask with the GitHub repo

```
python ask.py --query "What abount llama_index repo?"
```
