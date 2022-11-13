
# Class to write a gameScoreManager object to a file
class ScoreFileWriter:
    # file_path = file path to the document you want to write the leaderboard score data to
    # game_scores = GameScoreManager object that contains the leaderboard score data
    def __init__(self, file_path, game_scores):
        self.scoreFile = file_path
        self.gameScores = game_scores

    # Function to write the leaderboard score data from a GameScoreManager and store it in a file
    def write_scores(self):
        # Open the file
        file_writer = open(self.scoreFile, "w")
        # Loop over the scores in the GameScoreManager object
        num_scores = len(self.gameScores.scores)-1
        for i, score in enumerate(self.gameScores.scores):
            # Doing this check just so the last call to write doesn't add a newline to the end
            # of the file
            if i != num_scores:
                file_writer.write(score.to_string+'\n')
            else:
                file_writer.write(score.to_string)





