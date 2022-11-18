import pygame
import unittest
from unittest.mock import MagicMock
from menu import Menu

class TestMenu(unittest.TestCase):
    def setUp(self) -> None:
        pygame.font.init()
    #     pygame.display = MagicMock()

    # def test_menu_constructor(self):
    #     menu = Menu()
    #     self.assertEqual(len(menu.button_group), 3)
