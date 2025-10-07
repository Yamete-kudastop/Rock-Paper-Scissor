import random
from SRC.Choice.Choice import Choice

class Computer:
    def __init__(self):
        self.choice = None

    def make_choice(self):
        self.choice = random.choice(Choice.VALID_CHOICES)
        print(f"Computer chose: {self.choice}")
