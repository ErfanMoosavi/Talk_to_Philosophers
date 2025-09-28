class Chat:
    def __init__(self, chat_name: int):
        self.chat_name = chat_name
        self.messages = list[dict[str, str]]

    def add_message(self, role: str, message: str):
        self.messages.append({"role": role, "message": message})
