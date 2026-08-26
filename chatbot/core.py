"""
Core chatbot logic for Solvian
"""

import openai
from config import OPENAI_API_KEY, MODEL_NAME, MAX_TOKENS, TEMPERATURE, TOP_P


class Chatbot:
    """Main Chatbot class for handling AI conversations"""
    
    def __init__(self):
        """Initialize the chatbot with OpenAI API"""
        openai.api_key = OPENAI_API_KEY
        self.conversation_history = []
        self.model = MODEL_NAME
        
    def send_message(self, user_message: str) -> str:
        """
        Send a message to the chatbot and get a response
        
        Args:
            user_message (str): The user's input message
            
        Returns:
            str: The chatbot's response
        """
        try:
            # Add user message to history
            self.conversation_history.append({
                "role": "user",
                "content": user_message
            })
            
            # Get response from OpenAI
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=self.conversation_history,
                max_tokens=MAX_TOKENS,
                temperature=TEMPERATURE,
                top_p=TOP_P
            )
            
            # Extract and store the assistant's response
            assistant_message = response['choices'][0]['message']['content']
            self.conversation_history.append({
                "role": "assistant",
                "content": assistant_message
            })
            
            return assistant_message
            
        except openai.error.OpenAIError as e:
            return f"Error: Unable to connect to AI service. {str(e)}"
        except Exception as e:
            return f"Error: {str(e)}"
    
    def reset_conversation(self):
        """Reset the conversation history"""
        self.conversation_history = []
        
    def get_history(self) -> list:
        """Get the conversation history"""
        return self.conversation_history