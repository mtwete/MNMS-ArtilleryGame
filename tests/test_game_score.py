import unittest
from game_score import GameScore


class TestGameScore(unittest.TestCase):
    # Test the constructor
    def test_constructor(self):
        game_score = GameScore(1132, "Andre")
        self.assertIsNotNone(game_score)
        self.assertEqual(game_score.score, 1132)
        self.assertEqual(game_score.player_name, "Andre")

    # Test the to_string method
    def test_tostring(self):
        game_score = GameScore(1132, "Andre")
        expected_string = "Andre" + "\t" + str(1132)
        self.assertEqual(expected_string, game_score.to_string())

    # Make sure the equality operator works for scores
    def test_equality(self):
        game_score1 = GameScore(1132, "Andre")
        game_score2 = GameScore(1132, "Jess")
        self.assertTrue(game_score1 == game_score2)
        game_score3 = GameScore(1133, "Andre")
        game_score4 = GameScore(1132, "Jess")
        self.assertFalse(game_score3 == game_score4)

    # Make sure the < operator works for scores
    def test_less_than(self):
        game_score1 = GameScore(1132, "Andre")
        game_score2 = GameScore(2132, "Jess")
        self.assertTrue(game_score1 < game_score2)
        self.assertFalse(game_score2 < game_score1)





