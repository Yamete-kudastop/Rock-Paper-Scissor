from SRC.Choice.Choice import get_player_choice
from SRC.Computer.Computer import get_computer_choice
from SRC.Fight.Fight import decide_winner
from SRC.Win.Win import say_win
from SRC.Lose.Lose import say_lose

def play_round():
    player = get_player_choice()
    computer = get_computer_choice()

    print(f"Player   : {player}")
    print(f"Computer : {computer}")

    result = decide_winner(player, computer)
    if result == "tie":
        print("Its a tie.")
    elif result == "win":
        say_win()
    else:
        say_lose()
    return result
