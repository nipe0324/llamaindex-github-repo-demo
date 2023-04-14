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
$ python make_index.py --owner jerryjliu --repo llama_index
Making index for repo: jerryjliu/llama_index with main branch
Filtering directories: ['README.md', 'docs']
Filtering file extensions: ['.md']
...
Index saved to index.json
```

### Ask abount GitHub repo

```$$
$ python chat.py
Loading index...
Question: What is llama_index?
Answer: LlamaIndex is a project that provides a central interface to connect your LLM's (Language Models) with external data. It offers data connectors to existing data sources and data formats, provides indices over unstructured and structured data for use with LLMs, provides an interface to query the index, and offers a comprehensive toolset trading off cost and performance.

Question: how to install llama-index?                   
Answer: To install LlamaIndex, run the following command: 

`pip install llama-index`
```
