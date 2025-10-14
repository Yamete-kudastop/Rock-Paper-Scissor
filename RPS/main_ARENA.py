import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 640, 480
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rock Paper Scissors - Arena")

BG_COLOR = (30, 30, 40)
TEXT_COLOR = (255, 255, 255)

FONT = pygame.font.SysFont("arial", 24)
BIG_FONT = pygame.font.SysFont("arial", 36, bold=True)

choices = ["rock", "paper", "scissors"]
images = {
    "rock": pygame.image.load("rock.png"),
    "paper": pygame.image.load("paper.png"),
    "scissors": pygame.image.load("scissors.png")
}

player_score = 0
computer_score = 0
ties = 0
round_count = 1
show_next_round = False
player_choice_img = None
computer_choice_img = None
result_text = ""

BUTTONS = []

class Button:
    def __init__(self, x, y, w, h, text, color=(50, 50, 70)):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.color = color

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)
        label = FONT.render(self.text, True, TEXT_COLOR)
        label_rect = label.get_rect(center=self.rect.center)
        win.blit(label, label_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

# Génération du fond dynamique
BG_PARTICLES = [(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(200)]
BG_VELOCITY = [(random.choice([-1,1])*0.2, random.choice([-1,1])*0.2) for _ in range(200)]

def draw_window():
    WIN.fill(BG_COLOR)

    # Fond dynamique
    for i, (x, y) in enumerate(BG_PARTICLES):
        pygame.draw.circle(WIN, (50, 50, 70), (int(x), int(y)), 2)
        # Déplacement
        vx, vy = BG_VELOCITY[i]
        x += vx
        y += vy
        if x < 0: x = WIDTH
        if x > WIDTH: x = 0
        if y < 0: y = HEIGHT
        if y > HEIGHT: y = 0
        BG_PARTICLES[i] = (x, y)

    round_label = BIG_FONT.render(f"Round {round_count}", True, TEXT_COLOR)
    WIN.blit(round_label, (WIDTH//2 - round_label.get_width()//2, 20))

    score_label = FONT.render(f"You: {player_score}  Computer: {computer_score}  Ties: {ties}", True, TEXT_COLOR)
    WIN.blit(score_label, (WIDTH//2 - score_label.get_width()//2, 70))

    if player_choice_img and computer_choice_img:
        vs_label = BIG_FONT.render("VS", True, TEXT_COLOR)
        WIN.blit(vs_label, (WIDTH//2 - vs_label.get_width()//2, HEIGHT//2 - vs_label.get_height()//2))
        WIN.blit(player_choice_img, (WIDTH//4 - player_choice_img.get_width()//2, HEIGHT//2 - player_choice_img.get_height()//2))
        WIN.blit(computer_choice_img, (3*WIDTH//4 - computer_choice_img.get_width()//2, HEIGHT//2 - computer_choice_img.get_height()//2))

    if result_text:
        result_label = BIG_FONT.render(result_text, True, TEXT_COLOR)
        WIN.blit(result_label, (WIDTH//2 - result_label.get_width()//2, HEIGHT - 120))

    for button in BUTTONS:
        button.draw(WIN)

    pygame.display.update()

def play_round(player_choice_str):
    global player_score, computer_score, ties, player_choice_img, computer_choice_img, result_text, show_next_round
    computer_choice_str = random.choice(choices)
    player_choice_img = pygame.transform.scale(images[player_choice_str], (100, 100))
    computer_choice_img = pygame.transform.scale(images[computer_choice_str], (100, 100))

    if player_choice_str == computer_choice_str:
        result_text = "DRAW!"
        ties += 1
    elif (player_choice_str == "rock" and computer_choice_str == "scissors") or \
         (player_choice_str == "paper" and computer_choice_str == "rock") or \
         (player_choice_str == "scissors" and computer_choice_str == "paper"):
        result_text = "YOU WIN!"
        player_score += 1
    else:
        result_text = "COMPUTER WINS!"
        computer_score += 1

    show_next_round = True

def next_round_func():
    global round_count, player_choice_img, computer_choice_img, result_text, show_next_round
    round_count += 1
    player_choice_img = None
    computer_choice_img = None
    result_text = ""
    show_next_round = False

def main():
    global BUTTONS
    clock = pygame.time.Clock()
    run = True

    BUTTONS = [
        Button(50, HEIGHT - 60, 120, 40, "Rock"),
        Button(200, HEIGHT - 60, 120, 40, "Paper"),
        Button(350, HEIGHT - 60, 120, 40, "Scissors"),
        Button(500, HEIGHT - 60, 120, 40, "Next Round")
    ]

    while run:
        clock.tick(60)
        draw_window()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                for i, button in enumerate(BUTTONS):
                    if button.is_clicked((mx, my)):
                        if i == 0 and not show_next_round:
                            play_round("rock")
                        elif i == 1 and not show_next_round:
                            play_round("paper")
                        elif i == 2 and not show_next_round:
                            play_round("scissors")
                        elif i == 3 and show_next_round:
                            next_round_func()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
