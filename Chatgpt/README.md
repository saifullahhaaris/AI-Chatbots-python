# AI Agent Python

## Overview
This project is a simple AI assistant built with Python, leveraging [LangChain](https://python.langchain.com/), [OpenAI](https://platform.openai.com/), and [LangGraph](https://github.com/langchain-ai/langgraph). The assistant can interact with users in natural language and perform basic tool-augmented tasks using the OpenAI API.

## Key Features
- **Conversational AI:** Chat with the assistant in your terminal.
- **Tool Integration:** Includes a sample tool for adding numbers; easily extendable for more tools.
- **OpenAI LLM Integration:** Uses OpenAI's GPT models for natural language understanding and response.
- **Environment Configuration:** Uses `.env` for secure API key management.

## Ideal For
- Developers learning about AI agents and LangChain.
- Anyone wanting a simple, extensible Python AI chatbot.
- Experimenting with OpenAI's API and tool augmentation.

## Tech Stack
- **Language:** Python
- **AI/LLM:** OpenAI GPT (via `langchain_openai`)
- **Agent Framework:** LangChain, LangGraph
- **Environment Management:** python-dotenv

## Getting Started

### 1. Clone the repository
```sh
git clone https://github.com/saifullahhaaris/AI-agent-python.git
cd AI-agent-python
```

### 2. Install dependencies
It is recommended to use a virtual environment:
```sh
python -m venv .venv
.venv\Scripts\activate  # On Windows
pip install -r requirements.txt
```

### 3. Set up your OpenAI API key
- Go to [OpenAI API Keys](https://platform.openai.com/api-keys)
- Click **Create new secret key**
- Copy the key (it starts with `sk-`)
- Create a `.env` file in the project root (if not present) and add:
  ```
  OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
  ```
  *(Replace with your actual OpenAI key)*

### 4. Run the assistant
```sh
python main.py
```
or, if using `uv`:
```sh
uv run main.py
```

## Usage
- The assistant will greet you in the terminal.
- Type your question or command and press Enter.
- To exit, type `q` and press Enter.

## Extending the Agent
You can add more tools by defining new functions with the `@tool` decorator and adding them to the `tools` list in `main.py`.

---

**Note:**  
You must have a valid OpenAI API key with sufficient quota. If you encounter quota or authentication errors, check your key and billing status at [OpenAI Usage](https://platform.openai.com/account/usage).

---