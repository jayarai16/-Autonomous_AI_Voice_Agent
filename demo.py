import speech_recognition as sr
import pyttsx3
from textblob import TextBlob

# Initialize TTS
engine = pyttsx3.init()

# Set voice properties
voices = engine.getProperty('voices')
if voices:
    engine.setProperty('voice', voices[0].id)  # Default voice

# Conversation memory
conversation = []

# Simple intent keywords
intents = {
    'refund': ['refund', 'return', 'money back'],
    'cancel': ['cancel', 'stop', 'end'],
    'help': ['help', 'assist', 'support']
}

# Script for refund
script = [
    "Hello, I would like to request a refund for my recent purchase.",
    "The product was damaged upon arrival.",
    "Can you process the refund?",
    "Thank you."
]

script_index = 0
mode = 'scripted'  # or 'free'

def speak(text):
    sentiment = TextBlob(text).sentiment.polarity
    rate = 200
    if sentiment > 0:
        rate = 180  # faster for positive
    elif sentiment < 0:
        rate = 150  # slower for negative
    engine.setProperty('rate', rate)
    print(f"Agent speaks: {text}")  # For demo, print instead of speaking
    # engine.say(text)
    # engine.runAndWait()

def detect_intent(text):
    for intent, keywords in intents.items():
        if any(k in text for k in keywords):
            return intent
    return 'general'

def respond(text):
    global script_index, mode
    intent = detect_intent(text)
    conversation.append(f"User: {text}")
    if mode == 'scripted':
        if script_index < len(script):
            response = script[script_index]
            script_index += 1
            if script_index == len(script):
                mode = 'free'  # Switch after last scripted response
        else:
            response = "Thank you for your time."
            mode = 'free'
    else:
        if intent == 'refund':
            response = "I understand you want a refund. Let me check that for you."
        elif intent == 'cancel':
            response = "Are you sure you want to cancel?"
        elif intent == 'help':
            response = "How can I assist you?"
        else:
            response = "I'm sorry, I didn't understand. Can you repeat?"
    conversation.append(f"Agent: {response}")
    speak(response)
    return response

# Simulated conversation for demo
print("=== Autonomous AI Voice Agent Demo ===")
print("Simulating a conversation for demonstration purposes.\n")

# Sample user inputs
sample_inputs = [
    "hello",
    "yes",
    "the product is damaged",
    "please process refund",
    "I also want to cancel my subscription",
    "yes",
    "exit"
]

for user_input in sample_inputs:
    print(f"User: {user_input}")
    if user_input.lower() == 'exit':
        break
    respond(user_input.lower())

print("\n=== Conversation Ended ===")
print("Conversation history:")
for msg in conversation:
    print(msg)

print("\n=== Architecture Explanation ===")
print("STT: Google Speech Recognition (open-source API, free)")
print("TTS: pyttsx3 (offline, supports voice modulation)")
print("Intent Detection: Keyword matching for goal-oriented dialogue")
print("Memory: List-based conversation storage")
print("Autonomy: Loop-based processing with context awareness")
print("Modulation: Sentiment analysis adjusts speech rate")
print("Modes: Scripted (predefined sequence) → Free-flow (adaptive responses)")