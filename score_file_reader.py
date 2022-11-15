from game_score import GameScore
from game_score_list import GameScoreList


# Class to read a file with the leaderboard players/scores and store in a gameScoreManager
class ScoreFileReader:
    # input_file = file object containing the file with the leaderboard score data to read from
    def __init__(self, input_file):
        self.scoreFile = input_file

    # Function to read the leaderboard score data from a file and store it in a GameScoreList object
    def read_scores(self):
        # Get the lines
        lines = self.scoreFile.readlines()
        game_score_manager = GameScoreList()
        # Loop over the lines, splitting the data to feed into a GameScore object, then add that object
        # to the game score manager
        for line in lines:
            fields = line.split()
            game_score_manager.add_score(GameScore(int(fields[1]), fields[0]))
        self.scoreFile.close()
        return game_score_manager
