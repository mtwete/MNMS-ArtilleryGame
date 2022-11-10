from constants import *

class Menu(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface(DISPLAY_SIZE)
        self.image.fill('aqua')
        self.rect = self.image.get_rect()