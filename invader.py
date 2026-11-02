class Invader:
    invaders = []

    def __init__(self, x, y, variant=0):
        Invader.invaders.append(self)
        pass

    def shoot(self):
        pass

    @classmethod
    def update_all(cls, screen):
        pass

    @classmethod
    def draw_all(cls, screen):
        pass
