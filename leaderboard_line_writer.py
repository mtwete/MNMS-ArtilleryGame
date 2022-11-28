from constants import *

class LeaderboardLineWriter(pygame.sprite.Sprite):
    # Constructor
    # leaderboard_scores = string with leaderboard scores from the game_score_list leaderboard_string method
    # background_rect_width = leaderboard screen background image rect width
    # background_rect_height = leaderboard screen background image rect height
    # leaderboard_title_rect_height = leaderboard title text rect height
    # font = text font
    # size = text size
    # width = line width of the leaderboard scores
    def __init__(self, leaderboard_scores,background_rect_width,background_rect_height,
                 leaderboard_title_rect_height, font='ariel', size=24, width=500):
        super().__init__()
        self.leaderboard_scores_text = leaderboard_scores
        self.font = pygame.font.SysFont(font, size)
        self.size = size
        self.width = width + 100
        # Font color
        self.color = 'white'
        # height of lines
        self.line_height = size + 6
        self.line_width = width
        # Number of lines in the leaderboard
        self.line = 0
        # Lines of leaderboard scores
        self.leaderboard_score_lines = []
        self.background_rect_width = background_rect_width
        self.background_rect_height = background_rect_height
        self.leaderboard_title_rect_height = leaderboard_title_rect_height
        self.update()

    # Update the leaderboard
    def update(self):
        self.render_all_lines()
        # Set up surface to blit the scores on and blit scores
        self.image = pygame.Surface((self.background_rect_width, self.background_rect_height), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.image.blits(self.leaderboard_score_lines)

    # Render all the lines in the leaderboard score string
    def render_all_lines(self):
        # Split the score string into lines and render each
        score_lines = self.leaderboard_scores_text.splitlines()
        for line in score_lines:
            self.render_score_line(line)

    # Render an individual score line
    # line = line to render
    def render_score_line(self, line):
        # The lines have tabs separating some values which pygame doesn't line,
        # so replace the tabs with 4 spaces
        reformatted_line = line.replace('\t', ' ' * 4)
        score_line = self.font.render(reformatted_line, True, 'white')
        # Set up proper position, so they are space right
        position = score_line.get_rect()
        position.centerx = self.background_rect_width / 2
        position.y = (self.background_rect_height / 10)+(self.leaderboard_title_rect_height / 2)+self.line*self.line_height
        # Add the score line to the list of the score lines
        self.leaderboard_score_lines.append((score_line, position))
        self.line += 1