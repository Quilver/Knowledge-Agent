from fastmcp import FastMCP
from Tools.CreateFile import CreateFile, PageTypes, Confindence
mcp = FastMCP("Knowledge Agent")
#add tools
mcp.add_tool(CreateFile)
#add prompts
#@mcp.prompt
def ingest_source(source: str) -> str:
    """
    When the user says "ingest [source]":
        1. Read the source 
        2. Create a summary of the source with CreateFile tool
        3. Identify and record all concepts, entities, and strategies with the CreateFile tool"""
    # Placeholder for actual ingestion logic
    return f"Ingested source: {source[:100]}..."  # Return a preview of the source
if __name__ == "__main__":
    # Run the server
    mcp.run(transport="stdio")
