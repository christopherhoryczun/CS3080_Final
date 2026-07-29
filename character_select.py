import pygame
import sys

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def choose_character(screen):
    font = pygame.font.Font(None, 40)

    while True:
        screen.fill(BLACK)

        title = font.render("Choose Your Axolotl", True, WHITE)
        option1 = font.render("Press 1 - Golden Axolotl", True, WHITE)
        option2 = font.render("Press 2 - Pink Axolotl", True, WHITE)

        screen.blit(title, (220, 120))
        screen.blit(option1, (220, 240))
        screen.blit(option2, (220, 300))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return 1
                elif event.key == pygame.K_2:
                    return 2