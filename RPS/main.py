from SRC.Score.Score import Score
from SRC.Round.Round import Round

def main():
    print("=== Welcome to Rock-Paper-Scissors ===")
    score = Score()

    while True:
        round_game = Round(score)
        round_game.play()

        again = input("Play again? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
