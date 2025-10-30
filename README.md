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

1. Set your API credentials (for AI completion) in a `.env` file:

```
BASE_URL=your_openai_base_url
OPENAI_API_KEY=your_api_key
MODEL_NAME=your_model_name
```

2. Run PhilosopherChat!

```python
from philosopher_chat import PhilosopherChat

# Load environment variables from .env
# You can also pass variables manually
load_dotenv()
BASE_URL = os.getenv("BASE_URL")
API_KEY = os.getenv("OPENAI_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME")

pc = PhilosopherChat(BASE_URL, API_KEY, MODEL_NAME)
pc.run()
```

3. Follow the CLI prompts to sign up, log in, and start chatting.

---

## 🤝 Contributing

Contributions are welcome!  
Feel free to **open issues, suggest new features, or submit pull requests**.  

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
