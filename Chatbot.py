import random

def start():
    responses = ["Greetings!","Nice to meet you!","Good Morning!","Hello!", "Hi there!", "Hey!"]
    return random.choice(responses)

def farewell():
    responses = ["Goodbye!", "See you later!", "Farewell!", "Bye!"]
    return random.choice(responses)

def chatbot_response(user_input):
    if user_input.lower() == "hello" or user_input.lower() == "hi" or user_input.lower() == "hey":
        return start()
    
    elif user_input.lower() == "what is your name" or user_input.lower() == "your name" :
        return "My name is Chatbot and I'm here to assist you."
    
    elif user_input.lower() == "how are you" :
        return "I'm doing well, thank you!"
    
    elif user_input.lower() == "sorry" :
        return "It's alright, no worries."
    
    elif user_input.lower() == "bye" or user_input.lower() == "goodbye" or user_input.lower() == "quit":
        return farewell()
    
    else:
        return "I'm just a simple chatbot. I don't understand that, but if I were you, I would go and Google it."

def chat():
    print("Welcome to the Chatbot!")
    print("You can start chatting, or type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print(chatbot_response(user_input))
            break
        else:
            print("Chatbot: ", chatbot_response(user_input))

chat()
