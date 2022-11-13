
# Data class for a player's overall game score
# Class to read a file with the leaderboard players/scores and store in a gameScoreManager
from game_score import GameScore
from game_score_manager import GameScoreManager


class GameScoreReader:
    def __init__(self, file_path):
        self.scoreFile = file_path

    def read_scores(self):
        try:
            scoreboard_file = open(self.scoreFile, 'r')
            lines = scoreboard_file.readlines()
            game_score_manager = GameScoreManager()
            for line in lines:
                fields = line.split()
                game_score_manager.add_score(GameScore(int(fields[1]),fields[0]))
            return game_score_manager
        except IOError:
            # If the file isn't found just return an empty gameScoreManager
            return GameScoreManager()

