
import os
os.environ['TK_SILENCE_DEPRECATION'] = '1'  

import tkinter as tk
from tkinter import messagebox
import random


window = tk.Tk()
window.title("Rock Paper Scissors - Main Arena")
window.geometry("560x460")
window.config(bg="#0b0b0b")
window.resizable(False, False)

player_score = 0
computer_score = 0
ties = 0
round_count = 1
MAX_ROUNDS = None  


def get_winner(player, computer):
    """Retourne 'player', 'computer' ou 'draw'."""
    if player == computer:
        return "draw"
    if (player == "rock" and computer == "scissors") or \
       (player == "paper" and computer == "rock") or \
       (player == "scissors" and computer == "paper"):
        return "player"
    return "computer"

def show_popup(title, message):
    """Affiche une popup informative (non bloquante après update)."""
    window.update_idletasks()
    messagebox.showinfo(title, message)

def player_choice(choice):
    """Appelée quand le joueur choisit rock/paper/scissors."""
    global player_score, computer_score, ties

    computer = random.choice(["rock", "paper", "scissors"])

    player_label.config(text=f"YOU: {choice.upper()}")
    computer_label.config(text=f"COMPUTER: {computer.upper()}")
    window.update_idletasks()  

    winner = get_winner(choice, computer)

    if winner == "player":
        result_label.config(text=" YOU WIN! ", fg="#66ff66")
        player_score += 1
    elif winner == "computer":
        result_label.config(text=" COMPUTER WINS! ", fg="#ff6666")
        computer_score += 1
    else:
        result_label.config(text=" DRAW! ", fg="#ffd966")
        ties += 1

    score_label.config(
        text=f"Score: You {player_score} - {computer_score} Computer | Ties: {ties}"
    )

    set_choice_buttons_state("disabled")
    next_round_btn.config(state="normal")

    show_popup(
        "Round result",
        f"Ton choix : {choice.upper()}\nOrdinateur : {computer.upper()}\n\nRésultat : "
        + ("TU GAGNES " if winner=="player" else "ORDINATEUR GAGNE " if winner=="computer" else "ÉGALITÉ ")
    )

def next_round():
    """Prépare le round suivant."""
    global round_count
    round_count += 1
    if MAX_ROUNDS is not None and round_count > MAX_ROUNDS:
        end_game()
        return

    round_label.config(text=f"Round {round_count}")
    player_label.config(text="YOU: ?")
    computer_label.config(text="COMPUTER: ?")
    result_label.config(text="Choose your move!", fg="white")
    set_choice_buttons_state("normal")
    next_round_btn.config(state="disabled")

def reset_game():
    """Remet tout à zéro."""
    global player_score, computer_score, ties, round_count
    player_score = 0
    computer_score = 0
    ties = 0
    round_count = 1
    round_label.config(text=f"Round {round_count}")
    player_label.config(text="YOU: ?")
    computer_label.config(text="COMPUTER: ?")
    result_label.config(text="Choose your move!", fg="white")
    score_label.config(text=f"Score: You {player_score} - {computer_score} Computer | Ties: {ties}")
    set_choice_buttons_state("normal")
    next_round_btn.config(state="disabled")

def end_game():
    """Affiche le résultat final et propose de reset."""
    if player_score > computer_score:
        final_msg = f"Tu as gagné !\nFinal score : You {player_score} - {computer_score} Computer | Ties: {ties}"
    elif computer_score > player_score:
        final_msg = f"L'ordinateur a gagné.\nFinal score : You {player_score} - {computer_score} Computer | Ties: {ties}"
    else:
        final_msg = f"Match nul.\nFinal score : You {player_score} - {computer_score} Computer | Ties: {ties}"
    show_popup("Game Over", final_msg)
    set_choice_buttons_state("disabled")
    next_round_btn.config(state="disabled")

def set_choice_buttons_state(state):
    rock_btn.config(state=state)
    paper_btn.config(state=state)
    scissors_btn.config(state=state)


title_label = tk.Label(window, text="ROCK PAPER SCISSORS", font=("Helvetica", 20, "bold"),
                       fg="white", bg="#0b0b0b")
title_label.pack(pady=(12, 6))

round_label = tk.Label(window, text=f"Round {round_count}", font=("Helvetica", 14),
                       fg="#ffd700", bg="#0b0b0b")
round_label.pack()

choices_frame = tk.Frame(window, bg="#0b0b0b")
choices_frame.pack(pady=18)

player_label = tk.Label(choices_frame, text="YOU: ?", font=("Helvetica", 16, "bold"),
                        fg="#80ff80", bg="#0b0b0b")
player_label.grid(row=0, column=0, padx=24)

vs_label = tk.Label(choices_frame, text="VS", font=("Helvetica", 14), fg="white", bg="#0b0b0b")
vs_label.grid(row=0, column=1, padx=12)

computer_label = tk.Label(choices_frame, text="COMPUTER: ?", font=("Helvetica", 16, "bold"),
                          fg="#ff8080", bg="#0b0b0b")
computer_label.grid(row=0, column=2, padx=24)

result_label = tk.Label(window, text="Choose your move!", font=("Helvetica", 16, "bold"),
                        fg="white", bg="#0b0b0b")
result_label.pack(pady=12)

score_label = tk.Label(window, text=f"Score: You {player_score} - {computer_score} Computer | Ties: {ties}",
                       font=("Helvetica", 12), fg="#66ffff", bg="#0b0b0b")
score_label.pack()

buttons_frame = tk.Frame(window, bg="#0b0b0b")
buttons_frame.pack(pady=22)

rock_btn = tk.Button(buttons_frame, text="ROCK", font=("Helvetica", 13, "bold"),
                     width=10, height=2, bg="#2f2f2f", fg="white",
                     command=lambda: player_choice("rock"))
rock_btn.pack(side="left", padx=10)

paper_btn = tk.Button(buttons_frame, text="PAPER", font=("Helvetica", 13, "bold"),
                      width=10, height=2, bg="#2f2f2f", fg="white",
                      command=lambda: player_choice("paper"))
paper_btn.pack(side="left", padx=10)

scissors_btn = tk.Button(buttons_frame, text="SCISSORS", font=("Helvetica", 13, "bold"),
                         width=10, height=2, bg="#2f2f2f", fg="white",
                         command=lambda: player_choice("scissors"))
scissors_btn.pack(side="left", padx=10)

controls_frame = tk.Frame(window, bg="#0b0b0b")
controls_frame.pack(pady=12)

next_round_btn = tk.Button(controls_frame, text="NEXT ROUND", font=("Helvetica", 11, "bold"),
                           width=12, height=1, bg="#1e90ff", fg="white", state="disabled",
                           command=next_round)
next_round_btn.grid(row=0, column=0, padx=8)

reset_btn = tk.Button(controls_frame, text="RESET", font=("Helvetica", 11, "bold"),
                      width=10, height=1, bg="#ff8c00", fg="white", command=reset_game)
reset_btn.grid(row=0, column=1, padx=8)

quit_btn = tk.Button(controls_frame, text="QUIT", font=("Helvetica", 11),
                     width=10, height=1, bg="#b22222", fg="white", command=window.destroy)
quit_btn.grid(row=0, column=2, padx=8)


def on_keypress(event):
    key = event.keysym.lower()
    if key == "r":
        if rock_btn['state'] == "normal":
            player_choice("rock")
    elif key == "p":
        if paper_btn['state'] == "normal":
            player_choice("paper")
    elif key == "s":
        if scissors_btn['state'] == "normal":
            player_choice("scissors")
    elif key == "n":
        if next_round_btn['state'] == "normal":
            next_round()
    elif key == "t":  
        reset_game()

window.bind("<Key>", on_keypress)


if __name__ == "__main__":
    window.focus_force()
    window.mainloop()
