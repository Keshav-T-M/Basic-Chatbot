import nltk
import random
from nltk.chat.util import Chat, reflections

# Download NLTK resources if you haven't already
try:
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('wordnet')
try:
    nltk.data.find('corpora/omw-1.4')
except LookupError:
    nltk.download('omw-1.4')

# Define patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"what is your name ?",
        ["My name is Jarvis.",]
    ],
        [
        r"who created you ?",
        ["I was created by Keshav T M.",]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you!", "I'm fine, how about you?",]
    ],
    [
        r"sorry (.*)",
        ["It's alright","No problem",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that","Alright :)",]
    ]
]
