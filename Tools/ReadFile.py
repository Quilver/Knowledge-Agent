import os
from typing import Optional, Dict, List
from pathlib import Path
from enum import Enum
class documentTypes(Enum):
    markdown="markdown"
    code ="code"
    pdf="pdf"
    png="png"
    folder="folder"

def read_text_file(file_path: str) -> str:
    with open(file_path, 'r') as f:
        return f.read()
def chunk_text(text: str, max_size: int = 4000) -> List[str]:
    """Split text into chunks of max_size characters."""
    return [text[i:i + max_size] for i in range(0, len(text), max_size)]


def read_file(path: str, extension: str) -> str:
    if extension in [".txt", ".md", ".py", ".cs", ".cpp", ".json", ".yaml", ".yml", ".html", ".css", ".js"]:
        return read_text_file(path)

    #if extension == ".pdf":
        #return read_pdf(path)

    #if extension in [".png", ".jpg", ".jpeg", ".bmp", ".tiff"]:
        #return read_image(path)

    return "Could not read file"

def read_folder(path: Path) -> Dict[str, str]:
    results = {}

    for root, dirs, files in os.walk(path):
        # --- Skip hidden folders (those starting with ".") ---
        dirs[:] = [d for d in dirs if not d.startswith(".")]

        # --- Process files ---
        for file in files:
            if file.startswith(".") or file.startswith("__"):  # skip hidden files
                continue

            file_path = Path(root) / file
            try:
                results[str(file_path)] = read_file(str(file_path), file_path.suffix.lower())
            except Exception as e:
                results[str(file_path)] = f"ERROR: {e}"

    return results



def read_path(path_str: str, chunk_size: int = 4000) -> Dict[str, List[str]]:
    """
    Read a file or folder and return chunked text.
    Returns:
        { "filename": ["chunk1", "chunk2", ...] }
    """
    path = Path(path_str)

    if not path.exists():
        raise FileNotFoundError(f"Path not found: {path}")

    if path.is_dir():
        raw_results = read_folder(path)
    else:
        raw_results = {str(path): read_file(path_str, path.suffix.lower())}

    # chunk everything
    chunked = {
        filename: chunk_text(content, chunk_size)
        for filename, content in raw_results.items()
    }

    return chunked

'''
import os
import fnmatch
from pathlib import Path
from typing import Dict, List


def should_ignore(path: Path, ignore_hidden: bool, ignore_names: List[str], ignore_patterns: List[str]) -> bool:
    name = path.name

    # Hidden files/folders
    if ignore_hidden and name.startswith("."):
        return True

    # Exact name ignore (e.g., "node_modules", "dist")
    if name in ignore_names:
        return True

    # Pattern-based ignore (gitignore-style)
    for pattern in ignore_patterns:
        if fnmatch.fnmatch(name, pattern) or fnmatch.fnmatch(str(path), pattern):
            return True

    return False


def read_folder(
    path: Path,
    ignore_hidden: bool = True,
    ignore_names: List[str] = None,
    ignore_patterns: List[str] = None,
) -> Dict[str, str]:

    ignore_names = ignore_names or []
    ignore_patterns = ignore_patterns or []

    results = {}

    for root, dirs, files in os.walk(path):

        # Filter directories in-place
        dirs[:] = [
            d for d in dirs
            if not should_ignore(Path(root) / d, ignore_hidden, ignore_names, ignore_patterns)
        ]

        # Process files
        for file in files:
            file_path = Path(root) / file

            if should_ignore(file_path, ignore_hidden, ignore_names, ignore_patterns):
                continue

            try:
                results[str(file_path)] = read_file(file_path)
            except Exception as e:
                results[str(file_path)] = f"ERROR: {e}"

    return results

'''