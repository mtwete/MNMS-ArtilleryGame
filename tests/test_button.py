import unittest
import pygame
from unittest.mock import MagicMock
from button import Button

class TestButton(unittest.TestCase):
    def setUp(self) -> None:
        pygame.font.init()
        self.test_button = Button("test", 250, 250)

    def test_button_constructor(self):
        with self.assertRaises(TypeError):
            Button()
        self.assertEqual(self.test_button.value, "test")
        self.assertEqual(self.test_button.rect.center, (250, 250))
        self.assertFalse(self.test_button.clicked)

    def test_no_click_update_effect(self):
        self.test_button.update()
        self.assertNotEqual(self.test_button.shadow, self.test_button.button)

    def test_click_update_effect(self):
        self.test_button.clicked = MagicMock(True)
        self.test_button.update()
        self.assertEqual(self.test_button.shadow, self.test_button.button)

    def test_hover_effect(self):
        pass