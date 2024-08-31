import nltk as n
from nltk.chat.util import Chat,reflections
pairs = [
    [
        r"My name is (.*)",
        ["Hello %1, how are you today?","Hi %1, how can I help you today?","Hello %1, I hope you are doing good\nWhy did you land here today",]
    ],
    [
        r"What is your name?",
        ["My name is Superbot and I am a chatbot",]
    ],
    [
        r"How are you?",
        ["I am doing good\nHow about you?",]
    ],
    [
        r"sorry (.*)",
        ["It's alright","Its ok, Nevermind","No problem at all",]
    ],
    [
        r"I am (.*) (good|well|ok|i nice|okay)",
        ["Nice to hear that","Alright","Alright, what do you want to know today?",]
    ],
    [
        r"(hi|hello|hola|holla|hii)(.*)",
        ["Hello","Hey there",]
    ],
    [
        r"What (.*) want?",
        ["Make me an offer I can't refuse","I can do anything, just ask",]
    ],
    [
        r"(.*) created?",
        ["I was created by Dev Pandey","I was created by programmers",]
    ],
    [
        r"I work in (.*)",
        ["%1 is an amazing company!",]
    ],
    [
        r"(.*) is raining  in (.*)",
        ["No rain in %2 for now",]
    ],
    [
        r"who (.*) (moviestar|actor|actress)",
        ["I love all moviestars equally",]
    ],
    [
        r"(.*)(sports|games|sport)(.*)",
        ["I preferably love playing cricket and football. I like watching cricket but I hate watching football. What about you?",
         "I love all the sports equally",
         "I like watching cricket and I am a fan of Rohit Sharma, Virat Kohli and many more players",
         "I love Rohit Sharma's Pull Shot and Virat's cover drive",
         "For me football is the best game as it builds your stamina",]
    ],
    [
        r"quit",
        ["Bye, take care. See you soon","It was nice talking to you, see you soon"]
    ]
]

def chatbot():
    print("Hi I am your chatbot. Type 'quit' to exit")
    chat=Chat(pairs,reflections)
    chat.converse()

if __name__=="__main__":
    chatbot()