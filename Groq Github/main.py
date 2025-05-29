import os
import requests
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

def github_user_info(username: str) -> str:
    """Fetch public GitHub user info by username."""
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    url = f"https://api.github.com/users/{username}"
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        data = resp.json()
        return (
            f"User: {data['login']}\n"
            f"Name: {data.get('name', 'N/A')}\n"
            f"Public Repos: {data['public_repos']}\n"
            f"Followers: {data['followers']}\n"
            f"Bio: {data.get('bio', 'N/A')}\n"
            f"Location: {data.get('location', 'N/A')}"
        )
    elif resp.status_code == 404:
        return "User not found."
    else:
        return f"Error: {resp.status_code} - {resp.text}"

def ask_groq(question: str) -> str:
    """Ask any question to Groq Llama 3 model."""
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama3-8b-8192",  # You can use "llama3-70b-8192" if you want
        "messages": [{"role": "user", "content": question}],
        "max_tokens": 300,
        "temperature": 0.7,
    }
    resp = requests.post(url, headers=headers, json=data)
    if resp.status_code == 200:
        return resp.json()["choices"][0]["message"]["content"].strip()
    else:
        return f"Groq API Error: {resp.status_code} - {resp.text}"

def main():
    print("Hi, I'm your assistant! Ask me anything. (type 'q' to quit)")
    print("You can also type 'github <username>' to get GitHub user info.")
    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() == 'q':
            break
        if user_input.lower().startswith("github "):
            username = user_input.split(" ", 1)[1]
            print("\n" + github_user_info(username))
        else:
            print("\n" + ask_groq(user_input))

if __name__ == "__main__":
    main()


