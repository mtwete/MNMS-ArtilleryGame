from constants import *

class Button(pygame.sprite.Sprite):
    def __init__(self, button_text, center_x, center_y):
        super().__init__()
        self.value = button_text
        self.clicked = False
        self.button_color = 'white'
        self.shadow_color = CLAIRVOYANT

        #create transparent button surface
        self.image = pygame.Surface((250, 60), pygame.SRCALPHA)
        self.rect = self.image.get_rect(centerx=center_x, centery=center_y)

    def update(self):
        #"clear" button image of previously draw elements
        self.image.fill(pygame.Color(0,0,0,0))

        #set button and shadow rectangles with correct positioning
        self.shadow_rect = pygame.Rect(3, 5, 247, 55)
        self.button_rect = pygame.Rect(0, 0, 247, 55)
        if self.clicked:
            self.button_rect.move_ip(3, 5)

        #draw rectangles onto button image surface
        self.shadow = pygame.draw.rect(self.image, self.shadow_color, self.shadow_rect, border_radius=15)
        self.button = pygame.draw.rect(self.image, self.button_color, self.button_rect, border_radius=15)

        #add text on button
        self.text = pygame.font.SysFont("arialblack", 30).render(self.value, True, 'black')
        self.textpos = self.text.get_rect(center=self.button.center)
        self.image.blit(self.text, self.textpos)

    def check_click(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.button_color = 'gray'
            if pygame.mouse.get_pressed()[0]:
                if not self.clicked:
                    self.clicked = True
            else:
                if self.clicked:
                    self.clicked = False
                    return self.value
        else:
            self.clicked = False
            self.button_color = 'white'

