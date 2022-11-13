
# Data class for a player's overall game score
class GameScoreManager:

    def __init__(self):
        self.scores = []

    # Add a gameScore object to the manager
    def add_score(self, game_score):
        # add and sort
        self.scores.append(game_score).sort()

    # Generate the string with the top scores/players in sorted order
    def leaderboard_string(self):
        if len(self.scores) == 0:
            return ""
        leaderboard_str = ""
        num_scores = len(self.gameScores.scores) - 1
        for i, score in enumerate(self.gameScores.scores):
            if i != num_scores:
                leaderboard_str += score.to_string()+'\n'
            else:
                leaderboard_str += score.to_string()


