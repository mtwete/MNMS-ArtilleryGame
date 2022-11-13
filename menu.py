from constants import *
from background import Background
from long_text_writer import LongTextWriter

class Button(pygame.sprite.Sprite):
    def __init__(self, button_text, center_x, center_y):
        super().__init__()
        self.value = button_text
        self.clicked = False
        self.button_color = 'white'

        #create button surface
        self.image = pygame.Surface((250, 60), pygame.SRCALPHA)
        self.rect = self.image.get_rect(centerx=center_x, centery=center_y)
        

    def update(self):
        self.shadow = pygame.draw.rect(self.image, CLAIRVOYANT, pygame.Rect(3, 5, 247, 55), border_radius=15)
        self.button = pygame.draw.rect(self.image, self.button_color, pygame.Rect(0, 0, 247, 55), border_radius=15)

        #add text on button
        self.text = pygame.font.SysFont("arialblack", 30).render(self.value, True, 'black')
        self.textpos = self.text.get_rect(center=self.button.center)
        self.image.blit(self.text, self.textpos)

    def check_click(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.button_color = 'gray'
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                self.clicked = True
                return True
            if not pygame.mouse.get_pressed()[0]:
                self.clicked = False
        else:
            self.button_color = 'white'




class Menu(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = Background(BACKGROUND_IMAGES_FILE_PATHS).image
        self.rect = self.image.get_rect()
        self.button_group = pygame.sprite.Group()

        self.start_button = Button("Start Game", center_x=self.rect.width/2, center_y = self.rect.height/2 + 80)
        self.board_button = Button("Leader Board", center_x=self.rect.width/2, center_y = self.rect.height/2 + 160)
        self.exit_button = Button("Exit Game", center_x=self.rect.width/2, center_y = self.rect.height/2 + 240)
        self.button_group.add(self.start_button, self.board_button, self.exit_button)

        #add message to screen
        self.text = pygame.font.SysFont("arialblack", 50).render("Welcome Player", True, 'white')
        self.textpos = self.text.get_rect(centerx=self.rect.width/2, centery=self.rect.height/5)
        self.image.blit(self.text, self.textpos) 

        self.description = '''
        Game Objective:  Clear as many targets by shooting bullets from the tank
        to blast away the enemy.  Hurry, time is running out!
        '''
        text_writer = LongTextWriter(self.description)
        text_writer.update()
        text_writer.rect.center = (self.rect.width/2, self.rect.height/2.5)
        self.image.blit(text_writer.image, text_writer.rect)

    def draw(self):
        self.button_group.update()
        self.button_group.draw(self.image)
        
    def check_start_button(self):
        return self.start_button.check_click()

    def check_exit_button(self):
        return self.exit_button.check_click()
        
    def check_board_button(self):
        return self.board_button.check_click()
