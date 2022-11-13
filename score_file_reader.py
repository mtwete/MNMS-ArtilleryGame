from game_score import GameScore
from game_score_manager import GameScoreManager

# Class to read a file with the leaderboard players/scores and store in a gameScoreManager
class ScoreFileReader:
    # file_path = file path to the document containing the leaderboard score data
    def __init__(self, file_path):
        self.scoreFile = file_path

    # Function to read the leaderboard score data from a file and store it in a GameScoreManager object
    def read_scores(self):
        # Try to open the file and read in the contents
        try:
            # Open the file
            scoreboard_file = open(self.scoreFile, 'r')
            # Get the lines
            lines = scoreboard_file.readlines()
            game_score_manager = GameScoreManager()
            # Loop over the lines, splitting the data to feed into a GameScore object, then add that object
            # to the game score manager
            for line in lines:
                fields = line.split()
                game_score_manager.add_score(GameScore(int(fields[1]),fields[0]))
            return game_score_manager
        except IOError:
            # If the file isn't found just return an empty gameScoreManager
            return GameScoreManager()

