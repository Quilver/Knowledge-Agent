from typing import Dict, List

import Agents.lmstudioAI as lmstudioAI
from Tools.Codebase_tools.CreateFile import CreateInterface, CreateDataTypes, CreateFunction, CreateUML, CreateSummary
#from Tools.CreateFile import CreateFile, PageTypes, Confindence
from Tools.ReadFile import read_path, read_wiki_path
import os
from dotenv import find_dotenv, load_dotenv
def prompt(file: str) -> str:
    file_path = f"Prompts/Code base/{file}"
    if not os.path.exists(file_path):
        return f"Error: File at {file_path} does not exist."
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()
env = load_dotenv(find_dotenv())
os.getenv("FILE_ROOT")
FILE_ROOT: str = str(os.getenv("FILE_ROOT"))
WIKI_ROOT = FILE_ROOT+ str(os.getenv("WIKI_ROOT"))

#Agent ingestion process:
#1. Write summaries for each file with links between files. Creating a graph
#2. Look at graph and create interfaces
#3. Create data types, functions, and UML diagrams for each interface

def summary_agent(content: str):
    system_message = f"{prompt("Rules.md")}\n\nCreate a summary of the page"
    tools =[CreateSummary]
    agent = lmstudioAI.agent(tools, system_message)
    agent.invoke({"messages": [lmstudioAI.HumanMessage(content=content)]})
def interface_agent(content: str):
    index = open(f"{WIKI_ROOT}/index.md", 'r', encoding='utf-8').read()
    tags = open(f"{WIKI_ROOT}/tags.md", 'r', encoding='utf-8').read()
    system_message = f"{prompt("Rules.md")}\n\nCreate interfaces based on the content. An interface is a collection of functions that work together to fullfil a specific role. Look for common themes in the content to group functions into interfaces."
    system_message += f"\n\nindex:\n{index}\n\ntags:\n{tags}"
    tools =[CreateInterface, read_wiki_path]
    agent = lmstudioAI.agent(tools, system_message)
    agent.invoke({"messages": [lmstudioAI.HumanMessage(content=content)]})
def detail_agent(content: str):
    index = open(f"{WIKI_ROOT}/index.md", 'r', encoding='utf-8').read()
    tags = open(f"{WIKI_ROOT}/tags.md", 'r', encoding='utf-8').read()
    system_message = f"{prompt("Rules.md")}\n\nCreate data types, functions, and UML diagrams for each interface. Use the content to find details about each function and data type. Use the index and tags to find links between different pages."
    system_message += f"\n\nindex:\n{index}\n\ntags:\n{tags}"
    tools =[CreateDataTypes, CreateFunction, CreateUML, read_wiki_path]
    agent = lmstudioAI.agent(tools, system_message)
    agent.invoke({"messages": [lmstudioAI.HumanMessage(content=content)]})
def loopFiles(files: Dict[str, List[str]], agent):
    for file, content in files.items():
        if len(content) == 0:
            print(f"Skipping empty file: {file}")
            continue
        print(f"\nProcessing file: {file}")
        agent(file + "\n\n" + content[0]  + "\ningest")
        print(" X")

loopFiles(read_path("E:/RM example"), summary_agent)
loopFiles(read_path(f"{WIKI_ROOT}/summaries"), interface_agent)
loopFiles(read_path(f"{WIKI_ROOT}/interfaces"), detail_agent)
