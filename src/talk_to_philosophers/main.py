from enum import Enum

from talk_to_philosophers.internals.system import System
from talk_to_philosophers.internals.status import Status


class Commands(Enum):
    SIGNUP = "signup"
    LOGIN = "login"
    LOGOUT = "logout"
    NEW_CHAT = "new_chat"
    SELECT_CHAT = "select_chat"
    EXIT_CHAT = "exit_chat"
    EXIT = "exit"


def handle_chat_session(system: System, chat_name: str) -> str:
    status = system.select_chat(chat_name)
    if status != Status.SUCCESS:
        return status.value

    while system.logged_in_user.selected_chat:
        message = input("Enter your message (type 'exit_chat' to leave): ")
        if message == Commands.EXIT_CHAT.value:
            system.exit_chat()
            break
        system.send_message(message)

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

    elif command == Commands.NEW_CHAT.value:
        chat_name = input("Enter the chat name: ")
        philosopher = input("Enter philosopher name: ")
        return system.new_chat(chat_name, philosopher).value

    elif command == Commands.SELECT_CHAT.value:
        chat_name = input("Enter the chat name: ")
        return handle_chat_session(system, chat_name)

    elif command == Commands.EXIT.value:
        return "EXIT"

    return "Please enter a valid command."


def main():
    system = System()
    while True:
        command = input("Please enter the command: ")
        result = handle_command(command, system)

        if result == "EXIT":
            break
        print(result)


if __name__ == "__main__":
    main()
