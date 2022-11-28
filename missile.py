import pygame
import math
from constants import *

class Missile(pygame.sprite.Sprite):
    def __init__(self, x, y, player):
        super().__init__()
        self.x = x + (player.width / 2)
        self.y = y + (player.height / 2)
        self.image = pygame.Surface((4, 4), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.color = 'white'
        #speed of missile
        self.speed = 7

        #location


        #mouse clicks
        if player.direction == TANK_UP:
            self.direction_x = player.rect.x
            self.direction_y = player.rect.y - 10
        elif player.direction == TANK_RIGHT:
            self.direction_x = player.rect.x +10
            self.direction_y = player.rect.y
        elif player.direction == TANK_DOWN:
            self.direction_x = player.rect.x
            self.direction_y = player.rect.y +10
        elif player.direction == TANK_LEFT:
            self.direction_x = player.rect.x -10
            self.direction_y = player.rect.y

        #math that makes it work
        self.angle = math.atan2(y-self.direction_y, x-self.direction_x)
        self.x_vel = math.cos(self.angle) * self.speed
        self.y_vel = math.sin(self.angle) * self.speed
        
    # display on screen
    def display(self, display, player):
        self.x -= int(self.x_vel)
        self.y -= int(self.y_vel)
        pygame.draw.circle(display, (255, 255, 255), (self.x, self.y), 2)

    def update(self):
        self.rect.move_ip(-int(self.x_vel), -int(self.y_vel))
        pygame.draw.circle(self.image, self.color, self.image.get_rect().center, 2)
