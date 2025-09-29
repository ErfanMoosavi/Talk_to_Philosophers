from enum import Enum

from talk_to_philosophers.internals.system import System


class Commands(Enum):
    SIGNUP = "signup"
    LOGIN = "login"
    LOGOUT = "logout"
    NEW_CHAT = "new_chat"
    SELECT_CHAT = "select_chat"
    EXIT_CHAT = "exit_chat"
    SEND_MESSAGE = "send_message"


def _handle_input(system):
    command = input("Please enter the command: ")

    if command == Commands.SIGNUP:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        status = system.signup(username, password)
        print(status)

    elif command == Commands.LOGIN:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        status = system.login(username, password)
        print(status)

    elif command == Commands.LOGOUT:
        status = system.logout()
        print(status)

    elif command == Commands.NEW_CHAT:
        chat_name = input("Enter the chat name: ")
        status = system.new_chat(chat_name)
        print(status)

    elif command == Commands.SEND_MESSAGE:
        message = input("Enter your message to {philosopher_name}: ")
        system.send_message(message)


def main():
    system = System()

    _handle_input(system)


if __name__ == "__main__":
    main()
