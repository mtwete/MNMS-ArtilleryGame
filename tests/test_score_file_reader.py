import unittest
from unittest.mock import mock_open
from score_file_reader import ScoreFileReader


class TestScoreFileReader(unittest.TestCase):
    # Test the constructor
    def test_constructor(self):
        test_file_path = '/docs/leaderboard_data.txt'
        score_file_read = ScoreFileReader(test_file_path)
        self.assertEqual(test_file_path, score_file_read.scoreFile)

    # Test the read_scores method on an empty file
    def test_read_scores_empty_file(self):
        test_file_path = '/docs/leaderboard_data.txt'
        score_file_read = ScoreFileReader(test_file_path)
        game_score_manager = score_file_read.read_scores()
        # Make sure the game_score_manager has an empty list
        self.assertEqual(0, len(game_score_manager.scores))

    # Test the read_scores method on a non-empty file
    def test_read_scores_non_empty_file(self):
        test_file_path = './test_files/test_leaderboard_data.txt'
        score_file_read = ScoreFileReader(test_file_path)
        game_score_manager = score_file_read.read_scores()
        # Make sure the game_score_manager has 10 score objects
        self.assertEqual(10, len(game_score_manager.scores))




