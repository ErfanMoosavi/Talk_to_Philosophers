from typing import Optional

from . import Chat, Status


class User:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        self.chats: list[dict[str, Chat]] = []
        self.selected_chat: Optional[Chat] = None

    def new_chat(self, chat_name: str) -> Status:
        new_chat = Chat(chat_name)
        self.chats.append(new_chat)
        self.selected_chat = new_chat
        return Status.SUCCESS

    def select_chat(self, chat_name: str) -> Status:
        chat = self._find_chat(chat_name)
        self.selected_chat = chat
        return Status.SUCCESS

    def exit_chat(self) -> Status:
        self.selected_chat = None
        return Status.SUCCESS

    def add_message(self, role: str, message: str) -> Status:
        self.selected_chat.add_message(role, message)
        return Status.SUCCESS

    def _find_chat(self, chat_name: str) -> Optional[Chat]:
        return self.chats.get(chat_name)
