from SRC.Round.Round import play_round
from SRC.Score.Score import ScoreBoard, show_score

def ask_best_of():
    while True:
        raw = input("Round ? (Odd number, ex: 3 ou 5) : ").strip()
        if raw.isdigit():
            n = int(raw)
            if n > 0 and n % 2 == 1:
                return n
        print("Odd number (3, 5, 7, ...).")

def ask_yes_no(prompt="Play again? (y/n): "):
    while True:
        ans = input(prompt).strip().lower()
        if ans in ("y", "n"):
            return ans
        print("Please type only 'y' or 'n'.")

def main():
    print("=== Rock / Paper / Scissors ===")
    while True:
        best_of = ask_best_of()
        rounds_to_win = (best_of // 2) + 1
        score = ScoreBoard()
        current_round = 1

        while score.player < rounds_to_win and score.computer < rounds_to_win:
            print(f"\n--- Round {current_round}/{best_of} ---")
            result = play_round()
            score.add_result(result)
            show_score(score)
            current_round += 1

        print("\n=== Final Result ===")
        show_score(score, final=True)
        if score.player > score.computer:
            print("You win!")
        elif score.player < score.computer:
            print("You lose, go next")
        else:
            print("Its a tie!")

        if ask_yes_no("Play again? (y/n): ") == "n":
            break

if __name__ == "__main__":
    main()
