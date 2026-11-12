import pygame


class Barrier:
    barriers = []

    def __init__(self, index, max_barriers, width, hight):
        Barrier.barriers.append(self)
        self.rect = pygame.Rect(0, 0, 60, 20)
        self.rect.centerx = (index + 0.5) / max_barriers * width
        self.rect.centery = hight - hight / 5

    def update(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), self.rect)
