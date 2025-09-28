from enum import Enum
from typing import Optional

from talk_to_philosophers.internals import ChatCompleter, PromptLoader, User


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

    def chat(self, philosopher_name: str, input: str) -> str:
        prompt = self.prompt_loader.load_prompts(input, philosopher_name)
        response = self.chat_completer.completion(prompt)
        return response

    def _find_user(self, username: str) -> Optional[User]:
        return self.users.get(username)
