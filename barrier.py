import pygame

class Barrier:
    barriers = []

    def __init__(self, x, y, cell_size=1):
        self.x = x
        self.y = y
        self.cell_size = cell_size 

        # Barrier shape. Barrier is represented by a grid of 1s and 0s. 0 is empty space, 1 is a small rectangle.
        # When a bullet hits a barrier (1), both it and a small radius around it will be removed (set to 0)
        # eventually the barrier can be made larger but the logic kept the same
        self.grid = [
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 0, 0, 0, 0, 1, 1, 1],
            [1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
        ]

        self.rows = len(self.grid)
        self.cols = len(self.grid[0])

        Barrier.barriers.append(self)

    def get_cell_rect(self, row, col):
        return pygame.Rect(
            self.x + col * self.cell_size,
            self.y + row * self.cell_size,
            self.cell_size,
            self.cell_size
        )

    def draw(self, surface):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col] == 1:
                    rect = self.get_cell_rect(row, col)
                    pygame.draw.rect(surface, (0, 255, 0), rect)

    def update(self, screen):
        self.draw(screen)
