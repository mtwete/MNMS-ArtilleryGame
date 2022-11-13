import unittest
from game_score import GameScore


class MyTestCase(unittest.TestCase):

    def test_constructor(self):
        game_score = GameScore(1132, "Andre")
        self.assertIsNotNone(game_score)
        self.assertEqual(game_score.score, 1132)
        self.assertEqual(game_score.player_name, "Andre")

    def test_tostring(self):
        game_score = GameScore(1132, "Andre")
        expected_string = "Andre" + "\t" + str(1132)
        self.assertEqual(expected_string, game_score.to_string())

    def test_equality(self):
        game_score1 = GameScore(1132, "Andre")
        game_score2 = GameScore(1132, "Jess")
        self.assertTrue(game_score1 == game_score2)

    def test_less_than(self):
        game_score1 = GameScore(1132, "Andre")
        game_score2 = GameScore(2132, "Jess")
        self.assertTrue(game_score1 < game_score2)





