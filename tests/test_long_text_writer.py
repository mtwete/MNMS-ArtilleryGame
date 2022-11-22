import pygame
import unittest
from unittest.mock import MagicMock
from long_text_writer import LongTextWriter

class TestLongTextWriter(unittest.TestCase):
    def setUp(self) -> None:
        # pygame.font.init()
        self.text = """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
        sed do eiusmod tempor incididunt ut labore et dolore 
        magna aliqua. Ut enim ad minim veniam, quis nostrud 
        exercitation ullamco laboris nisi ut aliquip ex ea 
        commodo consequat. Duis aute irure dolor in reprehenderit 
        in voluptate velit esse cillum dolore eu fugiat nulla 
        pariatur. Excepteur sint occaecat cupidatat non proident, 
        sunt in culpa qui officia deserunt mollit anim id est 
        laborum.
        """
        self.writer = LongTextWriter(self.text)

    def test_writer_constructor(self):
        self.assertEqual(self.writer.rendered_group, [])
        self.assertEqual(self.writer.line, 0)
        self.assertGreater(self.writer.width, self.writer.line_width)
        self.assertGreater(self.writer.line_height, self.writer.font_size)
        
    def test_writer_update(self):
        self.writer.render_long_text = MagicMock()
        self.writer.image = MagicMock()
        self.writer.update()
        self.writer.render_long_text.assert_called_once()
        
    def test_render_text(self):
        self.writer.update()
        self.assertGreater(self.writer.line, 1)