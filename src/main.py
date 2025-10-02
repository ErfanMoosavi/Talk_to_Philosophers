from enum import Enum
import os
import json

from internals.system import System
from internals.status import Status


class Commands(Enum):
    SIGNUP = "signup"
    LOGIN = "login"
    LOGOUT = "logout"
    DELETE_ACCOUNT = "delete_account"
    NEW_CHAT = "new_chat"
    SELECT_CHAT = "select_chat"
    LIST_CHATS = "list_chats"
    EXIT_CHAT = "exit_chat"
    DELETE_CHAT = "delete_chat"
    HELP = "help"
    EXIT = "exit"


def load_philosophers():
    path = os.path.join(os.path.dirname(__file__), "..", "data", "philosophers.json")
    path = os.path.abspath(path)
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def msg_to_str(msg) -> str:
    print("-" * 50)
    return f"[{msg.time}] {msg.author} →\n{msg.content}"


def handle_chat_session(system: System, chat_name: str) -> str:
    status, all_messages = system.select_chat(chat_name)
    if status != Status.SUCCESS:
        return status.value

    for msg in all_messages:
        print(msg_to_str(msg))

    while system.logged_in_user.selected_chat:
        input_text = input("Enter your message (type 'exit_chat' to leave): ")
        if input_text == Commands.EXIT_CHAT.value:
            system.exit_chat()
            break
        status, ai_msg, user_msg = system.complete_chat(input_text)
        print(msg_to_str(user_msg))
        print(msg_to_str(ai_msg))

    return "Exited chat."


def handle_command(command: str, system: System) -> str:
    if command == Commands.SIGNUP.value:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        return system.signup(username, password).value

    elif command == Commands.LOGIN.value:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        return system.login(username, password).value

    elif command == Commands.LOGOUT.value:
        return system.logout().value

    elif command == Commands.DELETE_ACCOUNT.value:
        return system.delete_account().value

    elif command == Commands.NEW_CHAT.value:
        chat_name = input("Enter the chat name: ")

        philosophers = load_philosophers()
        for i, p in enumerate(philosophers, start=1):
            print(f"{i}. {p['name']}")

        choice = int(input("Choose a philosopher by number: ")) - 1
        if choice < 0 or choice >= len(philosophers):
            return "Invalid choice."

        philosopher_name = philosophers[choice]["name"]
        return system.new_chat(chat_name, philosopher_name).value

    elif command == Commands.SELECT_CHAT.value:
        chat_name = input("Enter the chat name: ")
        return handle_chat_session(system, chat_name)

    elif command == Commands.LIST_CHATS.value:
        status, chats = system.list_chats()
        for chat in chats:
            print(f"{chat.chat_name}\tPhilosopher-> {chat.philosopher}")

    elif command == Commands.DELETE_CHAT.value:
        chat_name = input("Enter the chat name: ")
        return system.delete_chat(chat_name).value

    elif command == Commands.HELP.value:
        return "HELP"

    elif command == Commands.EXIT.value:
        return "EXIT"

    return "Please enter a valid command."


def main():
    system = System()

    help_menu = "Available commands:"
    for command in Commands:
        help_menu += "\n\t-" + command.value

    print("Welcome to Philosopher Chat!")
    print(help_menu)

    while True:
        command = input("Please enter the command: ")
        result = handle_command(command, system)

        if result == "EXIT":
            break
        elif result == "HELP":
            print(help_menu)
        else:
            print(result)


if __name__ == "__main__":
    main()
