import pygame
import random
import os
from defender import Defender
from invader import Invader
from barrier import Barrier
from bullet import Bullet

BLOCK = 8
DISPLAY_X, DISPLAY_Y = 1000, 750
ASSETS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assests")
START_LIVES = 3

# pygame setup
pygame.init()
screen = pygame.display.set_mode((DISPLAY_X, DISPLAY_Y))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
big_font = pygame.font.Font(None, 80)

game_over_text = None
running = True

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
            if event.key == pygame.K_LEFT:
                Defender.move("left")
            if event.key == pygame.K_RIGHT:
                Defender.move("right")
            if event.key == pygame.K_SPACE:
                Defender.shoot()

    # draw background
    screen.blit(bg, (0, 0))

    if not game_over_text:
        Invader.update_all(screen)
        # Copy with list() because bullets remove themselves from Bullet.bullets while we loop
        for bullet in list(Bullet.bullets):
            bullet.update(screen)

        if Defender.lives <= 0 or any(
            i.rect.bottom >= Defender.rect.top for i in Invader.invaders
        ):
            game_over_text = "GAME OVER"
        elif not Invader.invaders:
            game_over_text = "YOU WIN!"

    Invader.draw_all(screen)
    Defender.update(screen)
    for barrier in Barrier.barriers:
        barrier.update(screen)
    draw_hud(screen)

    if game_over_text:
        draw_message(screen, game_over_text)

    pygame.display.flip()  # load display

    clock.tick(60)  # limits FPS to 60

pygame.quit()
