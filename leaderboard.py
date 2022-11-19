from background import Background
from constants import *
from long_text_writer import LongTextWriter
from button import Button

class Leaderboard(pygame.sprite.Sprite):

    def __init__(self,leaderboard_scores):
        super().__init__()
        self.leaderboard_scores = leaderboard_scores
        self.image = Background(BACKGROUND_IMAGES_FILE_PATHS).image.convert()
        self.rect = self.image.get_rect()
        self.text = pygame.font.SysFont("arialblack", 50).render(LEADERBOARD_TITLE, True, 'red')
        self.textpos = self.text.get_rect(centerx=self.rect.width / 2, centery=self.rect.height / 5)
        self.image.blit(self.text, self.textpos)
        self.text_writer = LongTextWriter(self.leaderboard_scores, size=24, width=200)
        self.text_writer.rect.center = (self.rect.width / 2, self.rect.height / 2.5)
        self.image.blit(self.text_writer.image, self.text_writer.rect)
        self.image_original = self.image.copy()
        self.return_button = Button(RETURN_TO_MENU, center_x=self.rect.width / 2, center_y=self.rect.height / 2 + 160)
        self.exit_button = Button(EXIT_GAME, center_x=self.rect.width / 2, center_y=self.rect.height / 2 + 240)
        self.button_group = pygame.sprite.Group()
        self.button_group.add(self.return_button, self.exit_button)

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
