"""
Configuration settings for Solvian Chatbot
"""

import os
from dotenv import load_dotenv

load_dotenv()

# API Configuration
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', '')
MODEL_NAME = os.getenv('MODEL_NAME', 'gpt-3.5-turbo')

# Chatbot Configuration
MAX_TOKENS = int(os.getenv('MAX_TOKENS', 150))
TEMPERATURE = float(os.getenv('TEMPERATURE', 0.7))
TOP_P = float(os.getenv('TOP_P', 0.9))

# Server Configuration
HOST = os.getenv('HOST', '127.0.0.1')
PORT = int(os.getenv('PORT', 5000))
DEBUG = os.getenv('DEBUG', 'True').lower() == 'true'

# Chatbot Personality
BOT_NAME = "Solvian"
BOT_DESCRIPTION = "An intelligent AI assistant ready to help you with any questions or tasks."