from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Python MCP Server")

@mcp.tool()
def get_employee_info(name: str) -> str:
    """
        Get information about a given employee name:
        - name
        - salary
    """
    return {
        "employee_name": name,
        "salary": 5400
    }