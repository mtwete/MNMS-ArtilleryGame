import unittest
from missile import Missile

class TestMissile(unittest.TestCase):

    #test successful missile creation
    def test_missile_init(self):
        missile = Missile(400,300,32,32)
        self.assertIsNotNone(missile)

