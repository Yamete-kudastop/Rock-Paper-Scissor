class Fight:
    @staticmethod
    def get_winner(player_choice, computer_choice):
        if player_choice == computer_choice:
            return "draw"
        elif (player_choice == "rock" and computer_choice == "scissors") \
            or (player_choice == "paper" and computer_choice == "rock") \
            or (player_choice == "scissors" and computer_choice == "paper"):
            return "player"
        else:
            return "computer"
