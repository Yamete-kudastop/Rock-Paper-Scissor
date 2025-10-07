from SRC.Player.Player import Player
from SRC.Computer.Computer import Computer
from SRC.Fight.Fight import Fight

class Round:
    def __init__(self, score):
        self.player = Player()
        self.computer = Computer()
        self.score = score

    def play(self):
        self.player.make_choice()
        self.computer.make_choice()
        winner = Fight.get_winner(self.player.choice, self.computer.choice)

        if winner == "draw":
            print("It's a draw!")
        elif winner == "player":
            print("You win this round!")
        else:
            print("Computer wins this round!")

        self.score.update(winner)
        self.score.display()
