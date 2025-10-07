class Score:
    def __init__(self):
        self.player = 0
        self.computer = 0

    def update(self, winner):
        if winner == "player":
            self.player += 1
        elif winner == "computer":
            self.computer += 1

    def display(self):
        print(f"Score -> Player: {self.player} | Computer: {self.computer}")
