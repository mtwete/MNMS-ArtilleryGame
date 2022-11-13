
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
        #If list is empty return an empty string
        if len(self.scores) == 0:
            return ""

        leaderboard_str = ""
        num_scores = len(self.scores) - 1
        # Loop over scores and call to_string method, adding it to the leaderboard_str
        # If it is the last score don't add a new line
        for i, score in enumerate(self.scores):
            if i != num_scores:
                leaderboard_str += score.to_string()+'\n'
            else:
                leaderboard_str += score.to_string()
        return leaderboard_str


