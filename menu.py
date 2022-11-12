from constants import *

class Button(pygame.sprite.Sprite):
    def __init__(self, button_text, center_x, center_y):
        super().__init__()
        self.value = button_text
        self.clicked = False

        #create button surface
        self.image = pygame.Surface((250, 60), pygame.SRCALPHA)
        self.rect = self.image.get_rect(centerx=center_x, centery=center_y)
        
        #draw button box and shadow
        self.shadow = pygame.draw.rect(self.image, 'black', pygame.Rect(3, 5, 247, 55), border_radius=15)
        self.button = pygame.draw.rect(self.image, 'white', pygame.Rect(0, 0, 247, 55), border_radius=15)

        #add text on button
        self.text = pygame.font.SysFont("arialblack", 30).render(self.value, True, 'black')
        self.textpos = self.text.get_rect(centerx=self.button.width/2, centery=self.button.height/2)
        self.image.blit(self.text, self.textpos)

    def check_click(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                self.clicked = True
                print(self.value)
                # return True
        if not pygame.mouse.get_pressed()[0]:
            self.clicked = False




class Menu(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface(DISPLAY_SIZE)
        self.image.fill('aquamarine3')
        self.rect = self.image.get_rect()
        self.button_group = pygame.sprite.Group()

        self.start_button = Button("Start Game", center_x = self.rect.width / 2, center_y = self.rect.height / 2)
        self.board_button = Button("Leader Board", center_x = self.rect.width / 2, center_y = self.rect.height / 2 + 80)
        self.exit_button = Button("Exit Game", center_x = self.rect.width / 2, center_y = self.rect.height / 2 + 160)
        self.button_group.add(self.start_button, self.board_button, self.exit_button)
        self.button_group.draw(self.image)
        
    def draw(self):
        self.start_button.check_click()
        self.board_button.check_click()
        self.exit_button.check_click()
