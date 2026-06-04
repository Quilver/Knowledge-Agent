import Agents.lmstudioAI as lmstudioAI
from Tools.Codebase_tools.CreateFile import CreateInterface, CreateDataTypes, CreateFunction, CreateUML, CreateSummary
from Tools.CreateFile import CreateFile, PageTypes, Confindence
from Tools.ReadFile import read_path
import os
def prompt(file: str) -> str:
    file_path = f"Prompts/Code base/{file}"
    if not os.path.exists(file_path):
        return f"Error: File at {file_path} does not exist."
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

#Test codebase 
files =  read_path("E:/RM example")


rules = prompt("Rules.md")
ingest = prompt("Ingest.md")
system_message = f"{rules}\n\n{ingest}"
tools = [CreateInterface, CreateDataTypes, CreateFunction, CreateUML, CreateSummary, read_path]
FILE_ROOT = "E:/Obsidian/LLM Guide"
WIKI_ROOT = FILE_ROOT+ "/LLM/wiki"
for file, content in files.items():
    index = open(f"{WIKI_ROOT}/index.md", 'r', encoding='utf-8').read()
    tags = open(f"{WIKI_ROOT}/tags.md", 'r', encoding='utf-8').read()
    system_message += f"\n\nindex:\n{index}\n\ntags:\n{tags}"
    if len(content) == 0:
        print(f"Skipping empty file: {file}")
        continue
    print(f"\nIngesting file: {file}")
    agent = lmstudioAI.agent(tools, system_message)
    human_message = file + "\n\n" + content[0]  + "\ningest" # Use the first chunk for simplicity
    result = agent.invoke({"messages": [lmstudioAI.HumanMessage(content=human_message)]})
    print(" X")

#result = agent.invoke()