def chatbot():
    print("Hello! I'm ChatBot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input == 'bye':
            print("ChatBot: Goodbye! Have a great day!")
            break
        elif 'hello' in user_input or 'hi' in user_input:
            print("ChatBot: Hello there!")
        elif 'how are you' in user_input:
            print("ChatBot: I'm just a program, but I'm doing fine. Thanks!")
        elif 'your name' in user_input:
            print("ChatBot: I'm just a simple chatbot.")
        elif 'help' in user_input:
            print("ChatBot: I can respond to greetings, tell you my name, and say goodbye.")
        else:
            print("ChatBot: I'm not sure how to respond to that.")

# Run the chatbot
chatbot()
