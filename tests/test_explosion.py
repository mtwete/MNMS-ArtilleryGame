import unittest
from itertools import product
from unittest.mock import MagicMock
from explosion import Explosion

class TestButton(unittest.TestCase):

    def setUp(self) -> None:
        self.explosion = Explosion(0, 0)

    def test_constructor(self):
        self.assertEqual(self.explosion.index, 0)
        self.assertEqual(self.explosion.speed_counter, 0)

    def test_update_sprite_index(self):
        for it in range(self.explosion.explosion_speed):
            self.explosion.update()
        self.assertGreater(self.explosion.index, 0)

    def test_self_kill(self):
        self.explosion.kill = MagicMock()
        for it in product(range(len(self.explosion.images)), range(self.explosion.explosion_speed)):
            self.explosion.update()
        self.explosion.kill.assert_called_once()
