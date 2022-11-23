from constants import *

#player tank
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        # image = pygame.image.load(TANK_UP)
        self.image = pygame.transform.scale(pygame.image.load(TANK_UP), (width, height))
        #size
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        #display
        self.rect = self.image.get_rect()
        #location
        self.rect.x = self.x
        self.rect.y = self.y
        #scorekeep
        self.score = 0

    def update_player(self):

        #tank movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= 2
            self.image = pygame.transform.scale(pygame.image.load(TANK_LEFT), (self.width, self.height))
        elif keys[pygame.K_d]:
            self.rect.x += 2
            self.image = pygame.transform.scale(pygame.image.load(TANK_RIGHT), (self.width, self.height))

        elif keys[pygame.K_w]:
            self.rect.y-= 2
            self.image = pygame.transform.scale(pygame.image.load(TANK_UP), (self.width, self.height))
        elif keys[pygame.K_s]:
            self.rect.y+= 2
            self.image = pygame.transform.scale(pygame.image.load(TANK_DOWN), (self.width, self.height))


        #dont go off screen
        if self.rect.x <= 0:
            self.rect.x = 0
        if self.rect.x >= 766:
            self.rect.x = 766
        if self.rect.y <= 0:
            self.rect.y = 0
        if self.rect.y >= 566:
            self.rect.y = 566 

    def update_score(self, add_point=1):
        self.score += add_point

    #function to display the current score of the player on the game screen
    #parameters:
    #display: the pygame display object used by the game, it will have the score blit onto it
    def display_score(self, display):
        #Create a font object to write the score with
        score_font = pygame.font.SysFont('cambria', 26)
        #create a surface with the current score in red text that you can
        #blit onto a different surface, the score will be red, hence (255,0,0), for visibility
        score_display = score_font.render("Score: " + str(self.score),1,(255,0,0))
        #Get the rectangle size of the text, so a background box of the right size can be drawn
        score_size = score_display.get_rect()
        score_box = pygame.Surface((score_size.w, score_size.h))
        score_box.fill("black")
        #variable for the display location of the player score, it will be in the lower left corner
        #and offset upwards by the score text box height so it isn't off the screen
        score_location = (0, 600-score_size.height)
        #display the score box background
        display.blit(score_box, score_location)
        #display the actual score text
        display.blit(score_display, score_location)