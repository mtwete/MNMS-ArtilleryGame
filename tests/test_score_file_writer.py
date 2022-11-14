import unittest

from game_score_writer import ScoreFileWriter
from unittest.mock import MagicMock

class TestScoreFileWriter(unittest.TestCase):
    # Test the constructor
    def test_constructor(self):
        test_file_path = '/docs/leaderboard_data.txt'
        game_scores = MagicMock()
        score_file_writer = ScoreFileWriter(test_file_path, game_scores)
        self.assertEqual(test_file_path, score_file_writer.scoreFile)
        self.assertEqual(game_scores, score_file_writer.gameScores)

    # Test writing empty GameScoreManager
    def test_writing_empty_scores(self):
        test_file_path = './test_files/test_empty_leaderboard_data.txt'
        game_scores = MagicMock()
        game_scores.scores = []
        score_file_writer = ScoreFileWriter(test_file_path, game_scores)

