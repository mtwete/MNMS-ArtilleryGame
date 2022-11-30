import unittest
import pygame
from unittest.mock import MagicMock, call
from leaderboard_line_writer import LeaderboardLineWriter

class TestLeaderboardLineWriter(unittest.TestCase):
    def setUp(self) -> None:
        pygame.init()
        #Values of the leaderboard background rect and title text rect
        #needed for the constructor
        self.background_rect_width = 800
        self.background_rect_height = 600
        self.leaderboard_title_rect_height = 71
        self.leaderboard_scores = """1. Andre	880\n2. Rene	878\n3. Adam	783\n4. Mina	680\n5. Natasha	573\n6. Sam	499\n7. Nick	461\n8. Surya	259\n9. Matt	182\n10. Rebecca	151"""
        self.leaderboard_line_writer = LeaderboardLineWriter(self.leaderboard_scores,self.background_rect_width,
                                                             self.background_rect_height,self.leaderboard_title_rect_height)

    def test_non_empty_list_constructor(self):
        #Because there are 10 scores above
        self.assertEqual(self.leaderboard_line_writer.line, 10)
        #Because default width is 500
        self.assertEqual(self.leaderboard_line_writer.width, 500+100)
        self.assertEqual(self.leaderboard_line_writer.line_width, 500)
        #30 because default font size is 24, and line height is font size + 6
        self.assertEqual(self.leaderboard_line_writer.line_height, 30)
        self.assertEqual(self.leaderboard_line_writer.size, 24)
        self.assertEqual(self.leaderboard_line_writer.leaderboard_scores_text, self.leaderboard_scores)
        self.assertEqual(self.leaderboard_line_writer.color, 'white')
        self.assertEqual(type(self.leaderboard_line_writer.font), type(pygame.font.SysFont('ariel', 24)))
        self.assertEqual(self.leaderboard_line_writer.background_rect_width, self.background_rect_width)
        self.assertEqual(self.leaderboard_line_writer.background_rect_height, self.background_rect_height)
        self.assertEqual(self.leaderboard_line_writer.leaderboard_title_rect_height, self.leaderboard_title_rect_height)

    def test_construtor_empty_list(self):
        empty_leaderboard_line_writer = LeaderboardLineWriter("", self.background_rect_width,
                                                              self.background_rect_height,
                                                              self.leaderboard_title_rect_height)
        self.assertEqual(empty_leaderboard_line_writer.leaderboard_score_lines, [])
        self.assertEqual(empty_leaderboard_line_writer.line, 0)
        # Because default width is 500
        self.assertEqual(empty_leaderboard_line_writer.width, 500 + 100)
        self.assertEqual(empty_leaderboard_line_writer.line_width, 500)
        # 30 because default font size is 24, and line height is font size + 6
        self.assertEqual(empty_leaderboard_line_writer.line_height, 30)
        self.assertEqual(empty_leaderboard_line_writer.size, 24)
        self.assertEqual(empty_leaderboard_line_writer.leaderboard_scores_text, "")
        self.assertEqual(empty_leaderboard_line_writer.color, 'white')
        self.assertEqual(type(empty_leaderboard_line_writer.font), type(pygame.font.SysFont('ariel', 24)))
        self.assertEqual(empty_leaderboard_line_writer.background_rect_width, self.background_rect_width)
        self.assertEqual(empty_leaderboard_line_writer.background_rect_height, self.background_rect_height)
        self.assertEqual(empty_leaderboard_line_writer.leaderboard_title_rect_height,
                         self.leaderboard_title_rect_height)

    def test_update(self):
        #Make sure render_all_lines is called
        self.leaderboard_line_writer.render_all_lines = MagicMock()
        self.leaderboard_line_writer.update()
        self.leaderboard_line_writer.render_all_lines.assert_called_once()

    def test_render_all_lines(self):
        self.leaderboard_line_writer.render_score_line = MagicMock()
        self.leaderboard_line_writer.update()
        calls = [call(line) for line in self.leaderboard_line_writer.leaderboard_scores_text.splitlines()]
        self.leaderboard_line_writer.render_score_line.assert_has_calls(calls, any_order=False)

    def test_render_score_line(self):
        lines = self.leaderboard_line_writer.leaderboard_scores_text.splitlines()
        old_line_num = self.leaderboard_line_writer.line
        old_leaderboard_score_lines_len = len(self.leaderboard_line_writer.leaderboard_score_lines)
        self.leaderboard_line_writer.render_score_line(lines[0])
        self.assertEqual(self.leaderboard_line_writer.line,old_line_num+1)
        self.assertEqual(len(self.leaderboard_line_writer.leaderboard_score_lines), old_leaderboard_score_lines_len+1)



