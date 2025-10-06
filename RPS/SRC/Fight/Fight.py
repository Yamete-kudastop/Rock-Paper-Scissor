
def decide_winner(player, computer):
    if player == computer:
        return "tie"
    if player == "rock" and computer == "scissors":
        return "win"
    if player == "paper" and computer == "rock":
        return "win"
    if player == "scissors" and computer == "paper":
        return "win"
    return "lose"
