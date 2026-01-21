# Zep Memory Assistant

We're building an AI Agent with human-like memory which integrates [Zep's](https://www.getzep.com/) long-term memory backend with Microsoft's AutoGen framework, enabling agents to retain, recall, and manage contextual memory across conversations—paving the way for more intelligent, personalized, and persistent multi-agent interactions.

We use:

- [Zep](https://www.getzep.com/) for the memory layer to AI agent
- Autogen (Agent Orchestration)
- Ollama as Model Provider
- Qwen 3 (LLM)
- Streamlit to wrap the logic in an interactive UI

## Set Up

Run these commands in project root

### Setting up Ollama

```bash
# Setting up Ollama on linux
curl -fsSL https://ollama.com/install.sh | sh

# Pull the Qwen 3 4B model
ollama pull qwen3:4b
```

### Install Dependencies

```bash
uv sync
```

### Run the Application

Run the application with:

```bash
streamlit run app.py
```

[Get your Zep API keys here](https://www.getzep.com/)


