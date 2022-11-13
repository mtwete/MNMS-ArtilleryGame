
# Data class for a player's overall game score
class GameScore:

    def __init__(self, score: int, name: str):
        self.player_name = name
        self.score = score

    def to_string(self):
        return self.player_name + "\t" + str(self.score)

    # Override comparison operators so that gamescores can be sorted by score
    # Less than operator
    def __lt__(self, other):
        # p1 < p2 calls p1.__lt__(p2)
        return self.score < other.score

    # Equality operator
    def __eq__(self, other):
        return self.score == other.score
