import unittest
from game_score_writer import ScoreFileWriter
from unittest.mock import MagicMock, mock_open, patch


class TestScoreFileWriter(unittest.TestCase):
    # Test the constructor
    def test_constructor(self):
        test_file = mock_open()
        game_scores = MagicMock()
        score_file_writer = ScoreFileWriter(test_file, game_scores)
        self.assertEqual(test_file, score_file_writer.scoreFile)
        self.assertEqual(game_scores, score_file_writer.gameScores)

    # Test writing empty GameScoreList
    def test_writing_empty_scores(self):
        game_scores = MagicMock()
        game_scores.scores = []
        # Doing this to mock having a file object passed to the ScoreFileWriter
        with patch('game_score_writer.ScoreFileWriter.write_scores', mock_open()) as mocked_file:
            score_file_writer = ScoreFileWriter(mocked_file, game_scores)
            score_file_writer.write_scores()
            # Make sure write is never called on the file since game_scores is empty
            mocked_file().write.assert_not_called()
