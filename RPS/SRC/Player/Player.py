from SRC.Choice.Choice import Choice

class Player:
    def __init__(self):
        self.choice = None

    def make_choice(self):
        while True:
            choice = input("Choose rock, paper or scissors: ").lower()
            if Choice.is_valid(choice):
                self.choice = choice
                break
            else:
                print("Invalid choice, please try again.")
