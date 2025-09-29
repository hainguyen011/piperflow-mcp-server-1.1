# PIPERFLOW MCP SERVER VERSION 1.1 USING PYTHON SDK

## Overview

- Manage and expose **Prompts, Tools, and Resources** in MCP standard.
- Support **multi-server architecture**: prompt server, tool server, resource server, orchestration server.
- Plugin-style extensibility: add new tools or prompts simply by placing files in their folders.
- Quick integration with MCP clients or external HTTP/REST gateways.

## Features

**Tool Server**: expose math, search, or custom tools via MCP.
**Prompt Server**: central repository for system or agent prompts.
**Resource Server**: unified access to databases, APIs, or knowledge bases.
**Orchestration Server**: optional meta-server to route and aggregate requests from multiple MCP servers.
**Gateway**: optional HTTP API to interact with MCP servers externally.
**Auto-Discovery**: tools, prompts, and resources are auto-loaded from their folders.
**Plugin-Friendly**: add new tool or prompt without modifying server code.
**JSON-RPC over MCP**: standardized client-server communication.
**Logging & Config**: centralized logging and environment-based configuratio

## Installation

### Adding MCP to your python project

We recommend using [uv](https://docs.astral.sh/uv/) to manage your Python projects.

If you haven't created a uv-managed project yet, create one:

   ```bash
   uv init mcp-server-demo
   cd mcp-server-demo
   ```

   Then add MCP to your project dependencies:

   ```bash
   uv add "mcp[cli]"
   ```

Alternatively, for projects using pip for dependencies:

```bash
pip install "mcp[cli]"
```

### Running the standalone MCP development tools

To run the mcp command with uv:

```bash
uv run mcp
```

## Quickstart

To run the mcp server 

```bash
mcp dev servers/mcp_tool_server/app.py      # Your mcp tool server
mcp dev servers/mcp_prompt_server/app.py    # Your mcp prompts server
mcp dev servers/mcp_resource_server/app.py    # Your mcp resource server
```

