"""
Utility functions for Solvian Chatbot
"""

import re
from datetime import datetime


def clean_text(text: str) -> str:
    """
    Clean and normalize text input
    
    Args:
        text (str): Raw text input
        
    Returns:
        str: Cleaned text
    """
    # Remove extra whitespace
    text = ' '.join(text.split())
    # Remove special characters (optional)
    # text = re.sub(r'[^a-zA-Z0-9\s\?\!\.\/,]', '', text)
    return text.strip()


def get_timestamp() -> str:
    """Get current timestamp in readable format"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def validate_input(user_input: str, min_length: int = 1, max_length: int = 5000) -> bool:
    """
    Validate user input
    
    Args:
        user_input (str): User's input text
        min_length (int): Minimum allowed length
        max_length (int): Maximum allowed length
        
    Returns:
        bool: True if valid, False otherwise
    """
    if not user_input:
        return False
    
    if len(user_input) < min_length or len(user_input) > max_length:
        return False
    
    return True


def format_response(response: str) -> str:
    """
    Format the chatbot response for better readability
    
    Args:
        response (str): Raw response text
        
    Returns:
        str: Formatted response
    """
    return response.strip()