from typing import Optional

from . import Chat


class User:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        self.chats: list[dict[str, Chat]] = []
        self.selected_chat: Optional[Chat] = None

    def new_chat(self, chat_name: str):
        new_chat = Chat(chat_name)
        self.chats.append(new_chat)
        self.selected_chat = new_chat
