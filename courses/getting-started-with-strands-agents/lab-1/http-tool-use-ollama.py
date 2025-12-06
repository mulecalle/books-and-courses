from strands import Agent
from strands.models.ollama import OllamaModel
from strands_tools import http_request

# Create an Ollama model
ollama_model = OllamaModel(
    host="http://localhost:11434",
    model_id="llama3.1"
)

dog_breed_helper = Agent(
    model=ollama_model,
    system_prompt="""You are a dog breed expert specializing
    in helping new pet parents decide what breed meets their lifestyles. Your expertise
    covers dog behavior, dog training, basic veterinary care, and dog breed standards.

    When giving recommendations:
    1. Provide both benefits and challenges of owning that breed.
    2. Only provide 3 recommendations at a time.
    3. Give examples when necessary
    4. Avoid jargon, but indicate when complex concepts are important

    Your goal is to help pet parents make an informed decision about their choice in a dog.
    """,
    tools=[http_request]  # Enables the agent to make HTTP requests to fetch information
)

query = """
Answer these questions:
1. Which dog should I adopt as a first time owner if I have an office job m-f 9-5, like to hike on weekends and don't know much about training?
2. Search wikipedia for the top 5 most popular dog breeds of the last 5 years.
"""
response = dog_breed_helper(query)
