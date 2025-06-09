import spacy

# Load English NLP model
nlp = spacy.load("en_core_web_sm")

# Define intents and responses
intents = {
    "greet": {
        "keywords": ["hello", "hi", "hey", "good morning"],
        "response": "Hello! How can I help you today?"
    },
    "goodbye": {
        "keywords": ["bye", "goodbye", "see you", "later"],
        "response": "Goodbye! Have a nice day!"
    },
    "name": {
        "keywords": ["your name", "who are you"],
        "response": "I am your friendly NLP chatbot, built using spaCy!"
    },
    "weather": {
        "keywords": ["weather", "temperature", "forecast"],
        "response": "I'm not connected to a weather API yet, but it looks sunny!"
    },
    "time": {
        "keywords": ["time", "clock"],
        "response": "Time is an illusion... Just kidding! I don't have a clock built in yet."
    }
}

def detect_intent(text):
    doc = nlp(text.lower())
    for intent, data in intents.items():
        if any(word in text.lower() for word in data["keywords"]):
            return intent
    return "unknown"

def extract_entities(text):
    doc = nlp(text)
    return [(ent.text, ent.label_) for ent in doc.ents]

def chatbot_reply(text):
    intent = detect_intent(text)
    entities = extract_entities(text)

    if intent in intents:
        response = intents[intent]["response"]
    else:
        response = "I'm not sure how to respond to that. Can you rephrase?"

    # Add entity feedback if any
    if entities:
        response += "\n[📌 I noticed these entities: " + ", ".join([f"{e[0]} ({e[1]})" for e in entities]) + "]"
    
    return response

# Run chatbot
print("🤖 spaCy Chatbot is online! (Type 'quit' to exit)")
while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("Bot: See you later! 👋")
        break
    print("Bot:", chatbot_reply(user_input))
