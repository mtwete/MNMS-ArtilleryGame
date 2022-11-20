from background import Background
from constants import *
from long_text_writer import LongTextWriter
from button import Button


#FIGURE OUT MAX WIDTH FOR THIS TEXT AND FONT TO GIVE TO CLASS GETTING NAME?


class Leaderboard(pygame.sprite.Sprite):

    def __init__(self, leaderboard_scores):
        super().__init__()
        self.leaderboard_scores = leaderboard_scores

        self.image = Background(BACKGROUND_IMAGES_FILE_PATHS).image.convert()
        self.rect = self.image.get_rect()
        self.text = pygame.font.SysFont("arialblack", 50).render(LEADERBOARD_TITLE, True, 'red')
        self.textpos = self.text.get_rect(centerx=self.rect.width / 2, centery=self.rect.height / 10)
        self.image.blit(self.text, self.textpos)

        self.score_font_size = 24
        self.score_lines_text = []
        self.line = 0
        self.width = 600
        self.line_height = self.score_font_size + 6
        self.render_scores(self.leaderboard_scores)
        self.image.blits(self.score_lines_text)

        #self.text_writer = LongTextWriter(self.leaderboard_scores, size=35, width=200)
        #self.text_writer.rect.center = (self.rect.width / 2, self.rect.height / 2.5)
        #self.image.blit(self.text_writer.image, self.text_writer.rect)

        self.image_original = self.image.copy()

        self.return_button = Button(RETURN_TO_MENU, center_x=self.rect.width / 2, center_y=self.rect.height / 2 + 160)
        self.exit_button = Button(EXIT_GAME, center_x=self.rect.width / 2, center_y=self.rect.height / 2 + 240)
        self.button_group = pygame.sprite.Group()
        self.button_group.add(self.return_button, self.exit_button)

    def render_scores(self, scores):
        score_lines = scores.splitlines()
        font = pygame.font.SysFont('ariel', self.score_font_size)
        for line in score_lines:
            #pygame can't render tabs so need to replace
            reformatted_line = line.replace('\t', ' ' * 4)
            score_line = font.render(reformatted_line, True, 'white')
            position = score_line.get_rect()
            position.centerx = self.rect.width / 2
            position.y = (self.rect.height / 10)+(self.text.get_rect().height/2)+self.line * self.line_height
            self.score_lines_text.append((score_line, position))
            self.line += 1


    def draw(self):
        #self.image.blit(self.text_writer.image, self.text_writer.rect)
        #self.image.blit(self.imalfge_original, self.rect)
        #self.button_group.update()
        #self.button_group.draw(self.image)

        self.image.blit(self.image_original, self.rect)
        self.button_group.update()
        self.button_group.draw(self.image)

    def check_button_click(self):
        if self.return_button.check_click() is not None:
            return None
        return self.exit_button.check_click() or LEADER_BOARD


        #click_result = self.return_button.check_click()
        #if click_result is not None:
        #    return click_result
        #else:
        #    return LEADER_BOARD
