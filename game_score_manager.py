
# GameScoreManager class, data structure class for adding GameScores to the leaderboard.
# It will keep up the top 10 scores in sorted order.
class GameScoreManager:

    def __init__(self):
        self.scores = []

    # Add a gameScore object to the manager, if the list is 10 scores long before adding
    # the new score, the lowest score will be removed after it is added
    def add_score(self, game_score):
        # add and sort
        self.scores.append(game_score)
        self.scores.sort(reverse=True)
        if len(self.scores) > 10:
            self.scores.remove(self.scores[-1])

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


