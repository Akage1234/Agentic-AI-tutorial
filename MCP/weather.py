from mcp.server.fastmcp import FastMCP

mcp  = FastMCP("Weather")

@mcp.tool()
async def get_weather(location: str) -> str: 
    """Get the weather location"""
    return "Its always raining in california"

# Streamable-http argument tells the server to use http server

if __name__ == "__main__":
    mcp.run(transport="streamable-http")


