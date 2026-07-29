import pygame
import random
from pathlib import Path


# Folder containing this Python file
game_folder = Path(__file__).parent


class Worm:
    def __init__(self, screen_width, screen_height):
        # Load the worm image
        image_path = game_folder / "Images" / "Worm.png"
        self.image = pygame.image.load(image_path).convert_alpha()

        # Resize the worm image
        self.image = pygame.transform.scale(self.image, (50, 50))

        # Store the worm's size
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        # Store the screen size
        self.screen_width = screen_width
        self.screen_height = screen_height

        # Give the worm its first random position
        self.respawn()

    def respawn(self):
        # Move the worm to a random position
        self.x = random.randint(
            0,
            self.screen_width - self.width
        )

        self.y = random.randint(
            0,
            self.screen_height - self.height
        )

    def get_rect(self):
        # Collision rectangle for the worm
        return self.image.get_rect(topleft=(self.x, self.y))

    def draw(self, screen):
        # Draw the worm image
        screen.blit(self.image, (self.x, self.y))