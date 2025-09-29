from tools import load_tools

# Load tất cả tools từ folder
_ALL_TOOLS = load_tools()

# Có thể filter tool nào được expose
TOOLS = {
    name: tool for name, tool in _ALL_TOOLS.items()
    if not getattr(tool, "hidden", False)   # ví dụ: skip tool ẩn
}

def list_tools():
    """Trả về danh sách tool name + description"""
    return [
        {
            "name": tool.name,
            "description": getattr(tool, "description", "")
        }
        for tool in TOOLS.values()
    ]

def get_tool(name: str):
    """Lấy tool class theo name"""
    return TOOLS.get(name)
