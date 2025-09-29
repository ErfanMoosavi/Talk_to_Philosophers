from typing import Optional

from internals import ChatCompleter, PromptLoader, User, Status


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
        return self.logged_in_user.new_chat(chat_name)

    def select_chat(self, chat_name: str) -> Status:
        return self.logged_in_user.select_chat(chat_name)

    def exit_chat(self) -> Status:
        return self.logged_in_user.exit_chat

    def send_message(self, philosopher_name: str, input_text: str) -> Status:
        prompt = self.prompt_loader.load_prompts(input_text, philosopher_name)
        response = self.chat_completer.completion(prompt)
        self.logged_in_user.add_message(f"{self.logged_in_user.username}", input_text)
        self.logged_in_user.add_message(f"{philosopher_name}", response)
        return Status.SUCCESS

    def _find_user(self, username: str) -> Optional[User]:
        return self.users.get(username)
