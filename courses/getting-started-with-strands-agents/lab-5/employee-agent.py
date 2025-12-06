import os

from mcp.client.streamable_http import streamablehttp_client
from strands import Agent
from strands.tools.mcp.mcp_client import MCPClient
from strands.multiagent.a2a import A2AServer
from urllib.parse import urlparse
from strands.models.ollama import OllamaModel

# Define URLs correctly - do not use os.environ.get() for literal values
EMPLOYEE_INFO_URL = "http://localhost:8002/mcp"
EMPLOYEE_AGENT_URL = "http://localhost:8001"

# Create the MCP client
employee_mcp_client = MCPClient(lambda: streamablehttp_client(EMPLOYEE_INFO_URL))

# Create an Ollama model
ollama_model = OllamaModel(
    host="http://localhost:11434",
    model_id="llama3.1"
)

# Using the MCP client within a context
with employee_mcp_client:
    tools = employee_mcp_client.list_tools_sync()

    # Create a Strands agent
    employee_agent = Agent(
        model=ollama_model,
        name="employee-agent",
        description="Answers questions about employees",
        tools=tools,
        system_prompt=(
            "You must answer using ONLY employee names and skills from the available data. "
            "NEVER make up or hallucinate names or skills. "
            "When listing employees, always abbreviate their first names (e.g., J. Smith) and provide all their skills from the records. "
            "If the information is not available in the data, you must say 'I do not have that information.'"
        )
    )

    # Create A2A server
    a2a_server = A2AServer(
        agent=employee_agent,
        version='1.2.3',
        port=8001,
        http_url=EMPLOYEE_AGENT_URL
    )

    # Start the server
    if __name__ == "__main__":
        a2a_server.serve(host="0.0.0.0", port=8001)