from fastmcp import FastMCP
from Tools.CreateFile import CreateFile#, PageTypes, Confindence
from Tools.ReadFile import read_path
mcp = FastMCP("Knowledge Agent")
#add tools
mcp.add_tool(CreateFile)
mcp.add_tool(read_path)
#add prompts
@mcp.prompt
def ingest_source(source: str) -> str:
    """
    When the user says "ingest [source]":
        1. Read the source 
        2. Create a summary of the source with CreateFile tool
        3. Identify and record all concepts, entities, and strategies with the CreateFile tool"""
    # Placeholder for actual ingestion logic
    return f"Ingested source: {source[:100]}..."  # Return a preview of the source
@mcp.prompt
def ingest_changes() -> str:
    """
    When the user says "ingest changes":
        1. Identify any new or updated sources since the last ingestion
        2. Read and summarize these sources with the CreateFile tool
        3. Update the knowledge base with any new concepts, entities, or strategies"""
    # Placeholder for actual change ingestion logic
    return "Ingested changes since last update."
@mcp.prompt
def query(query: str) -> str:
    """
    When the user says "query [query]":
        1. Search the ingested knowledge base for relevant information
        2. Return a concise answer to the query based on the ingested information"""
    # Placeholder for actual query logic
    return f"Answer to query: {query[:100]}..."  # Return a preview of the query
@mcp.prompt
def lint() -> str:
    """
    When the user says "lint":
        1. Review the ingested knowledge base for consistency, accuracy, and completeness
        2. Identify any gaps or areas for improvement in the knowledge base
        3. Provide recommendations for enhancing the knowledge base"""
    # Placeholder for actual linting logic
    return "Linting completed. No issues found."

if __name__ == "__main__":
    # Run the server
    mcp.run(transport="stdio")
