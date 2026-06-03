import os
from typing import Optional

def overwrite_markdown(file_path: str, content: str) -> str:
    """Overwrites the markdown file with new content."""
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return f"Successfully updated {file_path}."
    except Exception as e:
        return f"Error writing to file: {str(e)}"

def patch_markdown(file_path: str, search_string: str, replace_string: str) -> str:
    """Finds and replaces a specific block of text in the markdown file."""
    try:
        if not os.path.exists(file_path):
            return f"Error: File at {file_path} does not exist."
            
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if search_string not in content:
            return "Error: The search_string could not be found exactly as provided in the file."
            
        updated_content = content.replace(search_string, replace_string, 1) # Limit to 1 replace for safety
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
            
        return f"Successfully patched {file_path}."
    except Exception as e:
        return f"Error patching file: {str(e)}"