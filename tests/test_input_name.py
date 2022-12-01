import unittest
from unittest.mock import MagicMock
import pygame
from constants import GET_NAME, ENTER, LEADER_BOARD
from input_name import InputName

class TestInputName(unittest.TestCase):
    def setUp(self) -> None:
        self.instruction_string = "Please input your name(must be between 1-15 characters and have no spaces) below:"
        self.reenter_string = "Your name must be at least 1 character, please try again"
        self.max_len = 15
        pygame.display.set_mode((800, 600))
        self.input_name = InputName()

    def test_constructor(self):
        self.assertEqual(self.input_name.instruction_string, self.instruction_string)
        self.assertEqual(self.input_name.reenter_string, self.reenter_string)
        self.assertEqual(self.input_name.max_len, self.max_len)
        self.assertEqual(len(self.input_name.button_group), 1)

    def test_input_box_surface_and_loc(self):
        second_output = (self.input_name.rect.width / 2 - self.input_name.single_char_width*(self.input_name.max_len/2), self.input_name.rect.height / 2)
        surface, loc = self.input_name.input_box_surface_and_loc()
        self.assertEqual(loc , second_output)

    def test_input_box_update(self):
        events = MagicMock()
        self.input_name.text_input_box.update = MagicMock()
        self.input_name.input_box_update(events)
        self.input_name.text_input_box.update.assert_called_once_with(events)

    def test_reset(self):
        self.input_name.draw = MagicMock()
        self.input_name.reset()
        self.assertEqual(self.input_name.text_input_box.value,"")
        self.input_name.draw.assert_called()

    def test_check_button_click(self):
        self.assertEqual(self.input_name.check_button_click(),GET_NAME)
        self.input_name.enter_button.check_click = MagicMock(return_value=ENTER)
        self.input_name.text_input_box.value = "tim"
        self.assertEqual(self.input_name.check_button_click(), LEADER_BOARD)
        self.input_name.enter_button.check_click = MagicMock(return_value=ENTER)
        self.input_name.text_input_box.value = ""
        self.assertEqual(self.input_name.check_button_click(), GET_NAME)





