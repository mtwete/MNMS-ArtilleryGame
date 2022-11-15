
# Data class for a player's overall game score
class GameScore:

    def __init__(self, score: int, name: str):
        self.player_name = name
        self.score = score

    # Simple to_string method
    def to_string(self):
        return self.player_name + "\t" + str(self.score)

    # Override comparison operators so that gamescores can be sorted by score
    # Less than operator
    def __lt__(self, other):
        return self.score < other.score

    # Equality operator, NOTE this is only for sorting scores, not overall object equality
    def __eq__(self, other):
        return self.score == other.score
