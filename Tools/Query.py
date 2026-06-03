import os
from typing import Optional
from enum import Enum
class documentTypes(Enum):
    raw="raw"
    markdown="markdown"
    txt="txt"
    csv="csv"
    pdf="pdf"
    jpg="jpg"
    png="png"
    folder="folder"

def read_document(file_path: str) -> str:
    """Reads the content of a document file. If the file is too large, it can be split into chunks and returned as a list of strings to be read by separate agents."""
    if not os.path.exists(file_path):
        return f"Error: File at {file_path} does not exist."
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()



print(documentTypes.markdown.value)
def read_markdown(file_path: str) -> str:
    """Reads the content of a markdown file."""
    if not os.path.exists(file_path):
        return f"Error: File at {file_path} does not exist."
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()