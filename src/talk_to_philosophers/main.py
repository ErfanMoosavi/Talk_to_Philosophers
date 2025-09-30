from enum import Enum

from talk_to_philosophers.internals.system import System


class Commands(Enum):
    SIGNUP = "signup"
    LOGIN = "login"
    LOGOUT = "logout"
    NEW_CHAT = "new_chat"
    SELECT_CHAT = "select_chat"
    EXIT_CHAT = "exit_chat"
    EXIT = "exit"


def _handle_input(system):
    while True:
        command = input("Please enter the command: ")

        if command == Commands.SIGNUP.value:
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            status = system.signup(username, password)
            print(status.value)

        elif command == Commands.LOGIN.value:
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            status = system.login(username, password)
            print(status.value)

        elif command == Commands.LOGOUT.value:
            status = system.logout()
            print(status.value)

        elif command == Commands.NEW_CHAT.value:
            chat_name = input("Enter the chat name: ")
            philosopher = input("Enter philosopher name: ")
            status = system.new_chat(chat_name, philosopher)
            print(status.value)

        elif command == Commands.SELECT_CHAT.value:
            chat_name = input("Enter the chat name: ")
            system.select_chat(chat_name)
            while system.logged_in_user.selected_chat:
                message = input("Enter your message: ")
                if message == Commands.EXIT_CHAT.value:
                    system.exit_chat()
                system.send_message(message)
            print(status.value)

        elif command == Commands.EXIT.value:
            break

        else:
            print("Please enter a valid command.")


def main():
    system = System()

    _handle_input(system)


if __name__ == "__main__":
    main()
