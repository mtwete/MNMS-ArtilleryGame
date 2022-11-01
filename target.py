import pygame
import random


class Target(pygame.sprite.Sprite):

    def __init__(self, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.image = pygame.image.load('docs/target.png')
        self.image = pygame.transform.scale(self.image, (30, 30))
        #sprites require rect
        self.rect = self.image.get_rect()
        #location
        self.rect.x = random.randint(50, 750)
        self.rect.y = random.randint(50, 550)

        #18 is the radius that fits around the target for the hitbox
        self.radius = 18
        #size of the hitbox to detect collision
        self.hitbox = (self.rect.x+15, self.rect.y+15)

    def update(self, shootingTarget, bullet):
        #check if the bullet is hitting the target and kill the target if true
        if ((bullet.y <=  shootingTarget.hitbox[1] + shootingTarget.radius) 
        and (bullet.y >= shootingTarget.hitbox[1] - shootingTarget.radius)
        and (bullet.x <= shootingTarget.hitbox[0] + shootingTarget.radius) 
        and (bullet.x >= shootingTarget.hitbox[0] - shootingTarget.radius)):
            self.kill()
