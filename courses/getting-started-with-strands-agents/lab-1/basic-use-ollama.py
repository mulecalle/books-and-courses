from strands import Agent
from strands.models.ollama import OllamaModel

# https://strandsagents.com/latest/documentation/docs/user-guide/concepts/model-providers/ollama/

# Create an Ollama model instance
ollama_model = OllamaModel(
    host="http://localhost:11434",  # The address of the Ollama server
    model_id="llama3:8b",           # The Ollama model identifier
    keep_alive='10m', # How long the model stays loaded in memory
    max_tokens=None, # Maximum number of tokens to generate
    temperature=0.1, # Controls randomness (higher = more random)
    top_p=None, # Controls diversity via nucleus sampling
    stop_sequences=None, # List of sequences that stop generation
    options=None, # Additional model parameters (e.g., top_k)
    additional_args=None # Any additional arguments for the request
)

# Create an agent using the Ollama model
agent = Agent(model=ollama_model)

# Use the agent
agent("Tell me about Strands agents.") # Prints model output to stdout by default