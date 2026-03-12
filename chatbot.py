def get_response(user_input):

    text = user_input.lower()


    # greetings
    if "hello" in text or "hi" in text:
        return "Hello! How can I help you?"

    elif "how are you" in text:
        return "I am fine. Ready to answer your questions."


    # knowledge questions

    elif "prime minister of india" in text:
        return "The Prime Minister of India is Narendra Modi."

    elif "president of india" in text:
        return "The President of India is Droupadi Murmu."

    elif "capital of india" in text:
        return "The capital of India is New Delhi."

    elif "2+2" in text:
        return "2 + 2 = 4"

    elif "your name" in text:
        return "I am your Python AI chatbot."

    elif "python" in text:
        return "Python is a programming language."

    elif "flask" in text:
        return "Flask is a Python web framework."

    elif "mongodb" in text:
        return "MongoDB is a NoSQL database."

    elif "node" in text:
        return "Node.js is used for backend development."


    # math example

    elif "square of" in text:
        try:
            num = int(text.split()[-1])
            return str(num * num)
        except:
            return "Cannot calculate."


    # default

    else:
        return "I don't know that yet."
