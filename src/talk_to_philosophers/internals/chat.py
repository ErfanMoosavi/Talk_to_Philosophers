from talk_to_philosophers.internals.status import Status


class Chat:
    def __init__(self, chat_name: int, username: str, philosopher: str):
        self.chat_name = chat_name
        self.username = username
        self.philosopher = philosopher
        self.messages: list[dict[str, str]] = []

    def add_message(self, role: str, message: str) -> None:
        self.messages.append({"role": role, "message": message})
        self.show_new_message()

    def complete_chat(self, input_text: str, prompt_loader, chat_completer) -> Status:
        self.add_message(f"{self.username}", input_text)
        prompt = prompt_loader.load_prompts(input_text, self.philosopher)
        response = chat_completer.complete_chat(prompt)
        self.add_message(f"{self.philosopher}", response)
        return Status.SUCCESS

    def show_history(self) -> None:
        print(f"You are in {self.chat_name} chat:")
        for msg in self.messages:
            print(f"{msg['role']}: {msg['message']}")

    def show_new_message(self) -> None:
        msg = self.messages[-1]
        print(f"{msg['role']}: {msg['message']}")
