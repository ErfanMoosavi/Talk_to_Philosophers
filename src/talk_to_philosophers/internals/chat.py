from talk_to_philosophers.internals.status import Status
from talk_to_philosophers.internals.chat_items import MessageItem, HistoryItem


class Chat:
    def __init__(self, chat_name: str, philosopher: str):
        self.chat_name = chat_name
        self.philosopher = philosopher
        self.messages: list[MessageItem] = []
        self.chat_history: list[HistoryItem] = []

    def complete_chat(
        self, input_text: str, username: str, prompt_loader, chat_completer
    ) -> Status:
        self._add_message(f"{username}", input_text)

        if self._is_first_message():
            prompt = prompt_loader.load_prompts(input_text, self.philosopher)
            self._add_chat_history("user", prompt)
        else:
            self._add_chat_history("user", input_text)

        response = chat_completer.complete_chat(
            [h.to_openai_style() for h in self.chat_history]
        )
        self._add_message(f"{self.philosopher}", response)
        self._add_chat_history("assistant", response)
        return Status.SUCCESS

    def show_all_messages(self) -> None:
        print(f"You are in '{self.chat_name}' chat:")
        for message in self.messages:
            self._show_message(message)

    def _show_message(self, message: MessageItem) -> None:
        print(f"{message.role}: {message.message}\n{message.time}")

    def _add_message(self, role: str, message: str) -> None:
        new_message = MessageItem(role, message)
        self.messages.append(new_message)
        self._show_message(new_message)

    def _add_chat_history(self, role: str, content: str) -> None:
        self.chat_history.append(HistoryItem(role, content))

    def _is_first_message(self) -> bool:
        return bool(not self.chat_history)
