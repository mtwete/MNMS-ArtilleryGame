from constants import *

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

