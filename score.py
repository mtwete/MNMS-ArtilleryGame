from constants import *

class Score(pygame.sprite.Sprite):

    def __init__(self, value, size, center, display_rect: pygame.Rect) -> None:
        super().__init__()
        self.value = value
        self.size = 20 + size//2
        self.color1 = "yellow"
        self.color2 = "red"
        self.text_color = self.color1
        self.font = pygame.font.SysFont("arial", self.size)
        self.image = self.font.render(f'+{self.value}', True, self.text_color)
        self.rect = self.image.get_rect(center=center)
        self.rect.y -= self.size
        if not display_rect.contains(self.rect):
            self.rect.y += self.size * 2
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