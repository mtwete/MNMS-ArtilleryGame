from constants import *
from background import Background

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
        self.textpos = self.text.get_rect(centerx=self.button.width/2, centery=self.button.height/2)
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
        self.write_description()

    def write_description(self):
        font = pygame.font.SysFont("arial", 14)
        current_line = ""
        line_count = 1
       
        def render_line():
            nonlocal line_count
            nonlocal current_line
            rendered = font.render(current_line, True, 'white')
            position = rendered.get_rect(centerx=self.rect.width/2, centery=self.rect.height/3 + (17*line_count))
            self.image.blit(rendered, position)
            current_line = ""
            line_count += 1 

        all_words = []
        all_lines = self.description.splitlines()
        for line in all_lines:
            all_words.extend(line.strip().replace('\n', ' ').split())

        for text in all_words:
            current_line += text + " "
            if font.size(current_line)[0] > 300:
                render_line()
        render_line()
        

    def draw(self):
        self.button_group.update()
        self.button_group.draw(self.image)
        
    def check_start_button(self):
        return self.start_button.check_click()

    def check_exit_button(self):
        return self.exit_button.check_click()
        
    def check_board_button(self):
        return self.board_button.check_click()
