# Imports
import pygame
import random
import sys

#.py adds
from player import Player
from character_select import choose_character
from worm import Worm

# Initialize Pygame
pygame.init()

# Game Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors (RGB format)
WHITE = (255, 255, 255)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
BLUE = (50, 153, 213)

# Setup Game Window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Axoloto Adventure")
clock = pygame.time.Clock()

# Load Background
from pathlib import Path

game_folder = Path(__file__).parent
background = pygame.image.load(game_folder / "Images" / "Underground_Cave.jpg").convert()
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Character Selection
player_type = choose_character(screen)

# Create the player
player = Player(player_type)

worm = Worm(SCREEN_WIDTH, SCREEN_HEIGHT)
score = 0
score_font = pygame.font.Font(None, 40)

# Main Game Loop
running = True

while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check which keys are being held down
    keys = pygame.key.get_pressed()

    # Move the player
    player.move(keys)

    # Check if the player ate the worm
    if player.get_rect().colliderect(worm.get_rect()):
        score += 1
        worm.respawn()

    # Draw the background
    screen.blit(background, (0, 0))

    #Draw the Worm
    worm.draw(screen)

    # Draw the player
    player.draw(screen)

    # Draw the score
    score_text = score_font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (20, 20))

    # Update the screen
    pygame.display.flip()

    # Limit FPS
    clock.tick(FPS)

pygame.quit()
sys.exit()