# AI Agent Python

## Overview
This project is a simple AI assistant built with Python. It can answer any question using the [Groq Llama 3 API](https://console.groq.com/keys) and fetch public GitHub user info using the GitHub API. No OpenAI key or quota is required—just a free Groq API key and a GitHub token.

## Key Features
- **Conversational AI:** Ask any question and get an answer from Llama 3 (via Groq).
- **GitHub Integration:** Type `github <username>` to get public info about any GitHub user.
- **Environment Configuration:** Uses `.env` for secure API key management.

## Ideal For
- Developers wanting a simple, extensible Python AI chatbot.
- Anyone looking for a free alternative to OpenAI for LLM-powered Q&A.
- Experimenting with Groq's Llama 3 API and GitHub API.

## Tech Stack
- **Language:** Python
- **AI/LLM:** Llama 3 via Groq API
- **API Integration:** GitHub REST API
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

### 3. Set up your API keys
- Go to [Groq Console](https://console.groq.com/keys), sign up, and create a free API key.
- Go to [GitHub Tokens](https://github.com/settings/tokens) and create a personal access token (classic) with `read:user` scope.
- Create a `.env` file in the project root and add:
  ```
  GROQ_API_KEY=gsk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
  GITHUB_TOKEN=ghp-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
  ```
  *(Replace with your actual keys)*

### 4. Run the assistant
```sh
python main.py
```

## Usage
- The assistant will greet you in the terminal.
- Type any question and press Enter to get an answer from Llama 3.
- To get GitHub user info, type: `github <username>`
- To exit, type `q` and press Enter.

## Example
```
You: What is the capital of France?
Assistant: The capital of France is Paris.

You: github saifullahhaaris
Assistant: 
User: saifullahhaaris
Name: Saifullah Haaris
Public Repos: 20
Followers: 0
Bio: SE undergraduate passionate about full-stack development with Java, Flutter, and AI. Quick learner and focused on building impactful solutions.
Location: Kegalle district, Srilanka.

---

**Note:**  
You must have valid Groq and GitHub API keys. Never commit your `.env` file or secrets to version control.