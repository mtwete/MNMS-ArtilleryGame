import unittest
import pygame
from unittest.mock import MagicMock, patch
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

    def test_hover_on_off_effects(self):
        self.assertIs(self.test_button.button_color, "white")

        pygame.mouse = MagicMock()
        pygame.mouse.get_pos.return_value = self.test_button.rect.topleft
        pygame.mouse.get_pressed.return_value = [False, False, False]
        self.test_button.check_click()
        self.assertIs(self.test_button.button_color, "gray")

        pygame.mouse.get_pos.return_value = (self.test_button.rect.x - 1, self.test_button.rect.y - 1)
        self.test_button.check_click()
        self.assertIs(self.test_button.button_color, "white")

    def test_click_on_off_effects(self):
        self.assertFalse(self.test_button.clicked)
        
        pygame.mouse = MagicMock()
        pygame.mouse.get_pos.return_value = self.test_button.rect.topleft
        pygame.mouse.get_pressed.return_value = [True, False, False]
        self.test_button.check_click()
        self.assertTrue(self.test_button.clicked)

        pygame.mouse.get_pressed.return_value = [False, False, False]
        returned_value = self.test_button.check_click()
        self.assertFalse(self.test_button.clicked)
        self.assertEqual(returned_value, self.test_button.value)