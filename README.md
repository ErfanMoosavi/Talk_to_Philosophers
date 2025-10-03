# Philosopher Chat

Chat with your favorite philosophers—Nietzsche, Socrates, and more—in real-time!

## 📌 Overview

Philosopher Chat is an interactive command-line application that allows users to have AI-powered conversations with famous philosophers. Each philosopher responds in their distinctive style, language, and perspective. Users can create multiple chats, select philosophers, and maintain conversation histories.

---

## 🌟 Features

* **User Authentication:** Signup and login functionality to secure chats.
* **Multiple Chats:** Create multiple chat sessions with different philosophers.
* **AI-Powered Philosopher Responses:** Each philosopher responds intelligently using an AI completion engine.
* **Chat Management:** Delete or exit chats at any time.
* **Interactive CLI:** Easy-to-use command-line interface with clear prompts and messages.
* **Chat History:** Maintains conversation history per chat.
* **Persistent Data Handling:** Philosopher data is loaded from JSON, supporting future expansion.
* **Error Handling:** Validates inputs and provides user-friendly error messages.

---

## ⚙️ Commands

* `signup` - Create a new user account.
* `login` - Log in with an existing account.
* `logout` - Log out from the current account.
* `delete_account` - Delete your account.
* `new_chat` - Start a new chat with a philosopher.
* `select_chat` - Enter an existing chat session.
* `exit_chat` - Exit the current chat session.
* `delete_chat` - Delete a specific chat session.
* `list_chats` - Show all your existing chats and their philosophers.
* `list_philosophers` - Show all available philosophers.
* `help` - Show available commands.
* `exit` - Exit the application.

---

## 🚀 Installation

```bash
pip install philosopher-chat
```

---

## 🥩 Usage

1. Run the application:

```bash
python main.py
```

2. Set your API credentials (for AI completion) in a `.env` file:

```
BASE_URL=your_openai_base_url
OPENAI_API_KEY=your_api_key
MODEL_NAME=your_model_name
```

3. Follow the CLI prompts to sign up, log in, and start chatting.

   * Use `new_chat` to create a chat by selecting a philosopher from the numbered list.
   * Enter messages and receive responses in the philosopher's distinctive style.
   * Use `exit_chat` to leave a chat session safely.
   * Use `list_chats` and `select_chat` to manage multiple chat sessions.

---

## Contact

For questions or support, reach out to **Erfan** via your preferred contact method.
