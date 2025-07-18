def chatbot(user_input):

    user_input=user_input.lower()
    #predefined responses
    if(user_input=="hi"):
        return "Hello"
    elif(user_input=="how are you?" or user_input=="how are you"):
        return "I am fine"
    elif(user_input=="bye"):
        return "Goodbye!"
    else:
        return "Sorry I can't understand you"
def chatbot_run():
    print("Chatbot:Hello (say bye to exit)")
    while True:
        user_input=input("You: ")
        response=chatbot(user_input)
        print("Chatbot: ",response)

        if user_input.lower()=="bye":
            break
chatbot_run()

