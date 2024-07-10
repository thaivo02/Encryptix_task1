import random
import re


class Bot:
    negative_res = ("no", "nope", "nah", "not a chance")
    exit_commands = ("quit", "exit", "goodbye", "bye", "later")

    random_question = (
        "How are you? \n",
        "What is your job? \n",
        "How is the weather today? \n",
        "How many friends do you have? \n",
        "Why are you here? \n",
    )

    def __init__(self):
        self.response = {
            "describe_self_intent": r".*\s*your self.*",
            "answer_why_intent": r"^why.*",
            "hobby_intent": r".*\s*(hobby|like).*",
        }

    def greet(self):
        self.name = input("What's your name ?\n")
        will_help = input(
            f"Hi {self.name}, I am chatbot, would you like to have a conversation with me?\n"
        )
        if will_help in self.negative_res:
            print("See you!")
            return
        self.chat()

    def make_exit(self, reply):
        for command in self.exit_commands:
            if reply == command:
                print("Have a nice day.")
                return True

    def chat(self):
        reply = input(random.choice(self.random_question)).lower()
        while not self.make_exit(reply):
            reply = input(self.match_reply(reply))

    def match_reply(self, reply):
        for intent, regex_pattern in self.response.items():
            found_match = re.match(regex_pattern, reply)
            if found_match and intent == "describe_self_intent":
                return self.describe_self_intent()
            elif found_match and intent == "answer_why_intent":
                return self.answer_why_intent()
            elif found_match and intent == "hobby_intent":
                return self.hobby_intent()
        if not found_match:
            return self.no_match_intent()

    def describe_self_intent(self):
        responses = (
            "I am a rule-based chat bot. I am scripted to have a little conversation with you.\n",
            "I like cofee. \n",
            "I am a chatbot created by a human. \n",
        )
        return random.choice(responses)

    def answer_why_intent(self):
        responses = (
            "I come in peace. \n",
            "I am here to collect your data. \n",
            "I want to have a chat with you. \n",
        )
        return random.choice(responses)

    def hobby_intent(self):
        responses = (
            "I like to chat with you. \n",
            "I like to collect data. \n",
            "I like to read books. \n",
            "I like to watch movies. \n",
        )
        return random.choice(responses)

    def no_match_intent(self):
        responses = (
            "Please tell me more. \n",
            "Hmmm... \n",
            "I see. \n",
            "Interesting. Can you tell me more?\n",
            "How do you think? \n",
            "Why? \n",
            "How do you think I feel when i say that. Why? \n",
        )
        return random.choice(responses)


bot = Bot()
bot.greet()
