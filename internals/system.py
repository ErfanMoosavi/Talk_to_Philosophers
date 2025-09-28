from enum import Enum
from typing import Optional

from internals import ChatCompleter, PromptLoader, User, Chat


class Status(Enum):
    SUCCESS = "Success"
    PERMISSION_DENIED = "Permission Denied"
    BAD_REQUEST = "Bad Request"
    NOT_FOUND = "Not Found"


class System:
    def __init__(self):
        self.prompt_loader = PromptLoader()
        self.chat_completer = ChatCompleter()
        self.users: dict[str, User] = {}
        self.philosophers: list[str] = []
        self.logged_in_user: Optional[User] = None

    def signup(self, username: str, password: str) -> Status:
        if self.logged_in_user:
            return Status.PERMISSION_DENIED
        elif self._find_user(username):
            return Status.BAD_REQUEST
        self.users[username] = User(username, password)
        return Status.SUCCESS

    def login(self, username: str, password: str) -> Status:
        user = self._find_user(username)

        if self.logged_in_user:
            return Status.PERMISSION_DENIED
        elif not user:
            return Status.NOT_FOUND
        elif user.password != password:
            return Status.PERMISSION_DENIED
        self.logged_in_user = user
        return Status.SUCCESS

    def logout(self) -> Status:
        if not self.logged_in_user:
            return Status.PERMISSION_DENIED
        self.logged_in_user = None
        return Status.SUCCESS

    def new_chat(self, chat_name: str) -> Status:
        self.logged_in_user.new_chat(chat_name)
        return Status.SUCCESS

    def select_chat(self, chat_name: str) -> Status:
        self.logged_in_user.selected_chat = self._find_chat(chat_name)
        return Status.SUCCESS

    def exit_chat(self) -> Status:
        self.logged_in_user.selected_chat = None

    def send_message(self, philosopher_name: str, input: str) -> str:
        self.logged_in_user.selected_chat.add_message(f"{self.logged_in_user.username}")

        prompt = self.prompt_loader.load_prompts(input, philosopher_name)
        response = self.chat_completer.completion(prompt)

        self.logged_in_user.selected_chat.add_message(f"{philosopher_name}", response)
        return response

    def _find_user(self, username: str) -> Optional[User]:
        return self.users.get(username)

    def _find_chat(self, chat_name: str) -> Optional[Chat]:
        return self.logged_in_user.chat.get(chat_name)
