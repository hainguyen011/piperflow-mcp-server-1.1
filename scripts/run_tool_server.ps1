# Run Tool Server
$root = Split-Path -Parent $MyInvocation.MyCommand.Path
cd $root\..

Write-Host "🚀 Starting Tool Server..."
uv run python servers/mcp_tool_server/app.py
