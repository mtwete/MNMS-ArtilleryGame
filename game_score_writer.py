# Class to write a gameScoreManager object to a file
class ScoreFileWriter:
    # output_file = file object to write the leaderboard score data to
    # game_scores = GameScoreList object that contains the leaderboard score data
    def __init__(self, output_file, game_scores):
        self.scoreFile = output_file
        self.gameScores = game_scores

    # Function to write the leaderboard score data from a GameScoreList and store it in a file
    def write_scores(self):
        num_scores = len(self.gameScores.scores)-1
        # Loop over the scores in the GameScoreList object and write each one on a separate line
        for i, score in enumerate(self.gameScores.scores):
            # Doing this check just so the last call to write doesn't add a newline to the end
            # of the file
            if i != num_scores:
                self.scoreFile.write(score.to_string+'\n')
            else:
                self.scoreFile.write(score.to_string)
        self.scoreFile.close()






