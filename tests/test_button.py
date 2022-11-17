import unittest
import pygame
from unittest.mock import MagicMock
from button import Button

class TestButton(unittest.TestCase):
    def test_button_constructor(self):
        with self.assertRaises(TypeError):
            button = Button()
        button = Button("test", 250, 250)
        self.assertEqual(button.rect.center, (250, 250))
        self.assertFalse(button.clicked)
        self.assertEqual(button.value, "test")

    def test_no_click_update_effect(self):
        pygame.font.init()
        button = Button("test", 250, 250)
        button.update()
        self.assertNotEqual(button.shadow, button.button)

    def test_click_update_effect(self):
        pygame.font.init()
        button = Button("test", 250, 250)
        button.clicked = MagicMock(True)
        button.update()
        self.assertEqual(button.shadow, button.button)

    def test_hover_effect(self):
        button = Button("test", 250, 250)
