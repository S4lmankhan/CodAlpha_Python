import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"(hi|hello|hey)",
        ["Hi there! How can I help you today?", "Greetings! What would you like to talk about?"]
    ],
    [
        r"good morning|good afternoon|good evening",
        ["Good [morning/afternoon/evening]! How can I be of service?"]
    ],
    [
        r"how's it going|what's up",
        ["I'm doing well, thanks for asking! How are you?"]
    ],

    [
        r"what is your name?",
        ["My name is Chatbot. I'm here to assist you."]
    ],
    [
        r"who are you",
        ["I'm Chatbot, a virtual assistant. How can I help you today?"]
    ],

    [
        r"how are you?",
        ["I'm doing well, thank you for asking. How can I assist you today?"]
    ],

    [
        r"(.*) help (.*)",
        ["Sure, I can help you with %2. What do you need assistance with?"]
    ],
    [
        r"what can you do|what are your capabilities",
        ["I can answer your questions, tell you jokes, and have simple conversations. How can I be of service?"]
    ],

    [
        r"quit|goodbye|see you later",
        ["Thank you for chatting with me. Have a great day!"]
    ],

    [
        r"what is the weather like",
        ["I don't have access to real-time weather data, but I hope it's a lovely day for you!"]
    ],
    [
        r"tell me a joke",  
        ["Why did the scarecrow win an award? Because he was outstanding in his field!"]
    ],
    [
        r"do you like (.*)",
        ["As a language model, I don't have personal preferences. However, I can tell you some interesting facts about (topic) if you'd like."]
    ],
    [
        r"(.*) thank you",
        ["You're welcome! Glad I could assist you."]
    ],
    [
        r"(.*)",  
        ["I'm sorry, I don't quite understand. Can you rephrase that?"]
    ],
]

def chatbot():
  print("Hello! I'm Afra The Chatbot. How can I assist you ?")
  chat = Chat(pairs, reflections)
  chat.converse()

if __name__ == "__main__":
  chatbot()
