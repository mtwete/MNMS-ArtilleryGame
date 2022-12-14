import unittest
from unittest.mock import MagicMock
import pygame
from leaderboard import Leaderboard


class TestLeaderboard(unittest.TestCase):
    def setUp(self) -> None:
        pygame.init()
        pygame.display.set_mode((800,600))
        self.leaderboard_scores = """1. Andre	880\n2. Rene	878\n3. Adam	783\n4. Mina	680\n5. Natasha	573\n6. Sam	499\n7. Nick	461\n8. Surya	259\n9. Matt	182\n10. Rebecca	151"""
        self.leaderboard = Leaderboard(self.leaderboard_scores)

    def test_constructor(self):
        self.assertEqual(len(self.leaderboard.button_group), 2)
        self.assertEqual(self.leaderboard.leaderboard_scores, self.leaderboard_scores)

    def test_check_button_click(self):
        return_val = self.leaderboard.check_button_click()
        self.assertEqual(return_val,"Leader Board")

    def test_update_scores(self):
        new_scores = """1. Tim	880\n2. Rene	878\n3. Adam	783\n4. Mina	680\n5. Natasha	573\n6. Sam	499\n7. Nick	461\n8. Surya	259\n9. Matt	182\n10. Rebecca	151"""
        self.leaderboard.blit_topscore_text = MagicMock()
        self.leaderboard.update_scores(new_scores)
        self.assertEqual(self.leaderboard.leaderboard_scores, new_scores)
        self.leaderboard.blit_topscore_text.assert_called()

    def test_blit_topscore_text(self):
        self.leaderboard.draw = MagicMock()
        self.leaderboard.blit_topscore_text()
        self.leaderboard.draw.assert_called()