from constants import *

class Button(pygame.sprite.Sprite):
    def __init__(self, button_text, center_x, center_y):
        super().__init__()
        font = pygame.font.SysFont("arial", 30)
        self.text_rendered = font.render(button_text, True, 'white')
        self.text = button_text

        self.image = pygame.Surface((self.text_rendered.get_width() + 20, self.text_rendered.get_height() + 10))
        self.image.fill('black')
        self.rect = self.image.get_rect(centerx = center_x, centery = center_y)

        self.textpos = self.text_rendered.get_rect(centerx = self.rect.width / 2, centery = self.rect.height / 2)
        self.image.blit(self.text_rendered, self.textpos)




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
