from background import Background
from constants import *
from leaderboard_line_writer import LeaderboardLineWriter
from button import Button


class Leaderboard(pygame.sprite.Sprite):
    #Constructor
    #leaderboard_scores = string with leaderboard scores from the game_score_list
    #leaderboard_string method
    def __init__(self, leaderboard_scores):
        super().__init__()
        self.leaderboard_scores = leaderboard_scores

        #Set up background
        self.image = Background(BACKGROUND_IMAGES_FILE_PATHS).image.convert()
        self.rect = self.image.get_rect()
        #Display the leaderboard title text
        self.text = pygame.font.SysFont("arialblack", 50).render(LEADERBOARD_TITLE, True, 'red')
        self.textpos = self.text.get_rect(centerx=self.rect.width / 2, centery=self.rect.height / 10)
        self.image.blit(self.text, self.textpos)

        #Generate text display for actual scores from LeaderboardLineWriter
        self.score_line_writer = LeaderboardLineWriter(self.leaderboard_scores, self.rect.width,self.rect.height,self.text.get_rect().height)
        self.image.blit(self.score_line_writer.image, self.score_line_writer.rect)

        #Copy the original menu
        self.image_original = self.image.copy()

        #Set up return to menu and exit game buttons
        self.return_button = Button(RETURN_TO_MENU, center_x=self.rect.width / 2, center_y=self.rect.height / 2 + 160)
        self.exit_button = Button(EXIT_GAME, center_x=self.rect.width / 2, center_y=self.rect.height / 2 + 240)
        self.button_group = pygame.sprite.Group()
        self.button_group.add(self.return_button, self.exit_button)

    #Method to draw the leaderboard screen
    def draw(self):
        self.image.blit(self.image_original, self.rect)
        self.button_group.update()
        self.button_group.draw(self.image)

    #Method to check for button clicks
    def check_button_click(self):
        #Since run.py goes to the main menu logic when game state is None
        #if the user clicks the return button and it will return the return button
        #string, so return None instead so the game state will make the main menu logic
        #to run
        if self.return_button.check_click() is not None:
            return None
        #Check for exit button click, if there's nothing stay at the leaderboard
        return self.exit_button.check_click() or LEADER_BOARD
