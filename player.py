from utils import *

#player tank
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()

        # image = pygame.image.load(TANK_UP)
        self.image = pygame.transform.scale(pygame.image.load(TANK_UP), (width, height))
        self.direction = TANK_UP

        #size
        self.width = width
        self.height = height

        #display
        self.rect = self.image.get_rect()

        #update image location
        self.rect.x = x
        self.rect.y = y
        
        #scorekeep
        self.score = 0

    def update_player(self):

        #tank movement
        #also updates the tank image to be facing in the direction of movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= 2
            self.image = pygame.transform.scale(pygame.image.load(TANK_LEFT), (self.width, self.height))
            self.direction = TANK_LEFT
        elif keys[pygame.K_d]:
            self.rect.x += 2
            self.image = pygame.transform.scale(pygame.image.load(TANK_RIGHT), (self.width, self.height))
            self.direction = TANK_RIGHT
        elif keys[pygame.K_w]:
            self.rect.y-= 2
            self.image = pygame.transform.scale(pygame.image.load(TANK_UP), (self.width, self.height))
            self.direction = TANK_UP
        elif keys[pygame.K_s]:
            self.rect.y+= 2
            self.image = pygame.transform.scale(pygame.image.load(TANK_DOWN), (self.width, self.height))
            self.direction = TANK_DOWN


        #stops player from going off screen
        if self.rect.x <= 0:
            self.rect.x = 0
        if self.rect.x >= DISPLAY_SIZE[0] - self.rect.width:
            self.rect.x = DISPLAY_SIZE[0] - self.rect.width
        if self.rect.y <= 0:
            self.rect.y = 0
        if self.rect.y >= DISPLAY_SIZE[1] - self.rect.height:
            self.rect.y = DISPLAY_SIZE[1] - self.rect.height 

    def update_score(self, add_point=1):
        self.score += add_point

    #display: the pygame display object used by the game, it will have the score blit onto it
    def display_score(self, display):
        score_font = pygame.font.SysFont('cambria', 26)
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