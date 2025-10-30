import os

from dotenv import load_dotenv

from philosopher_chat import PhilosopherChat

# Load environment variables from .env
load_dotenv()
BASE_URL = os.getenv("BASE_URL")
API_KEY = os.getenv("OPENAI_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME")

pc = PhilosopherChat(BASE_URL, API_KEY, MODEL_NAME)
pc.run()
