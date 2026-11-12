import pygame
import os
ASSETS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assests")

class Defender:
    def __init__(self, dis_x, dis_y, speed, lives):
        pass
        self.lives = lives
        self.speed = speed
        img =  pygame.image.load(ASSETS + "/images/defender.png").convert_alpha()
        self.image = pygame.transform.scale(img, (100, 60))
        self.rect = self.image.get_rect()
        self.rect.center = (dis_x // 2 , dis_y - 10)
                
    def update(self, screen):
        self.move(screen)
        screen.blit(self.image, self.rect)

    def move(self, screen):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
        
            
        self.rect.clamp_ip(screen.get_rect())
    

    def shoot(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pass #call bullet class


