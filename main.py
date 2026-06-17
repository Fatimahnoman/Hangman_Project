import pygame
import random
import sys
import asyncio

# Initialize Pygame
pygame.init()

# Constants & Colors
WIDTH, HEIGHT = 800, 600
WHITE = (248, 249, 250)
BLACK = (33, 37, 41)
RED = (220, 53, 69)
BLUE = (0, 123, 255)
GREEN = (40, 167, 69)
ORANGE = (253, 126, 20)
GRAY = (206, 212, 218)

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Modern Hangman - Portfolio Edition")

# Fonts (Using default as fallback, but bold for better UI)
def get_font(size):
    return pygame.font.SysFont("arial", size, bold=True)

TITLE_FONT = get_font(70)
WORD_FONT = get_font(50)
UI_FONT = get_font(30)
KEY_FONT = get_font(25)

# Game Data
WORDS = ["UMBRELLA", "COMPUTER", "SMARTPHONE", "TELESCOPE", "DEVELOPER", "PYTHON", "PROGRAMMING"]

def get_word():
    return random.choice(WORDS).upper()

def draw_hangman_modern(chances):
    # Base/Gallows with smoother colors
    pygame.draw.rect(screen, BLACK, (50, 500, 200, 10), border_radius=5) # Base
    pygame.draw.rect(screen, BLACK, (145, 100, 10, 400)) # Pole
    pygame.draw.rect(screen, BLACK, (145, 100, 200, 10)) # Top Bar
    pygame.draw.rect(screen, BLACK, (340, 100, 5, 50)) # Rope

    # Modern Character Parts
    color = BLACK
    if chances <= 6: # Head
        pygame.draw.circle(screen, color, (342, 190), 40, 5)
    if chances <= 5: # Body
        pygame.draw.line(screen, color, (342, 230), (342, 380), 5)
    if chances <= 4: # Left Arm
        pygame.draw.line(screen, color, (342, 260), (290, 320), 5)
    if chances <= 3: # Right Arm
        pygame.draw.line(screen, color, (342, 260), (394, 320), 5)
    if chances <= 2: # Left Leg
        pygame.draw.line(screen, color, (342, 380), (290, 460), 5)
    if chances <= 1: # Right Leg
        pygame.draw.line(screen, color, (342, 380), (394, 460), 5)

def draw_buttons(guessed_letters):
    # Virtual Keyboard for Mobile users
    buttons = []
    start_x, start_y = 50, 520
    gap = 10
    btn_size = 45
    
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i, l in enumerate(letters):
        x = start_x + (i % 13) * (btn_size + gap)
        y = start_y + (i // 13) * (btn_size + gap)
        
        rect = pygame.Rect(x, y, btn_size, btn_size)
        color = GRAY
        if l in guessed_letters:
            color = BLUE
            
        pygame.draw.rect(screen, color, rect, border_radius=5)
        text = KEY_FONT.render(l, True, WHITE if color != GRAY else BLACK)
        screen.blit(text, (x + (btn_size//2 - text.get_width()//2), y + (btn_size//2 - text.get_height()//2)))
        buttons.append((rect, l))
    return buttons

async def main():
    word = get_word()
    guessed_letters = []
    chances = 7
    game_over = False
    won = False

    clock = pygame.time.Clock()

    while True:
        screen.fill(WHITE)
        mouse_pos = pygame.mouse.get_pos()
        
        # Draw Keyboard
        kb_buttons = draw_buttons(guessed_letters)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            # Physical Keyboard
            if event.type == pygame.KEYDOWN and not game_over:
                letter = pygame.key.name(event.key).upper()
                if len(letter) == 1 and letter.isalpha():
                    if letter not in guessed_letters:
                        guessed_letters.append(letter)
                        if letter not in word:
                            chances -= 1
            
            # Virtual Keyboard / Mouse Click
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                for rect, l in kb_buttons:
                    if rect.collidepoint(mouse_pos):
                        if l not in guessed_letters:
                            guessed_letters.append(l)
                            if l not in word:
                                chances -= 1
            
            # Restart
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                if game_over:
                    # Check for click on Restart Button area or 'R' key
                    if (event.type == pygame.KEYDOWN and event.key == pygame.K_r) or event.type == pygame.MOUSEBUTTONDOWN:
                        word = get_word()
                        guessed_letters = []
                        chances = 7
                        game_over = False
                        won = False

        # Logic: Word Display
        display_word = ""
        for char in word:
            if char in guessed_letters:
                display_word += char + " "
            else:
                display_word += "_ "
        
        if "_" not in display_word and not game_over:
            won = True
            game_over = True
        if chances <= 0 and not game_over:
            game_over = True

        # Render Visuals
        draw_hangman_modern(chances)

        # Render Word with a nice underline effect
        word_text = WORD_FONT.render(display_word.strip(), True, BLACK)
        screen.blit(word_text, (400, 250))

        # Render Chances with an Icon-like feel
        pygame.draw.rect(screen, ORANGE, (600, 40, 160, 50), border_radius=10)
        chances_text = UI_FONT.render(f"Lives: {chances}", True, WHITE)
        screen.blit(chances_text, (620, 48))

        if game_over:
            # Semi-transparent overlay for Game Over
            overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            overlay.fill((255, 255, 255, 200))
            screen.blit(overlay, (0,0))

            if won:
                msg = TITLE_FONT.render("YOU WON!", True, GREEN)
            else:
                msg = TITLE_FONT.render("GAME OVER", True, RED)
                correct_word = UI_FONT.render(f"The word was: {word}", True, BLACK)
                screen.blit(correct_word, (WIDTH//2 - correct_word.get_width()//2, 350))
            
            screen.blit(msg, (WIDTH//2 - msg.get_width()//2, 200))
            restart_btn = pygame.draw.rect(screen, BLUE, (WIDTH//2-100, 450, 200, 60), border_radius=15)
            restart_text = UI_FONT.render("RESTART", True, WHITE)
            screen.blit(restart_text, (WIDTH//2 - restart_text.get_width()//2, 460))

        pygame.display.update()
        await asyncio.sleep(0)
        clock.tick(60)

if __name__ == "__main__":
    asyncio.run(main())
