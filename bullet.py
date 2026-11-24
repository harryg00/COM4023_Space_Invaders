import pygame
import barrier
import invader
import os

BULLET_COLOR = (255, 255, 0)
SPEED = 5
ASSETS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assests")


class Bullet:
    bullets = []
    defender = None
    DISPLAY_X = None

    def __init__(self, direction, centerx, y):
        Bullet.bullets.append(self)
        self.direction = direction
        self.rect = pygame.Rect(0, 0, 5, 5)
        self.rect.center = (centerx, y)

        pan = max(0.0, min(1.0, self.rect.centerx / Bullet.DISPLAY_X))
        left_volume = 1.0 - pan
        right_volume = pan
        pygame.mixer.Sound.play(
            pygame.mixer.Sound(ASSETS + "/sounds/shoot.wav")
        ).set_volume(left_volume * 0.1, right_volume * 0.1)

    @classmethod
    def updateAll(cls, screen):
        for bullet in cls.bullets:
            bullet.rect.y += SPEED * bullet.direction
            if bullet.rect.bottom > screen.get_height() or bullet.rect.top < 0:
                cls.bullets.remove(bullet)
                break

            for b in barrier.Barrier.barriers:
                if b.check_collision(bullet.rect):
                    cls.bullets.remove(bullet)
                    break

            if bullet.direction == -1:
                for i in invader.Invader.invaders:
                    if bullet.rect.colliderect(i.rect):
                        Bullet.bullets.remove(bullet)
                        invader.Invader.invaders.remove(i)
                        pygame.mixer.Sound.play(
                            pygame.mixer.Sound(ASSETS + "/sounds/invaderDeath.wav")
                        ).set_volume(0.5)
                        break
            else:
                if bullet.rect.colliderect(cls.defender.rect):
                    Bullet.bullets.remove(bullet)
                    break

            pygame.draw.rect(screen, BULLET_COLOR, bullet.rect)
