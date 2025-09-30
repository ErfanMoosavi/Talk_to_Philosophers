from datetime import datetime


class MessageItem:
    def __init__(self, role: str, message: str):
        self.role = role
        self.message = message
        self.time = datetime.now().strftime("%H:%M")

    def to_chat_style(self) -> dict[str, str]:
        return {"role": self.role, "message": self.message, "time": self.time}


class HistoryItem:
    def __init__(self, role: str, content: str):
        self.role = role
        self.content = content

    def to_openai_style(self) -> dict[str, str]:
        return {"role": self.role, "content": self.content}
