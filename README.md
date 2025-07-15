# AI-CHATBOT-WITH-NLP

*COMPANY*: CODTECH IT SOLUTIONS 

*NAME*: VARNIKA CHAUDHARY 

*INTERN ID*: :CT04DH361

*DOMAIN*: PYTHON PROGRAMMING 

*DURATION*: 4 WEEKS 

*MENTOR*: NEELA SANTOSH 

## Task 3 – AI Chatbot Using Natural Language Processing (NLP)

Task Objective:

For Task 3 of the CODTECH internship, I was assigned to build an AI chatbot using Natural Language Processing (NLP) libraries like NLTK or spaCy. The goal was to create a working Python script that can accept user input and respond like a chatbot using basic NLP techniques.


---

Project Summary:

Project Title: AI Chatbot with NLP

Language Used: Python 3

NLP Library: NLTK (Natural Language Toolkit)

Environment: PyCharm

Deliverables: Python Script (ai_chatbot.py) + Working Chatbot

Type: Terminal-based command-line chatbot



---

 Technologies and Tools Used:

Python – Programming Language

NLTK – For NLP functionality and chatbot module

Regex – For pattern matching user queries

PyCharm – IDE for development and execution

Command Line Interface – For chatbot interaction



---

 What the Chatbot Can Do:

The chatbot is designed to interact with users using pattern-matching techniques. It responds to common phrases and queries. Here's what it can handle:

Basic greetings like: hi, hello, hey

General questions like:

“What is your name?”

“How are you?”

“What can you do?”


Exit commands like: bye, exit, or quit

Unknown inputs: It replies with fallback messages like “Sorry, I didn’t understand that.”


The chatbot uses regular expressions and a simple decision-based conversation logic. It gives predefined answers to matched user inputs and keeps the interaction user-friendly.


---

 What I Did and How I Did It:

1. Started with Setup:
I first installed the nltk library in PyCharm using the terminal with the command pip install nltk.


2. Downloaded Required Data:
I created a temporary script file (nltksetup.py) just to download essential datasets like punkt, wordnet, and omw-1.4. Once this was complete, I deleted this setup file to keep the workspace clean.


3. Removed Unused Files:
I had created an extra file named task3.py during the initial stages. Once everything was finalized in ai_chatbot.py, I deleted that extra file to maintain a clean project directory.


4. Wrote the Final Code in ai_chatbot.py:
I structured the chatbot logic using nltk.chat.util.Chat, defined all the question-answer pairs using regular expressions, and ensured the script ran perfectly from start to finish.


5. Tested It:
I ran the chatbot in PyCharm's run terminal and tested different types of questions. The responses were appropriate and conversational, and it exited properly on command.




---

 Final Output:

When the script is run, the chatbot greets the user and waits for input. It interacts conversationally and responds to known questions. If an unknown input is given, it prompts the user to rephrase. The chatbot gracefully exits when the user types "bye", "exit", or "quit".

Example:

CODBot: Hi! I'm CODBot. Type 'bye' to exit.
> hi
CODBot: Hello! How can I help you?
> what is your name?
CODBot: I am a chatbot created by CODTECH!


---

 Learning and Experience:

This task was a fun and insightful introduction to NLP. I learned:

How NLP libraries like NLTK can be used to build a functional chatbot

How to tokenize, match, and process natural language using regex

How to handle Python package installations and environment setup

How to structure a clean Python project with functional code and readable logic

How to test chatbot conversations and debug patterns


This chatbot is rule-based and doesn’t involve machine learning, but it gave me the base knowledge needed for more advanced AI chatbots in the future using spaCy, transformers, or LLM APIs.


