from background import Background
from utils import *
from leaderboard_line_writer import LeaderboardLineWriter
from button import Button


class Leaderboard(pygame.sprite.Sprite):
    #Constructor
    #leaderboard_scores = string with leaderboard scores from the game_score_list
    #leaderboard_string method
    def __init__(self, leaderboard_scores):
        super().__init__()
        #Leaderboard scores
        self.leaderboard_scores = leaderboard_scores

        #Set up background
        self.image = Background(BACKGROUND_IMAGES_FILE_PATHS).image.convert()
        self.rect = self.image.get_rect()
        #Display the leaderboard title text
        self.text = pygame.font.SysFont("arialblack", 50).render(LEADERBOARD_TITLE, True, 'red')
        self.textpos = self.text.get_rect(centerx=self.rect.width / 2, centery=self.rect.height / 10)
        self.image.blit(self.text, self.textpos)
        #Copy the background image
        self.background_image = self.image.copy()

        #Set up return to menu and exit game buttons
        self.return_button = Button(MAIN_MENU, center_x=self.rect.width / 2, center_y=self.rect.height / 2 + 160)
        self.exit_button = Button(EXIT_GAME, center_x=self.rect.width / 2, center_y=self.rect.height / 2 + 240)
        self.button_group = pygame.sprite.Group()
        self.button_group.add(self.return_button, self.exit_button)

        #Generate and display the top scores text
        self.blit_topscore_text()

    #Method to draw the leaderboard screen
    def draw(self):
        self.image.blit(self.current_image, self.rect)
        self.button_group.update()
        self.button_group.draw(self.image)

    #Method to check for button clicks
    def check_button_click(self):
        #Check for exit button or main menu click, if there's nothing stay at the leaderboard
        return self.return_button.check_click() or self.exit_button.check_click() or LEADER_BOARD

    #Method to blit the top score text on the original background image, needs to be done since the
    #leaderboard might change during gameplay
    def blit_topscore_text(self):
        # Generate text display for actual scores from LeaderboardLineWriter
        self.score_line_writer = LeaderboardLineWriter(self.leaderboard_scores, self.rect.width, self.rect.height,
                                                       self.text.get_rect().height)
        #Reset the current image to the background
        self.current_image = self.background_image.copy()
        #Now blit the current scores
        self.current_image.blit(self.score_line_writer.image, self.score_line_writer.rect)
        #Need to call draw so the screen doesn't flash when going from the input_name screen to leaderboard
        self.draw()

    #Method to update leaderboard in case a new score has been added to the game_score_list
    #leaderboard_scores = string with leaderboard scores from the game_score_list leaderboard_string method
    def update_scores(self,leaderboard_scores):
        self.leaderboard_scores = leaderboard_scores
        #Now blit the scores
        self.blit_topscore_text()

