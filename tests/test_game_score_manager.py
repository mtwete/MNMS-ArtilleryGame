import unittest
from game_score_manager import GameScoreManager
# Have to import this class because magicmock can't override operators
from game_score import GameScore
from unittest.mock import MagicMock

class TestGameScoreManager(unittest.TestCase):

    # Test the constructor
    def test_constructor(self):
        game_score_manager = GameScoreManager()
        #make sure it is just an empty list
        self.assertEqual(len(game_score_manager.scores), 0)

    # Test adding a score
    def test_add_score(self):
        game_score_manager = GameScoreManager()
        score1 = GameScore(1,"Adam")
        game_score_manager.add_score((score1))
        #make sure the item was added
        self.assertEqual(game_score_manager.scores[0], score1)

    # Test adding multiple scores and the sort
    def test_add_score_sort(self):
        game_score_manager = GameScoreManager()
        score1 = GameScore(1,"Adam")
        game_score_manager.add_score((score1))
        score2 = GameScore(2,"Mary")
        game_score_manager.add_score((score2))
        #make sure the item was added
        self.assertEqual(game_score_manager.scores[0], score2)



