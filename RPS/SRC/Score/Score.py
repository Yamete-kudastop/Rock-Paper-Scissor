class ScoreBoard:
    def __init__(self):
        self.player = 0
        self.computer = 0
        self.ties = 0
        self.rounds = 0

    def add_result(self, result):
        self.rounds += 1
        if result == "win":
            self.player += 1
        elif result == "lose":
            self.computer += 1
        else:
            self.ties += 1

def show_score(score, final=False):
    label = "Final score" if final else "Actual score"
    print(f"{label} → Player {score.player} | Computer {score.computer} | Ties {score.ties} (Rounds: {score.rounds})")
