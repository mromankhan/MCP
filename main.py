from re import search
from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="hello-MCP", stateless_http=True)

@mcp.tool(name="online_researcher", description="Search the web for information")
def search_online(query: str) -> str:
    return f"Result of searching for {query}..."

@mcp.tool(name="check_weather", description="Check the weather in a given location")
def search_online(city: str) -> str:
    return f"weather in {city} is sunny..."

@mcp.tool(name="check_usage", description="Check the weather in a given location")
def search_online(city: str) -> str:
    return f"usage in db {city} is sunny..."


mcp_app = mcp.streamable_http_app()

