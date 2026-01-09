from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="hello-MCP", stateless_http=True)

@mcp.tool(name="find_repo", description="Find github repo with given name")
def find_repo(name: str) -> str:
    print(f"Finding repo with name {name}...")
    return f"{name} repo found."

@mcp.tool(name="get_all_repo", description="Get all github repos")
def all_repo() -> str:
    return f"All repos."

@mcp.tool(name="delete_repo", description="delete github repo")
def delete_repo(id: str) -> str:
    return f"{id} Repo deleted sucessfully."

@mcp.tool(name="edit_repo", description="edit github repo")
def edit_repo(id: str) -> str:
    return f"{id} Repo edit sucessfully."

mcp_app = mcp.streamable_http_app()