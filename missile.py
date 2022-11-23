import pygame
import math
from constants import *

class Missile:
    def __init__(self, x, y, player):
        #location
        self.x = x + (player.width / 2)
        self.y = y + (player.height / 2)
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
        #speed of missile
        self.speed = 7
        #math that makes it work
        self.angle = math.atan2(y-self.direction_y, x-self.direction_x)
        self.x_vel = math.cos(self.angle) * self.speed
        self.y_vel = math.sin(self.angle) * self.speed
        
    #display on screen
    def display(self, display, player):
        self.x -= int(self.x_vel)
        self.y -= int(self.y_vel)
        pygame.draw.circle(display, (255, 255, 255), (self.x, self.y), 2)