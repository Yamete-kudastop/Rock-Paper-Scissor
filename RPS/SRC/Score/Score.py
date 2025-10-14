class Score:
    def __init__(self):
        self.player = 0
        self.computer = 0
        self.ties = 0

    def update(self, winner):
        if winner == "player":
            self.player += 1
        elif winner == "computer":
            self.computer += 1
        elif winner == "draw":
            self.ties += 1

    def display(self):
        print(f"Score -> Player: {self.player} | Computer: {self.computer} | Ties: {self.ties}")