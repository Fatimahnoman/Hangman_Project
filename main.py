import pygame
import random
import sys
import asyncio

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 128, 0)

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game - Portfolio Version")

# Fonts
FONT = pygame.font.SysFont("arial", 40)
WORD_FONT = pygame.font.SysFont("arial", 60)
TITLE_FONT = pygame.font.SysFont("arial", 80)

# Game Data
WORDS = ["UMBRELLA", "COMPUTER", "SMARTPHONE", "TELESCOPE"]

def get_word():
    return random.choice(WORDS).upper()

def draw_hangman(chances):
    # Base
    pygame.draw.line(screen, BLACK, (100, 500), (300, 500), 5)
    pygame.draw.line(screen, BLACK, (200, 500), (200, 100), 5)
    pygame.draw.line(screen, BLACK, (200, 100), (400, 100), 5)
    pygame.draw.line(screen, BLACK, (400, 100), (400, 150), 5)

    # Character parts
    if chances <= 6: # Head
        pygame.draw.circle(screen, BLACK, (400, 190), 40, 5)
    if chances <= 5: # Body
        pygame.draw.line(screen, BLACK, (400, 230), (400, 350), 5)
    if chances <= 4: # Left Arm
        pygame.draw.line(screen, BLACK, (400, 250), (350, 300), 5)
    if chances <= 3: # Right Arm
        pygame.draw.line(screen, BLACK, (400, 250), (450, 300), 5)
    if chances <= 2: # Left Leg
        pygame.draw.line(screen, BLACK, (400, 350), (350, 450), 5)
    if chances <= 1: # Right Leg
        pygame.draw.line(screen, BLACK, (400, 350), (450, 450), 5)

async def main():
    word = get_word()
    guessed_letters = []
    chances = 7
    game_over = False
    won = False

    clock = pygame.time.Clock()

    while True:
        screen.fill(WHITE)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN and not game_over:
                letter = pygame.key.name(event.key).upper()
                if len(letter) == 1 and letter.isalpha():
                    if letter not in guessed_letters:
                        guessed_letters.append(letter)
                        if letter not in word:
                            chances -= 1
            
            if event.type == pygame.KEYDOWN and game_over:
                if event.key == pygame.K_r: # Restart
                    word = get_word()
                    guessed_letters = []
                    chances = 7
                    game_over = False
                    won = False

        # Logic
        display_word = ""
        for char in word:
            if char in guessed_letters:
                display_word += char + " "
            else:
                display_word += "_ "
        
        # Win/Loss check
        if "_" not in display_word and not game_over:
            won = True
            game_over = True
        
        if chances <= 0 and not game_over:
            game_over = True

        # Drawing
        draw_hangman(chances)

        # Render Word
        word_text = WORD_FONT.render(display_word.strip(), True, BLACK)
        screen.blit(word_text, (450, 250))

        # Render Chances
        chances_text = FONT.render(f"Chances: {chances}", True, RED if chances < 3 else BLACK)
        screen.blit(chances_text, (550, 50))

        if game_over:
            if won:
                msg = TITLE_FONT.render("YOU WON!", True, GREEN)
            else:
                msg = TITLE_FONT.render("GAME OVER!", True, RED)
                correct_word = FONT.render(f"Word was: {word}", True, BLACK)
                screen.blit(correct_word, (WIDTH//2 - correct_word.get_width()//2, 450))
            
            screen.blit(msg, (WIDTH//2 - msg.get_width()//2, 20))
            restart_text = FONT.render("Press 'R' to Restart", True, BLUE)
            screen.blit(restart_text, (WIDTH//2 - restart_text.get_width()//2, 520))

        pygame.display.update()
        
        # Crucial for web deployment: yield control back to the browser
        await asyncio.sleep(0)
        clock.tick(60)

if __name__ == "__main__":
    asyncio.run(main())
