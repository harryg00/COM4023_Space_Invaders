
import os
os.environ['SDL_VIDEODRIVER'] = 'x11'
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Keep Open Test")

# Force an update and wait 5 seconds
pygame.display.flip()
pygame.quit()