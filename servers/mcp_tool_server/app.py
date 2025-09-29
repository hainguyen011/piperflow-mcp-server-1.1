
from mcp.server.fastmcp import FastMCP
from registry import list_tools, get_tool


# Create an MCP server
mcp = FastMCP("mcp_tool_server")

for meta in list_tools():
    ToolClass = get_tool(meta["name"])

    @mcp.tool(name=ToolClass.name, description=meta["description"])
    async def dynamic_tool(params: dict, tool_cls=ToolClass):
        tool = tool_cls()
        return tool.run(params)


if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')
