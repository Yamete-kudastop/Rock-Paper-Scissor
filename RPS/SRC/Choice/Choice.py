class Choice:
    VALID_CHOICES = ["rock", "paper", "scissors"]

    @staticmethod
    def is_valid(choice):
        return choice.lower() in Choice.VALID_CHOICES
