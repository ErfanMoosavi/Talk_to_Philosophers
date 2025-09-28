from openai import OpenAI

from ..globals import BASE_URL, API_KEY, MODEL_NAME


class ChatCompleter:
    def __init__(self):
        self.client = OpenAI(base_url=BASE_URL, api_key=API_KEY)

    def completion(self, prompt: str):
        completion = self.client.chat.completions.create(
            model=MODEL_NAME, messages=prompt
        )
        return completion.choices[0].message.content.strip()
