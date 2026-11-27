"""Invader sprites and formation movement for the game."""

import random

import pygame

import bullet

INVADER_BITMAPS = [
    [
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
            "00000001111110000000",
            "00000111111111100000",
            "00000111111111100000",
            "00111111111111111100",
            "11111111111111111111",
            "11111001111110011111",
            "11111111111111111111",
            "11111111111111111111",
            "00111001111110011100",
            "00000111000011100000",
            "00111001111110011100",
            "00000111000011100000",
        ],
    ],
    [
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
            "00001110000001110000",
            "00000110000001100000",
            "00011111111111111000",
            "00111111111111111100",
            "00111101111110111100",
            "11111111111111111111",
            "11111111111111111111",
            "11011111111111111011",
            "11001111100111110011",
            "11011100000000111011",
            "00000111100111100000",
        ],
    ],
    [
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
            "00110000000000001100",
            "00011000000000011000",
            "00001100000000110000",
        ],
    ],
]
INVADER_PIXEL_SIZE = 2
INVADER_COLOR = (255, 255, 255)
INVADER_SHOOT_CHANCE = 0.0005


def make_invader_sprite(bitmap: list[str]) -> pygame.Surface:
    """Build a transparent/alpha Pygame surface from a pixel bitmap."""
    image = pygame.Surface(
        (len(bitmap[0]) * INVADER_PIXEL_SIZE, len(bitmap) * INVADER_PIXEL_SIZE),
        pygame.SRCALPHA,
    )
    for row_index, row in enumerate(bitmap):
        for column_index, pixel in enumerate(row):
            if pixel == "1":
                pygame.draw.rect(
                    image,
                    INVADER_COLOR,
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
    speed = 1  # pixels per frame
    MAX_SPEED_MULTIPLIER = 5
    SPEED_CURVE = 2.0
    ANIMATION_INTERVAL_MS = 250
    EDGE_MARGIN = 10
    DROP_DISTANCE = 10
    direction = 1  # 1 moves right, -1 moves left
    total_num_invaders = 0
    animation_frame = 0
    last_animation_update = 0

    def __init__(self, row: int, column: int, column_count: int) -> None:
        """Create an invader positioned in the formation's given row and column."""
        Invader.invaders.append(self)
        Invader.total_num_invaders += 1
        variant = min((row + 1) // 2, len(INVADER_BITMAPS) - 1)
        if variant not in self.sprites:
            self.sprites[variant] = tuple(
                make_invader_sprite(bitmap) for bitmap in INVADER_BITMAPS[variant]
            )
        self.images = self.sprites[variant]
        self.image = self.images[0]
        self.rect = self.image.get_rect()

        column_spacing = self.image.get_width() + 15
        row_spacing = self.image.get_height() + 10
        start_x = (self.DISPLAY_X - (column_count * column_spacing - 25)) // 2
        start_y = 60

        self.rect.topleft = (
            start_x + column * column_spacing,
            start_y + row * row_spacing,
        )
        self.float_x = float(self.rect.x)

    @classmethod
    def current_speed(cls) -> float:
        """Return the speed that is scaled by the number of alive/dead invaders."""
        remaining = len(cls.invaders)
        if remaining <= 0 or cls.total_num_invaders <= 0:
            return 0.0

        kills = cls.total_num_invaders - remaining
        progress = kills / max(cls.total_num_invaders - 1, 1)
        progress = min(max(progress, 0.0), 1.0)

        multiplier = 1 + (cls.MAX_SPEED_MULTIPLIER - 1) * progress**cls.SPEED_CURVE
        return cls.speed * multiplier

    @classmethod
    def update_all(cls, screen: pygame.Surface) -> None:
        """Updates all invaders by changing the animation state, moving and draw all of them."""
        cls._update_animation()
        cls._handle_edge()
        cls._update_invaders(screen)

    @classmethod
    def _update_animation(cls) -> None:
        """Advance the animation frame when its time elapses."""
        now = pygame.time.get_ticks()
        if now - cls.last_animation_update >= cls.ANIMATION_INTERVAL_MS:
            cls.animation_frame = 1 - cls.animation_frame
            cls.last_animation_update = now

    @classmethod
    def _handle_edge(cls) -> None:
        """Reverse and drop the formation when it reaches a screen edge."""
        if not cls.invaders:
            return

        rightmost_edge = max(invader.rect.right for invader in cls.invaders)
        leftmost_edge = min(invader.rect.left for invader in cls.invaders)
        reached_edge = (
            cls.direction > 0 and rightmost_edge >= cls.DISPLAY_X - cls.EDGE_MARGIN
        ) or (cls.direction < 0 and leftmost_edge <= cls.EDGE_MARGIN)

        if reached_edge:
            cls.direction *= -1
            for invader in cls.invaders:
                invader.rect.y += cls.DROP_DISTANCE

    @classmethod
    def _update_invaders(cls, screen: pygame.Surface) -> None:
        """Move, shoot, animate, and draw each remaining invader."""
        step = cls.current_speed() * cls.direction
        for invader in cls.invaders:
            invader.float_x += step
            invader.rect.x = round(invader.float_x)
            if random.random() < INVADER_SHOOT_CHANCE:
                bullet.Bullet(1, invader.rect.centerx, invader.rect.centery)
            invader.image = invader.images[cls.animation_frame]
            screen.blit(invader.image, invader.rect)
