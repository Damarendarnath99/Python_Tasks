def get_reply(message):
    """Return a predefined reply based on the user's message."""
    message = message.lower().strip()

    if message in ("hello", "hi", "hey"):
        return "Hi!"
    elif message == "how are you":
        return "I'm fine, thanks!"
    elif message in ("what is your name", "your name", "who are you"):
        return "I'm a simple chatbot."
    elif message == "help":
        return "Try saying: hello, how are you, what is your name, or bye."
    elif message in ("bye", "goodbye", "exit"):
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that. Type 'help' to see what I can reply to."


def main():
    print("Chatbot: Hi! Type 'help' for options or 'bye' to quit.")

    while True:
        user_input = input("You: ")
        reply = get_reply(user_input)
        print("Chatbot:", reply)

        if reply == "Goodbye!":
            break


if __name__ == "__main__":
    main()
