import unittest
from game_score_manager import GameScoreManager
# Have to import this class because magicmock can't override operators
from game_score import GameScore

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
        score3 = GameScore(3, "Sam")
        game_score_manager.add_score((score3))
        # Make the GameScore with the highest score is first
        self.assertEqual(game_score_manager.scores[0], score3)
        # Make the GameScore with the second highest score is second
        self.assertEqual(game_score_manager.scores[1], score2)

    # Test that it only will keep the top 10 scores when
    def test_only_10_scores(self):
        game_score_manager = GameScoreManager()
        for i in range(10):
            score = GameScore(i+1, "Adam")
            game_score_manager.add_score((score))
        score1 = GameScore(100, "Mary")
        game_score_manager.add_score((score1))
        # Make the GameScore with the highest score is first
        self.assertEqual(game_score_manager.scores[0], score1)
        # Make there are only 10 scores in the game_score_manager
        self.assertEqual(len(game_score_manager.scores), 10)

    # Test leaderboard_string method when the list is empty
    def test_leaderboard_string_empty_list(self):
        game_score_manager = GameScoreManager()
        leaderboard_string = game_score_manager.leaderboard_string()
        self.assertEqual(leaderboard_string,"")

    # Test leaderboard_string method when the list is not empty
    def test_leaderboard_string_nonempty_list(self):
        game_score_manager = GameScoreManager()
        correct_leaderboard_string = ""
        for i in range(10):
            score = GameScore(10-i, "Adam")
            game_score_manager.add_score((score))
            if i != 9:
                correct_leaderboard_string += score.to_string()+'\n'
            else:
                correct_leaderboard_string += score.to_string()
        leaderboard_string = game_score_manager.leaderboard_string()
        self.assertEqual(leaderboard_string, correct_leaderboard_string)





