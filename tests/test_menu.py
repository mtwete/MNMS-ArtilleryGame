import pygame
import unittest
from unittest.mock import MagicMock
from menu import Menu

class TestMenu(unittest.TestCase):
    def setUp(self) -> None:
        self.menu = Menu()
        pass

    def test_menu_constructor(self):
        self.assertEqual(len(self.menu.button_group), 3)
