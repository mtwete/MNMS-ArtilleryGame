from constants import *

class Button(pygame.sprite.Sprite):
    def __init__(self, button_text, center_x, center_y):
        super().__init__()
        self.value = button_text

        #create button surface
        self.image = pygame.Surface((250, 60), pygame.SRCALPHA)
        self.rect = self.image.get_rect(centerx=center_x, centery=center_y)
        
        #draw button box and shadow
        self.button = pygame.draw.rect(self.image, 'white', pygame.Rect(0, 0, 247, 55), border_radius=15)
        self.shadow = pygame.draw.rect(self.image, 'black', pygame.Rect(3, 5, 247, 55), border_radius=15)

        #add text on button
        self.text = pygame.font.SysFont("arialblack", 30).render(self.value, True, 'black')
        self.textpos = self.text.get_rect(centerx=self.button.width/2, centery=self.button.height/2)
        self.image.blit(self.text, self.textpos)

    def click_engage(self):
        self.button = self.shadow




class Menu(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface(DISPLAY_SIZE)
        self.image.fill('aquamarine3')
        self.rect = self.image.get_rect()

        self.button1 = Button("Start Game", center_x = self.rect.width / 2, center_y = self.rect.height / 2)

        self.button2 = Button("Leader Board", center_x = self.rect.width / 2, center_y = self.rect.height / 2 + 80)
        
    def draw(self):
        self.image.blit(self.button1.image, self.button1.rect)
        self.image.blit(self.button2.image, self.button2.rect)

        if self.button1.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                return True
