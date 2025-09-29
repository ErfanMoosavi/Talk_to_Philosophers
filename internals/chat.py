class Chat:
    def __init__(self, chat_name: int):
        self.chat_name = chat_name
        self.messages = list[dict[str, str]] = []

    def add_message(self, role: str, message: str) -> None:
        self.messages.append({"role": role, "message": message})

    def show_history(self) -> None:
        print({self.chat_name})
        for msg in self.messages:
            print(f"{msg['role']}: {msg['message']}")

    def show_new_message(self) -> None:
        msg = self.messages[-1]
        print(f"{msg['role']}: {msg['message']}")
