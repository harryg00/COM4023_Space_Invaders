# ---Imports--------------------------------------------------------------------
import pygame
import random
import os
from defender import Defender
from invader import Invader
import bullet
import barrier

# ---Defanitions---------------------------------------------------------------------
# changable
START_LIVES = 3
PLAYER_SPEED = 5
INVADER_SPEED = 1
INVADER_ROW_COUNT = 5
INVADER_COL_COUNT = 12
NUMBER_OF_BARRIERS = 5

# non changable
DISPLAY_X, DISPLAY_Y = 1000, 750
ASSETS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assests")

game_over_text = None
running = True

# ---pygame setup--------------------------------------------------------------------
pygame.init()
screen = pygame.display.set_mode((DISPLAY_X, DISPLAY_Y))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
big_font = pygame.font.Font(None, 80)

# ---Background-----------------------------------------------------------------
bg = pygame.image.load(ASSETS + "/images/space.png")
bg = pygame.transform.scale(bg, (DISPLAY_X, DISPLAY_Y))

# ---define objects-----------------------------------------------------------------
defender = Defender(DISPLAY_X, DISPLAY_Y, PLAYER_SPEED, START_LIVES)
bullet.Bullet.defender = defender
Invader.speed = INVADER_SPEED
Invader.DISPLAY_X = DISPLAY_X
Invader.DISPLAY_Y = DISPLAY_Y
for x in range(INVADER_ROW_COUNT):
    for y in range(INVADER_COL_COUNT):
        Invader(x, y, INVADER_ROW_COUNT, INVADER_COL_COUNT)
for b in range(NUMBER_OF_BARRIERS):
    barrier.Barrier(b, NUMBER_OF_BARRIERS, DISPLAY_X, DISPLAY_Y)

# ---Functions-------------------------------------------------------------------

# ---main loop--------------------------------------------------------------------
while running:
    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False

    # draw background
    screen.blit(bg, (0, 0))

    # update objects
    defender.update(screen)
    Invader.update_all(screen)
    bullet.Bullet.updateAll(screen)
    for b in barrier.Barrier.barriers:
        b.update(screen)

    # game over
    if game_over_text:
        pass

    pygame.display.flip()  # load display

    clock.tick(60)  # limits FPS to 60

pygame.quit()
