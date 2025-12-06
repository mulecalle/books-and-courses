import os

import uvicorn
from strands import Agent
from strands_tools.a2a_client import A2AClientToolProvider
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from strands.models.ollama import OllamaModel

EMPLOYEE_AGENT_URL = "http://localhost:8001"

app = FastAPI(title="HR Agent API")

class QuestionRequest(BaseModel):
    question: str

@app.get("/health")
def health_check():
    return {"status": "healthy"}

# Create an Ollama model
ollama_model = OllamaModel(
    host="http://localhost:11434",
    model_id="llama3.1"
)

@app.post("/inquire")
async def ask_agent(request: QuestionRequest):
    async def generate():
        provider = A2AClientToolProvider(known_agent_urls=[EMPLOYEE_AGENT_URL])

        agent = Agent(
            model=ollama_model, 
            tools=provider.tools,
            system_prompt=f"""You are an HR agent. To answer questions about employees, you MUST use the a2a_send_message tool.

CRITICAL RULES:
- You MUST use a2a_send_message tool to communicate with the employee agent
- The employee agent URL is EXACTLY: {EMPLOYEE_AGENT_URL}
- ALWAYS use target_agent_url="{EMPLOYEE_AGENT_URL}" in your a2a_send_message calls
- NEVER use placeholder URLs like "https://example.com" or make up URLs
- If you need to discover the agent first, use a2a_discover_agent with url="{EMPLOYEE_AGENT_URL}"

When the user asks about employees, forward their question to the employee agent using a2a_send_message with target_agent_url="{EMPLOYEE_AGENT_URL}"."""
        )

        stream_response = agent.stream_async(request.question)

        async for event in stream_response:
            if "data" in event:
                yield event["data"]

    return StreamingResponse(
        generate(),
        media_type="text/plain"
    )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)