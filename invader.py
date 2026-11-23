import random
import bullet
import pygame

INVADER_BITMAPS = [
    [
        "00000001111110000000",
        "00000111111111100000",
        "00000111111111100000",
        "00111111111111111100",
        "11111111111111111111",
        "11111001111110011111",
        "11111111111111111111",
        "11111111111111111111",
        "00000111000011100000",
        "00111001111110011100",
        "11111111111111111111",
        "11100111000011100111",
    ],
    [
        "00011100000000111000",
        "00001110000001110000",
        "00000110000001100000",
        "00011111111111111000",
        "00111111111111111100",
        "00111101111110111100",
        "11111111111111111111",
        "11111111111111111111",
        "11011111111111111011",
        "11011100000000111011",
        "11001111100111110011",
        "00000111100111100000",
    ],
    [
        "00011100000000111000",
        "11001110000001110011",
        "11000110000001100011",
        "11011111111111111011",
        "11111111111111111111",
        "11111101111110111111",
        "11111111111111111111",
        "11111111111111111111",
        "00111111111111111100",
        "00011100000000111000",
        "00111000000000011100",
        "00110000000000001100",
    ],
]
INVADER_PIXEL_SIZE = 2


def make_invader_sprite(bitmap):
    image = pygame.Surface(
        (len(bitmap[0]) * INVADER_PIXEL_SIZE, len(bitmap) * INVADER_PIXEL_SIZE),
        pygame.SRCALPHA,
    )
    for row_index, row in enumerate(bitmap):
        for column_index, pixel in enumerate(row):
            if pixel == "1":
                pygame.draw.rect(
                    image,
                    (255, 255, 255),
                    (
                        column_index * INVADER_PIXEL_SIZE,
                        row_index * INVADER_PIXEL_SIZE,
                        INVADER_PIXEL_SIZE,
                        INVADER_PIXEL_SIZE,
                    ),
                )
    return image


class Invader:
    invaders = []
    DISPLAY_X, DISPLAY_Y = 1000, 750
    sprites = {}
    speed = 1
    total_num_invaders = 0

    def __init__(self, x, y, max_x, max_y):
        Invader.invaders.append(self)
        Invader.total_num_invaders += 1
        image_variant = min((x + 1) // 2, len(INVADER_BITMAPS) - 1)
        if image_variant not in self.sprites:
            self.sprites[image_variant] = make_invader_sprite(
                INVADER_BITMAPS[image_variant]
            )
        self.image = self.sprites[image_variant]
        self.rect = self.image.get_rect()

        spacing_x = self.image.get_width() + 15
        spacing_y = self.image.get_height() + 10
        start_x = (self.DISPLAY_X - (max_y * spacing_x - 25)) // 2
        start_y = 60

        self.rect.topleft = (start_x + y * spacing_x, start_y + x * spacing_y)
        self.float_x = float(self.rect.x)

    def shoot(self):
        pass

    @classmethod
    def update_all(cls, screen):
        ma = 0
        mi = cls.DISPLAY_X
        for i in cls.invaders:
            ma = max(i.rect.right, ma)
            mi = min(i.rect.left, mi)

        if (ma >= cls.DISPLAY_X - 10 and cls.speed > 0) or (mi <= 10 and cls.speed < 0):
            cls.speed *= -1
            for invader in cls.invaders:
                invader.rect.y += 10

        for invader in cls.invaders:
            invader.float_x += cls.speed / (len(cls.invaders) / cls.total_num_invaders)
            invader.rect.x = round(invader.float_x)
            if random.random() < 0.0005:
                bullet.Bullet(1, invader.rect.centerx, invader.rect.centery)
            screen.blit(invader.image, invader.rect)
