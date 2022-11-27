from constants import *

class Missile(pygame.sprite.Sprite):
    def __init__(self, x, y, mouse_x, mouse_y):
        super().__init__()
        self.image = pygame.Surface((4, 4), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(x, y))
        self.color = 'white'
        #speed of missile
        self.speed = 7
        #math that makes it work
        self.angle = math.atan2(y-mouse_y, x-mouse_x)
        self.x_vel = math.cos(self.angle) * self.speed
        self.y_vel = math.sin(self.angle) * self.speed
        
    #display on screen
    def update(self):
        self.rect.move_ip(-int(self.x_vel), -int(self.y_vel))
        pygame.draw.circle(self.image, self.color, self.image.get_rect().center, 2)