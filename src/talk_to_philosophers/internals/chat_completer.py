from openai import OpenAI

from talk_to_philosophers.utils.globals import BASE_URL, API_KEY, MODEL_NAME


class ChatCompleter:
    def __init__(self):
        self.client = OpenAI(base_url=BASE_URL, api_key=API_KEY)

    def complete_chat(self, messages: str) -> str:
        completion = self.client.chat.completions.create(
            model=MODEL_NAME, messages=messages
        )
        return completion.choices[0].message.content.strip()
