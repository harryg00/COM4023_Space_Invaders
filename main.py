import pygame
import random
import os
from defender import Defender
from invaders import Invaders
from barriers import Barriers

DISPLAY_X, DISPLAY_Y = 1000, 750

# pygame setup
pygame.init()
screen = pygame.display.set_mode((DISPLAY_X, DISPLAY_Y))
clock = pygame.time.Clock()
running = True

# Assets path
ASSETS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assests")

# Background
bg = pygame.image.load(ASSETS + "/images/space.png")
bg = pygame.transform.scale(bg, (DISPLAY_X, DISPLAY_Y))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.type.key == pygame.K_Q:
                running = False

    # draw background
    screen.blit(bg, (0, 0))

    # draw things
    Defender.update(screen)
    Invaders.update(screen)
    Barriers.update(screen)

    pygame.display.flip()  # load display

    clock.tick(60)  # limits FPS to 60

pygame.quit()
