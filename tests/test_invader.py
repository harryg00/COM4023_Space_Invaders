import os
import unittest
from unittest.mock import patch

os.environ["SDL_AUDIODRIVER"] = "dummy"
os.environ["SDL_VIDEODRIVER"] = "dummy"

import pygame

pygame.init()

from invader import Invader


class InvaderUpdateTests(unittest.TestCase):
    def setUp(self) -> None:
        Invader.invaders.clear()
        Invader.total_num_invaders = 0
        Invader.direction = 1
        Invader.animation_frame = 0
        Invader.last_animation_update = 0
        self.screen = pygame.Surface((Invader.DISPLAY_X, Invader.DISPLAY_Y))

    def test_update_all_advances_animation_frame(self) -> None:
        invader = Invader(0, 0, 1)

        with (
            patch("pygame.time.get_ticks", side_effect=(0, 250)),
            patch("invader.random.random", return_value=1),
        ):
            Invader.update_all(self.screen)
            first_pose = invader.image
            Invader.update_all(self.screen)

        self.assertIsNot(invader.image, first_pose)

    def test_update_all_reverses_and_drops_at_screen_edge(self) -> None:
        invader = Invader(0, 0, 1)
        invader.rect.right = Invader.DISPLAY_X - Invader.EDGE_MARGIN
        invader.float_x = float(invader.rect.x)
        original_x = invader.rect.x
        original_y = invader.rect.y

        with (
            patch("pygame.time.get_ticks", return_value=0),
            patch("invader.random.random", return_value=1),
        ):
            Invader.update_all(self.screen)

        self.assertEqual(Invader.direction, -1)
        self.assertEqual(invader.rect.y, original_y + Invader.DROP_DISTANCE)
        self.assertEqual(invader.rect.x, original_x - 1)


if __name__ == "__main__":
    unittest.main()
