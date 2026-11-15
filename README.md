Multi-Agent Article Writer (CrewAI + Ollama)
Planner → Writer → Editor agents that write a blog article on any topic, using local llama3.2.

Run
Install Ollama and run ollama pull llama3.2
python -m venv .venv and .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy .env.example to .env
python main.py