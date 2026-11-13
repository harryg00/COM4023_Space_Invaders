import pygame
import invader

BULLET_COLOR = (255, 255, 0)
SPEED = 5


class Bullet:
    bullets = []
    defender = None

    def __init__(self, direction, centerx, y):
        Bullet.bullets.append(self)
        self.direction = direction
        self.rect = pygame.Rect(0, 0, 5, 5)
        self.rect.center = (centerx, y)

    @classmethod
    def updateAll(cls, screen):
        for bullet in cls.bullets:
            bullet.rect.y += SPEED * bullet.direction
            if bullet.rect.bottom > screen.get_height() or bullet.rect.top < 0:
                cls.bullets.remove(bullet)
                break

            if bullet.direction == -1:
                for i in invader.Invader.invaders:
                    if bullet.rect.colliderect(i.rect):
                        Bullet.bullets.remove(bullet)
                        invader.Invader.invaders.remove(i)
                        break
            else:
                if bullet.rect.colliderect(cls.defender.rect):
                    Bullet.bullets.remove(bullet)
                    break

            pygame.draw.rect(screen, BULLET_COLOR, bullet.rect)
