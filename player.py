import pygame
from pathlib import Path

game_folder = Path(__file__).parent


class Player:
    def __init__(self, player_type):
        if player_type == 1:
            image_path = game_folder / "Images" / "golden_albino.png"
        else:
            image_path = game_folder / "Images" / "leuciastic.png"

        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))

        self.x = 350
        self.y = 400
        self.speed = 5

    def move(self, keys):
        if keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_d]:
            self.x += self.speed
        if keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_s]:
            self.y += self.speed

        #Boundaries
        if self.x < 0:
            self.x = 0
        if self.x > 700:
            self.x = 700
        if self.y < 0:
            self.y = 0
        if self.y > 500:
            self.y = 500

        # Keep player inside the game window
        self.x = max(0, min(self.x, 800 - self.image.get_width()))
        self.y = max(0, min(self.y, 600 - self.image.get_height()))

    def get_rect(self):
        return self.image.get_rect(topleft=(self.x, self.y))

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))