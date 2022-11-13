
# Class to write a gameScoreManager object to a file
class GameScoreWriter:

    def __init__(self, file_path, game_scores):
        self.scoreFile = file_path
        self.gameScores = game_scores

    def write_scores(self):
        file_writer = open(self.scoreFile, "w")
        # Doing this just so the last call to write doesn't add a newline to the end
        # of the file
        num_scores = len(self.gameScores.scores)-1
        for i, score in enumerate(self.gameScores.scores):
            if i != num_scores:
                file_writer.write(score.to_string+'\n')
            else:
                file_writer.write(score.to_string)





