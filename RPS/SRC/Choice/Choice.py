OPTIONS = ("rock", "paper", "scissors")

def get_player_choice():
    while True:
        choice = input("Your choice (rock, paper, scissors) : ").strip().lower()
        if choice in OPTIONS:
            return choice
        print(" Invalid choice. Please choose rock, paper, or scissors.")
