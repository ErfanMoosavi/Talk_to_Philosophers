from talk_to_philosophers.internals.status import Status


class Chat:
    def __init__(self, chat_name: int, philosopher: str):
        self.chat_name = chat_name
        self.philosopher = philosopher
        self.messages: list[dict[str, str]] = []
        self.chat_history: list[dict[str, str]] = []

    def complete_chat(
        self, input_text: str, username: str, prompt_loader, chat_completer
    ) -> Status:
        self._add_message(f"{username}", input_text)

        if self._is_first_message():
            prompt = prompt_loader.load_prompts(input_text, self.philosopher)
            self._add_chat_history("user", prompt)
        else:
            self._add_chat_history("user", input_text)

        response = chat_completer.complete_chat(self.chat_history)
        self._add_message(f"{self.philosopher}", response)
        self._add_chat_history("assistant", response)
        return Status.SUCCESS

    def show_messages_history(self) -> None:
        print(f"You are in '{self.chat_name}' chat:")
        for msg in self.messages:
            print(f"{msg['role']}: {msg['message']}")

    def _show_new_message(self) -> None:
        msg = self.messages[-1]
        print(f"{msg['role']}: {msg['message']}")

    def _add_message(self, role: str, message: str) -> None:
        self.messages.append({"role": role, "message": message})
        self._show_new_message()

    def _add_chat_history(self, role: str, message: str) -> None:
        self.chat_history.append({"role": role, "content": message})

    def _is_first_message(self) -> bool:
        return bool(not self.chat_history)
