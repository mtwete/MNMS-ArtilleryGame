from constants import *

class Missile(pygame.sprite.Sprite):
    def __init__(self, x, y, mouse_x, mouse_y):
        super().__init__()
        #location
        self.x = x
        self.y = y
        #mouse clicks
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y
        #speed of missile
        self.speed = 7
        #math that makes it work
        self.angle = math.atan2(y-mouse_y, x-mouse_x)
        self.x_vel = math.cos(self.angle) * self.speed
        self.y_vel = math.sin(self.angle) * self.speed
        
    #display on screen
    def update(self, display):
        self.x -= int(self.x_vel)
        self.y -= int(self.y_vel)
        pygame.draw.circle(display, (255, 255, 255), (self.x, self.y), 2)