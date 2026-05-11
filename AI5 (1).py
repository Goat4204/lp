import nltk
from nltk.chat.util import Chat, reflections
import datetime

# Download required package
nltk.download('punkt')

# Chat patterns and responses
pairs = [

    [
        r"hi|hello|hey",
        ["Hello! Welcome to our online store.",
         "Hi there! How can I help you today?"]
    ],

    [
        r"what is your name ?",
        ["I am a Customer Support Chatbot."]
    ],

    [
        r"how are you ?",
        ["I am doing great! How can I assist you?"]
    ],

    [
        r"(.*)order(.*)track(.*)|track(.*)order(.*)",
        ["You can track your order from the 'My Orders' section."]
    ],

    [
        r"(.*)payment(.*)|(.*)payment methods(.*)",
        ["We accept Credit Card, Debit Card, UPI, and Net Banking."]
    ],

    [
        r"(.*)return(.*)product(.*)|refund",
        ["Go to 'My Orders' and click on 'Return Product'."]
    ],

    [
        r"(.*)delivery(.*)time(.*)",
        ["Delivery usually takes 3 to 5 business days."]
    ],

    [
        r"(.*)contact(.*)|customer care",
        ["You can contact customer care at +91-9876543210."]
    ],

    [
        r"(.*)offers(.*)|discounts",
        ["Today's offer: Get 20% off on orders above Rs. 2000."]
    ],

    [
        r"(.*)time(.*)|date",
        [f"Current date and time is: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"]
    ],

    [
        r"thank you|thanks",
        ["You're welcome!",
        "Happy to help!"]
    ],

    [
        r"bye|exit|quit",
        ["Thank you for visiting our store. Goodbye!"]
    ],

    [
        r"(.*)",
        ["Sorry, I did not understand that.",
        "Please ask another question."]
    ]
]

# Create chatbot object
chatbot = Chat(pairs, reflections)

# Start chatbot
print("===================================")
print("   Customer Support Chatbot")
print("===================================")
print("Type 'bye' to exit.\n")

# Start conversation
chatbot.converse()