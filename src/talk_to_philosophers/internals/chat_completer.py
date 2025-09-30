from openai import OpenAI

from talk_to_philosophers.utils.globals import BASE_URL, API_KEY, MODEL_NAME


class ChatCompleter:
    def __init__(self):
        self.client = OpenAI(base_url=BASE_URL, api_key=API_KEY)

    def _build_user_message(self, prompt: str) -> list[dict[str, str]]:
        return [{"role": "user", "content": prompt}]

    def complete_chat(self, prompt: str) -> str:
        message = self._build_user_message(prompt)
        completion = self.client.chat.completions.create(
            model=MODEL_NAME, messages=message
        )
        return completion.choices[0].message.content.strip()
