from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="hello-MCP", stateless_http=True)

@mcp.tool(name="check_weather", description="Check the weather in a given location")
def search_online(city: str) -> str:
    print(f"Checking weather for {city}...")
    return f"weather in {city} is sunny..."

@mcp.tool(name="find_repo", description="Find github repo with given name")
def find_repo(name: str) -> str:
    print(f"Finding repo with name {name}...")
    return f"{name} repo found."

@mcp.tool(name="get_all_repo", description="Get all github repos")
def find_repo() -> str:
    return f"All repos."

@mcp.tool(name="delete_repo", description="delete github repo")
def find_repo(id: str) -> str:
    return f"{id} Repo deleted sucessfully."

mcp_app = mcp.streamable_http_app()