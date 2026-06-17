import pygame
import random
import sys
import asyncio

# Initialize Pygame
pygame.init()

# Constants & Colors (Matched to Reference Aesthetic)
WIDTH, HEIGHT = 800, 600
BG_COLOR = (28, 28, 57)  # Deep Dark Blue/Purple
TEXT_WHITE = (255, 255, 255)
ACCENT_COLOR = (0, 210, 255) # Cyan/Neon Blue
BUTTON_COLOR = (45, 45, 85) # Slightly lighter than BG
BUTTON_HOVER = (65, 65, 125)
RED_ACCENT = (255, 82, 82)
GREEN_ACCENT = (105, 240, 174)

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Neon Hangman - Modern UI")

# Fonts
def get_font(size):
    return pygame.font.SysFont("consolas", size, bold=True)

TITLE_FONT = get_font(80)
WORD_FONT = get_font(60)
UI_FONT = get_font(28)
KEY_FONT = get_font(22)

# Game Data
WORDS = ["UMBRELLA", "COMPUTER", "SMARTPHONE", "TELESCOPE", "DEVELOPER", "PYTHON", "PROGRAMMING"]

def get_word():
    return random.choice(WORDS).upper()

def draw_hangman_styled(chances):
    # Modern Styled Hangman (Neon White Lines)
    color = TEXT_WHITE
    thickness = 6
    
    # Gallows
    pygame.draw.line(screen, color, (80, 480), (220, 480), thickness) # Base
    pygame.draw.line(screen, color, (150, 480), (150, 120), thickness) # Pole
    pygame.draw.line(screen, color, (150, 120), (320, 120), thickness) # Top Bar
    pygame.draw.line(screen, color, (320, 120), (320, 160), thickness) # Rope

    # Character
    if chances <= 6: # Head
        pygame.draw.circle(screen, color, (320, 200), 40, thickness)
    if chances <= 5: # Body
        pygame.draw.line(screen, color, (320, 240), (320, 360), thickness)
    if chances <= 4: # Left Arm
        pygame.draw.line(screen, color, (320, 270), (270, 320), thickness)
    if chances <= 3: # Right Arm
        pygame.draw.line(screen, color, (320, 270), (370, 320), thickness)
    if chances <= 2: # Left Leg
        pygame.draw.line(screen, color, (320, 360), (270, 440), thickness)
    if chances <= 1: # Right Leg
        pygame.draw.line(screen, color, (320, 360), (370, 440), thickness)

def draw_keyboard(guessed_letters, mouse_pos):
    buttons = []
    start_x, start_y = 50, 480
    radius = 22
    gap = 12
    
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i, l in enumerate(letters):
        col = i % 13
        row = i // 13
        x = start_x + col * (radius * 2 + gap) + radius
        y = start_y + row * (radius * 2 + gap) + radius
        
        color = BUTTON_COLOR
        if l in guessed_letters:
            color = (80, 80, 120) # Deactivated color
        elif (x-mouse_pos[0])**2 + (y-mouse_pos[1])**2 < radius**2:
            color = BUTTON_HOVER
            
        pygame.draw.circle(screen, color, (x, y), radius)
        # Letter in white
        text_color = TEXT_WHITE if l not in guessed_letters else (150, 150, 180)
        text = KEY_FONT.render(l, True, text_color)
        screen.blit(text, (x - text.get_width()//2, y - text.get_height()//2))
        buttons.append(((x, y, radius), l))
    return buttons

async def main():
    word = get_word()
    guessed_letters = []
    chances = 7
    game_over = False
    won = False

    clock = pygame.time.Clock()

    while True:
        screen.fill(BG_COLOR)
        mouse_pos = pygame.mouse.get_pos()
        
        # Draw Background Decorative Elements
        pygame.draw.circle(screen, (35, 35, 75), (WIDTH, 0), 200)
        pygame.draw.circle(screen, (35, 35, 75), (0, HEIGHT), 150)

        # Event handling
        kb_buttons = draw_keyboard(guessed_letters, mouse_pos)
        
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
            
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                for (x, y, r), l in kb_buttons:
                    if (x-mouse_pos[0])**2 + (y-mouse_pos[1])**2 < r**2:
                        if l not in guessed_letters:
                            guessed_letters.append(l)
                            if l not in word:
                                chances -= 1
            
            if game_over and (event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN):
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_r) or event.type == pygame.MOUSEBUTTONDOWN:
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
        
        if "_" not in display_word and not game_over:
            won = True
            game_over = True
        if chances <= 0 and not game_over:
            game_over = True

        # Drawing
        draw_hangman_styled(chances)

        # Title
        title_text = TITLE_FONT.render("HANGMAN", True, ACCENT_COLOR)
        screen.blit(title_text, (WIDTH//2 - title_text.get_width()//2, 30))

        # Word Display
        word_render = WORD_FONT.render(display_word.strip(), True, TEXT_WHITE)
        screen.blit(word_render, (420, 220))

        # Lives Indicator
        lives_label = UI_FONT.render(f"LIVES: {chances}", True, RED_ACCENT if chances < 3 else GREEN_ACCENT)
        screen.blit(lives_label, (600, 130))

        if game_over:
            # Game Over Modal
            modal_rect = pygame.Rect(WIDTH//2-250, HEIGHT//2-150, 500, 300)
            pygame.draw.rect(screen, BUTTON_COLOR, modal_rect, border_radius=20)
            pygame.draw.rect(screen, ACCENT_COLOR, modal_rect, 3, border_radius=20)

            if won:
                result_text = TITLE_FONT.render("WINNER!", True, GREEN_ACCENT)
            else:
                result_text = TITLE_FONT.render("LOST!", True, RED_ACCENT)
                reveal_text = UI_FONT.render(f"WORD: {word}", True, TEXT_WHITE)
                screen.blit(reveal_text, (WIDTH//2 - reveal_text.get_width()//2, HEIGHT//2))
            
            screen.blit(result_text, (WIDTH//2 - result_text.get_width()//2, HEIGHT//2 - 100))
            
            restart_msg = UI_FONT.render("TAP TO RESTART", True, ACCENT_COLOR)
            screen.blit(restart_msg, (WIDTH//2 - restart_msg.get_width()//2, HEIGHT//2 + 80))

        pygame.display.update()
        await asyncio.sleep(0)
        clock.tick(60)

if __name__ == "__main__":
    asyncio.run(main())
