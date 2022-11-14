import unittest
from unittest.mock import mock_open
from score_file_reader import ScoreFileReader
from io import StringIO

class TestScoreFileReader(unittest.TestCase):
    # Test the constructor
    def test_constructor(self):
        test_file = mock_open()
        score_file_read = ScoreFileReader(test_file)
        self.assertEqual(test_file, score_file_read.scoreFile)

    # Test the read_scores method on an empty file
    def test_read_scores_empty_file(self):
        test_file = StringIO("")
        score_file_read = ScoreFileReader(test_file)
        game_score_manager = score_file_read.read_scores()
        # Make sure the game_score_manager has an empty list
        self.assertEqual(0, len(game_score_manager.scores))

    # Test the read_scores method on a non-empty file
    def test_read_scores_non_empty_file(self):
        file_content_string = "Adam\t10\nAdam\t9\nAdam\t8\nAdam\t7\nAdam\t6"
        test_file = StringIO(file_content_string)
        score_file_read = ScoreFileReader(test_file)
        game_score_manager = score_file_read.read_scores()
        # Make sure the game_score_manager has 5 score objects
        self.assertEqual(5, len(game_score_manager.scores))




