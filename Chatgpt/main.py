from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv


load_dotenv()

@tool
def add_numbers(a: float, b: float) -> str:
    """Add two numbers together."""
    return f"The sum of {a} and {b} is {a + b}."

def main():
    model = ChatOpenAI(temperature=0)

    tools = [add_numbers]
    agent_executor = create_react_agent(model, tools)

    print("Hi i'm Your AI assistant. How can I help you today? (type 'q' to quit)")
    
    while True:
        user_input = input("\nYou: ").strip()

        if user_input.lower() == 'q':
            break

        print(f"\nAssistant: ", end="")
        for chunk in agent_executor.stream(
            {"messages": [HumanMessage(content=user_input)]}
        ):
            if "agent" in chunk and "messages" in chunk["agent"]:
                for message in chunk["agent"]["messages"]:
                    print(message.content, end="")
        print()

if __name__ == "__main__":
    main()        