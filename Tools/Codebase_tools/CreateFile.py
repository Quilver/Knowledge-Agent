
from typing import Any, Dict, Type, List
import yaml, re, os
from datetime import datetime


def slugify(title: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
def updateTags(tags: List[str]):
    FILE_ROOT = "E:/Obsidian/LLM Guide"
    WIKI_ROOT = FILE_ROOT+ "/LLM/wiki"
    #add tags 
    _tags = open(f"{WIKI_ROOT}/tags.md", 'r', encoding='utf-8')
    for line in _tags:
        tag = line.strip().strip('[]')
        if tag not in tags:
            tags.append(tag)

    with open(WIKI_ROOT+"/tags.md", 'w', encoding='utf-8') as f:
        for tag in tags:
            f.write(f"[[{tag}]]\n")

def CreateFile(title: str, section:str, content:str, tags:List[str]):
    FILE_ROOT = "E:/Obsidian/LLM Guide"
    WIKI_ROOT = FILE_ROOT+ "/LLM/wiki"
    file_path=f"{WIKI_ROOT}/{section}/{slugify(title)}.md"
    os.makedirs(f"{WIKI_ROOT}/{section}", exist_ok=True)
    #Create the file
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    ##add to index 
    with open(WIKI_ROOT+"/index.md", 'a', encoding='utf-8') as f:
        f.write(f"[[{section}/{slugify(title)}]]:{tags} \n")
    #add to log
    with open(WIKI_ROOT+"/log.md", 'a', encoding='utf-8') as f:
        f.write(f"\n{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Created {section} page: {title} with tags {tags}")
    

def CreateInterface(title: str, description: str, Functions: List[str], tags: List[str]):
    """
    Creates an interface wiki page.This page describes the role of the interface and how it communicated with other interfaces.

    Args:
        title: name of the wiki page
        tags: list of tags
        sources: list of files that were used to create this file
        description: description of the interface and its communication with other interfaces.
        Functions: list of functions that belong to this interface.
    """
    content = yaml.dump({
        "title": title,
        "description": description,
        "functions": Functions,
        "tags": tags
    }, sort_keys=False) 
    content = f"---\n{content}---\n"
    CreateFile(title, "interfaces", content, tags)
def CreateDataTypes(title: str, description: str, attributes: List[str], tags: List[str]):
    """
    Creates a data type wiki page.This page describes the data type, its usage, and the attributes it is composed of.

    Args:
        title: name of the wiki page
        tags: list of tags
        sources: list of files that were used to create this file
        description: description of the data type does, where it is used, and its inteded role.
        attributes: list of attributes that compose this data type, including descriptions of each attribute.
    """
    content = yaml.dump({
        "title": title,
        "description": description,
        "attributes": attributes,
        "tags": tags
    }, sort_keys=False)  
    content = f"---\n{content}---\n"
    CreateFile(title, "datatypes", content, tags)

def CreateFunction(title: str, description: str, interface: str, Inputs: List[str], outputs: List[str], tags: List[str], examples: List[str]):
    """
    Creates a function wiki page.This page describes the function, its usage, and runs through examples with edge cases.

    Args:
        title: name of the wiki page
        tags: list of tags
        sources: list of files that were used to create this file
        description: description of what the function does, when to use it, and how it is implemented.
        interface: the interface this function belongs to
        Inputs: list of inputs for this function
        outputs: list of outputs for this function
        examples: list of examples that show the outputs of the function given specific inputs, including edge cases.
    """
    content = yaml.dump({
        "title": title,
        "description": description,
        "interface": interface,
        "inputs": Inputs,
        "outputs": outputs,
        "tags": tags,
    }, sort_keys=False)
    content = f"---\n{content}---\n\n {examples}"
    CreateFile(title, "functions", content, tags)

def CreateUML(title: str, content: str, tags: List[str], sources: List[str]):
    """
    Creates a UML wiki page.This page shows the relationships between data types, functions, and interfaces.

    Args:
        title: name of the wiki page
        tags: list of tags
        sources: list of files that were used to create this file
        content: A mermaid UML diagram showing the relationships between data types, functions, and interfaces.
    """
    header = yaml.dump({
        "title": title,
        "tags": tags,
        "sources": sources
    }, sort_keys=False)
    content = f"---\n{header}---\n{content}"
    CreateFile(title, "uml", content, tags)
def CreateSummary(title: str, content: str, tags: List[str], sources: List[str]):
    """
    Creates a summary wiki page of a source file.

    Args:
        title: name of the wiki page
        tags: list of tags
        sources: list of files that were used to create this file. The first source should be the file that is being summarized, and the rest are dependencies.
        content: summary of source file
    """
    header = yaml.dump({
        "title": title,
        "tags": tags,
        "sources": sources
    }, sort_keys=False)
    content = f"---\n{header}---\n{content}"
    CreateFile(title, "summaries", content, tags)
