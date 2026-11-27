import pygame
import math
import barrier
import invader
import os

BULLET_COLOR = (255, 255, 0)
SPEED = 5
ASSETS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assests")
SHOOT_VOLUME = 0.30

SHOOT_SOUND = pygame.mixer.Sound(ASSETS + "/sounds/shoot.wav")
INVADER_DEATH_SOUND = pygame.mixer.Sound(ASSETS + "/sounds/invaderDeath.wav")
INVADER_DEATH_SOUND.set_volume(0.40)
PLAYER_DEATH_SOUND = pygame.mixer.Sound(ASSETS + "/sounds/playerDeath.wav")
PLAYER_DEATH_SOUND.set_volume(0.50)


class Bullet:
    bullets = []
    defender = None
    DISPLAY_X = None

    @classmethod
    def has_defender_bullet(cls):
        return any(bullet.direction == -1 for bullet in cls.bullets)

    def __init__(self, direction, centerx, y):
        Bullet.bullets.append(self)
        self.direction = direction
        self.rect = pygame.Rect(0, 0, 5, 5)
        self.rect.center = (centerx, y)

        self.play_shoot_sound()

    def play_shoot_sound(self):
        pan = max(0.0, min(1.0, self.rect.centerx / Bullet.DISPLAY_X))
        left_volume = math.cos(pan * math.pi / 2)
        right_volume = math.sin(pan * math.pi / 2)

        channel = SHOOT_SOUND.play()
        if channel is not None:
            channel.set_volume(left_volume * SHOOT_VOLUME, right_volume * SHOOT_VOLUME)

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
                        INVADER_DEATH_SOUND.play()
                        break
            else:
                if bullet.rect.colliderect(cls.defender.rect):
                    Bullet.bullets.remove(bullet)
                    PLAYER_DEATH_SOUND.play()
                    break

            pygame.draw.rect(screen, BULLET_COLOR, bullet.rect)
