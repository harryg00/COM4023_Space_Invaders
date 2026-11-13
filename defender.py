import pygame
import os
from bullet import Bullet

ASSETS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assests")


class Defender:
    def __init__(self, dis_x, dis_y, speed, lives):
        pass
        self.lives = lives
        self.speed = speed
        img = pygame.image.load(ASSETS + "/images/defender.png").convert_alpha()
        self.image = pygame.transform.scale(img, (100, 60))
        self.rect = self.image.get_rect()
        self.rect.center = (dis_x // 2, dis_y - 10)

    def update(self, screen):
        self.move(screen)
        self.shoot()
        screen.blit(self.image, self.rect)

    def move(self, screen):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed

        self.rect.clamp_ip(screen.get_rect())

    def shoot(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            Bullet(-1, self.rect.centerx, self.rect.top)
