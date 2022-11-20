from constants import *

class LeaderboardLineWriter(pygame.sprite.Sprite):

    def __init__(self, leaderboard_scores,background_rect_width,background_rect_height,
                 leaderboard_title_rect_height, font='ariel', size=24, width=500):
        super().__init__()
        self.leaderboard_scores_text = leaderboard_scores
        self.font = pygame.font.SysFont(font, size)
        self.size = size
        self.width = width + 100
        self.color = 'white'
        self.line_height = size + 6
        self.line_width = width
        self.line = 0
        self.leaderboard_score_lines = []
        self.background_rect_width = background_rect_width
        self.background_rect_height = background_rect_height
        self.leaderboard_title_rect_height = leaderboard_title_rect_height
        self.update()

    def update(self):
        self.render_all_lines()
        self.image = pygame.Surface((self.background_rect_width, self.background_rect_height), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.image.blits(self.leaderboard_score_lines)

    def render_all_lines(self):
        score_lines = self.leaderboard_scores_text.splitlines()
        for line in score_lines:
            self.render_score_line(line)

    def render_score_line(self, line):
        reformatted_line = line.replace('\t', ' ' * 4)
        score_line = self.font.render(reformatted_line, True, 'white')
        position = score_line.get_rect()
        position.centerx = self.background_rect_width / 2
        position.y = (self.background_rect_height / 10)+(self.leaderboard_title_rect_height / 2)+self.line*self.line_height
        self.leaderboard_score_lines.append((score_line, position))
        self.line += 1