from openai import OpenAI

from .philosopher import Philosopher
from .utils.globals import BASE_URL, API_KEY, MODEL_NAME


class ChatCompleter:
    def __init__(self, philospher: Philosopher):
        self.client = OpenAI(base_url=BASE_URL, api_key=API_KEY)
        self.philosopher = philospher
