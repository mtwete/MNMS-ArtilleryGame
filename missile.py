import pygame
import math
from utils import *
from player import Player

class Missile(pygame.sprite.Sprite):
    def __init__(self, player: Player):
        super().__init__()

        #where the bullet starts, turret area of tank image
        self.x = player.rect.x + (player.rect.width / 2)
        self.y = player.rect.y + (player.rect.height / 2)

        self.image = pygame.Surface((4, 4), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.color = 'white'
        #speed of missile
        self.speed = 7

        #sets the direction for where the bullet goes, 
        #depends fully on the direction the tank is facing
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

        #math that makes the bullet move
        self.angle = math.atan2(player.rect.y-self.direction_y, player.rect.x-self.direction_x)
        self.x_vel = math.cos(self.angle) * self.speed
        self.y_vel = math.sin(self.angle) * self.speed

    #update bullet image while in motion
    def update(self):
        self.rect.move_ip(-int(self.x_vel), -int(self.y_vel))
        pygame.draw.circle(self.image, self.color, self.image.get_rect().center, 2)
