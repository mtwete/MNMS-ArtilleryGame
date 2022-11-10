from constants import *

class Button(pygame.sprite.Sprite):
    def __init__(self, button_text):
        super().__init__()
        font = pygame.font.SysFont("arial", 30)
        text = font.render(button_text, True, 'white')

        self.image = pygame.Surface((text.get_width() + 20, text.get_height() + 10))
        self.image.fill('black')
        self.rect = self.image.get_rect()

        textpos = text.get_rect(centerx = self.rect.width / 2, centery = self.rect.height / 2)
        self.image.blit(text, textpos)

class Menu(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface(DISPLAY_SIZE)
        self.image.fill('aquamarine3')
        self.rect = self.image.get_rect()

        button = Button("Start Game")
        buttonpos = button.image.get_rect(centerx = self.rect.width / 2, centery = self.rect.height / 2)
        self.image.blit(button.image, buttonpos)

        button = Button("Leader Board")
        buttonpos = button.image.get_rect(centerx = self.rect.width / 2, centery = self.rect.height / 2 + + 50)
        self.image.blit(button.image, buttonpos)
        

    