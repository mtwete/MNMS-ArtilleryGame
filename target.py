import pygame
import random
from enum import Enum

DISPLAY_SIZE = (800, 600)

class TargetAttr(Enum):
    X_SMALL = (10, 10, 9)
    SMALL = (30, 30, 7)
    MEDIUM = (50, 50, 5)
    LARGE = (70, 70, 3)
    X_LARGE = (90, 90, 1)

    def __init__(self, width: int, height: int, points: int):
        super().__init__()
        self.width = width
        self.height = height
        self.points = points


class Target(pygame.sprite.Sprite):
    
    def __init__(self, target_attr: TargetAttr):
        super().__init__()
        image = pygame.image.load('target.png')
        self.image = pygame.transform.scale(image, (target_attr.width, target_attr.height))
        self.rect = self.image.get_rect()
        #location
        self.rect.x = random.randint(0, DISPLAY_SIZE[0] - target_attr.width)
        self.rect.y = random.randint(0, DISPLAY_SIZE[1] - target_attr.height)
        self.radius = target_attr.width//2 - 2
        #size
        self.hitbox = (self.rect.x + target_attr.width//2, self.rect.y + target_attr.height//2)

    def update(self, shootingTarget, bullet):
        if ((bullet.y <=  shootingTarget.hitbox[1] + shootingTarget.radius) and (bullet.y >= shootingTarget.hitbox[1] - shootingTarget.radius)
                    and (bullet.x <= shootingTarget.hitbox[0] + shootingTarget.radius) and (bullet.x >= shootingTarget.hitbox[0] - shootingTarget.radius)):
            # print("hit hit hit hit")
            self.kill()
