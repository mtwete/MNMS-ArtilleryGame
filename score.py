from constants import *

class Score(pygame.sprite.Sprite):

    def __init__(self, value, size, center) -> None:
        super().__init__()
        self.value = value
        self.color1 = "yellow"
        self.color2 = "red"
        self.text_color = self.color1
        self.font = pygame.font.SysFont("arial", size)
        self.image = self.font.render(f'+{self.value}', True, self.text_color)
        self.rect = self.image.get_rect(center=center)
        self.rect.y -= size
        self.times = 4
        self.speed = 10
        self.count = 0

    def update(self):
        self.count += 1
        if self.count < self.speed:
            return
        
        if self.text_color == self.color1:
            self.text_color = self.color2
        else:
            self.text_color = self.color1

        self.image = self.font.render(f'+{self.value}', True, self.text_color)

        self.count = 0

        if self.times <= 0:
            self.kill()
        else:
            self.times -= 1