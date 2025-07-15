# ai_chatbot.py

import nltk
from nltk.chat.util import Chat, reflections

# Define chatbot responses using pairs
pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I help you?", "Hi there! What can I do for you?"]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created by CODTECH!", "You can call me CODBot."]
    ],
    [
        r"how are you?",
        ["I'm doing well, thank you!", "Feeling helpful as always."]
    ],
    [
        r"what can you do?",
        ["I can answer your basic questions using NLP!", "I help with simple queries."]
    ],
    [
        r"(.) your internship (.)",
        ["The completion certificate will be issued at the end of your internship."]
    ],
    [
        r"(.*) (location|city) ?",
        ['I am in the cloud, everywhere!']
    ],
    [
        r"bye|exit|quit",
        ["Goodbye! Have a nice day.", "See you later!"]
    ],
    [
        r"(.*)",
        ["Sorry, I didn't understand that. Can you rephrase?", "Hmm, not sure about that."]
    ]
]

# Create chatbot
def codtech_chatbot():
    print("CODBot: Hi! I'm CODBot. Type 'bye' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

# Run the chatbot
if __name__ == "__main__":
    codtech_chatbot()
