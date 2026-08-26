#!/usr/bin/env python3
"""
Main entry point for Solvian Chatbot
"""

import sys
from chatbot import Chatbot
from chatbot.utils import clean_text, validate_input, get_timestamp
from config import BOT_NAME, BOT_DESCRIPTION


def print_welcome_message():
    """Display welcome message"""
    print("\n" + "="*60)
    print(f"Welcome to {BOT_NAME}!")
    print(f"{BOT_DESCRIPTION}")
    print("="*60)
    print("Type 'quit' or 'exit' to end the conversation")
    print("Type 'clear' to reset conversation history")
    print("Type 'help' for available commands")
    print("="*60 + "\n")


def print_help():
    """Display help message"""
    print("\n" + "-"*60)
    print("Available Commands:")
    print("  quit/exit  - End the chatbot")
    print("  clear      - Clear conversation history")
    print("  help       - Show this help message")
    print("  history    - Show conversation history")
    print("-"*60 + "\n")


def main():
    """Main function to run the chatbot"""
    print_welcome_message()
    
    try:
        chatbot = Chatbot()
        
        while True:
            try:
                # Get user input
                user_input = input(f"\nYou: ").strip()
                
                # Handle empty input
                if not user_input:
                    continue
                
                # Handle commands
                if user_input.lower() in ['quit', 'exit']:
                    print(f"\n{BOT_NAME}: Goodbye! Have a great day!")
                    break
                
                if user_input.lower() == 'clear':
                    chatbot.reset_conversation()
                    print(f"{BOT_NAME}: Conversation history cleared.")
                    continue
                
                if user_input.lower() == 'help':
                    print_help()
                    continue
                
                if user_input.lower() == 'history':
                    history = chatbot.get_history()
                    if history:
                        print("\nConversation History:")
                        for i, msg in enumerate(history, 1):
                            print(f"  {i}. {msg['role'].upper()}: {msg['content'][:100]}...")
                    else:
                        print("\nNo conversation history yet.")
                    continue
                
                # Validate and clean input
                if not validate_input(user_input):
                    print(f"{BOT_NAME}: Please enter a valid message (1-5000 characters)")
                    continue
                
                clean_input = clean_text(user_input)
                
                # Get response from chatbot
                print(f"\n{BOT_NAME}: ", end="", flush=True)
                response = chatbot.send_message(clean_input)
                print(response)
                
            except KeyboardInterrupt:
                print(f"\n\n{BOT_NAME}: Conversation interrupted. Goodbye!")
                break
            except Exception as e:
                print(f"\n{BOT_NAME}: An error occurred: {str(e)}")
                continue
    
    except Exception as e:
        print(f"Error initializing chatbot: {str(e)}")
        print("Make sure you have set up your environment variables correctly.")
        print("See .env.example for configuration details.")
        sys.exit(1)


if __name__ == "__main__":
    main()
