import pygame
import random


class Target(pygame.sprite.Sprite):

    def __init__(self, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.image = pygame.image.load('target.png')
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        #location
        self.rect.x = random.randint(50, 750)
        self.rect.y = random.randint(50, 550)
        self.radius = 18
        #size
        self.hitbox = (self.rect.x+15, self.rect.y+15)

    def update(self, shootingTarget, bullet):
        if ((bullet.y <=  shootingTarget.hitbox[1] + shootingTarget.radius) and (bullet.y >= shootingTarget.hitbox[1] - shootingTarget.radius)
                    and (bullet.x <= shootingTarget.hitbox[0] + shootingTarget.radius) and (bullet.x >= shootingTarget.hitbox[0] - shootingTarget.radius)):
            # print("hit hit hit hit")
            self.kill()
