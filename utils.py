import os
from dotenv import load_dotenv
from crewai import LLM

load_dotenv()  # reads the .env file

def get_llm():
    return LLM(
        model=os.getenv("MODEL", "ollama/llama3.2"),
        base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"),
        temperature=0.7,
    )