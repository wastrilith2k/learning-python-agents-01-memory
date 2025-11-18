import os
from dotenv import load_dotenv
from anthropic import Anthropic



def main():
    """Main conversation loop for the chatbot."""

    # Load environment variables
    load_dotenv()

    # Initialize the Anthropic client
    client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

    system_prompt = """You are a friendly and helpful AI Assistant. you provide clear, concise answers and ask clarifying questions when needed. You maintain a warm, conversational tone."""

    chat_history = []

    print("🤖 Chatbot started! Type 'quit' to exit.\n")

    # This is the conversation loop
    while True:
        # Get user input
        user_input = input("You: ").strip()

        # Check for exit command
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("Goodbye! 👋")
            break

        # Skip empty inputs
        if not user_input:
            continue

        chat_history.append({
            "role":"user",
            "content":user_input
        })

        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1024,
            system=system_prompt,
            messages=chat_history
        )

        bot_message = response.content[0].text

        chat_history.append({
            "role":"assistant",
            "content":bot_message
        })

        print(f"Assistant: {bot_message}")

if __name__ == "__main__":
    main()