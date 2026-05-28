from fastmcp import FastMCP

mcp = FastMCP("Knowledge Agent")

if __name__ == "__main__":
    # Run the server
    mcp.run(transport="stdio")
