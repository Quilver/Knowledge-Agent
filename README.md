# Local Knowledge Agent
 I am inspired by Andrej Karpathy's wiki ([llm-wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)) to build an agent that can run locally to provide local automatic documentation. Currently I am working on the ingestion pipeline and am trying to decide between building more custom tooling vs prebuilt tools like cognee or graphify

## Code base ingestion
[IngestCodeAgent.py](https://github.com/Quilver/Knowledge-Agent/blob/main/IngestCodeAgent.py "IngestCodeAgent.py")
An ingestion tool for codebases. 

## Cognee Knowledge Graphs
[KnowledgeGraph.py](https://github.com/Quilver/Knowledge-Agent/blob/main/Agents/KnowledgeGraph.py)
Cognee provides a flexible method for building up knowledge graphs. However I am still studying the library
## Docling Document readers
[PDF reader](https://github.com/Quilver/Knowledge-Agent/blob/main/Agents/readPDFv2.py)
Docling is a library for converting rich documents into a more AI friendly formats such as .md

# Setup
I am running everything locally on windows and using lmstudio. You can use the .toml file for the packages and here is how the .env is setup.
``` yaml
DATA_ROOT_DIRECTORY="~/.cognee_data"

SYSTEM_ROOT_DIRECTORY="~/.cognee_system"

  

LLM_PROVIDER="custom"

LLM_MODEL=MODEL_ID

LLM_ENDPOINT="http://localhost:1234/v1"

LLM_API_KEY="."

LLM_INSTRUCTOR_MODE="json_schema_mode"

  

# Change custom to openai_compatible

EMBEDDING_PROVIDER="openai_compatible"

# Use a clean model name or keep your identifier string

EMBEDDING_MODEL=EMBEDDING_MODEL_ID

EMBEDDING_ENDPOINT="http://127.0.0.1:1234/v1/embeddings"

EMBEDDING_API_KEY="."

EMBEDDING_DIMENSIONS=

  

COGNEE_Folder= SAVE COGNEE LOCATION

  

FILE_ROOT = OBSIDIAN VAULT

WIKI_ROOT = "/YOLO/wiki"

SOURCE = CODE_BASE_TO_READ

base_url="http://localhost:1234/v1"

MODEL_ID = MODEL_ID
```
