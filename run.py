import pygame 
import math
import sys



pygame.init()
display = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

#player tank
class Player:
    def __init__(self, x, y, width, height):
        #location
        self.x = x
        self.y = y
        #size
        self.width = width
        self.height = height
    #draw on screen
    def main(self, display):
        pygame.draw.rect(display, (255, 0, 0), (self.x, self.y, self.width, self.height))


class Missile:
    def __init__(self, x, y, mouse_x, mouse_y):
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
    def main(self, display):
        self.x -= int(self.x_vel)
        self.y -= int(self.y_vel)
        pygame.draw.circle(display, (255, 255, 255), (self.x, self.y), 2)

class Target:
    def __init__(self, x, y, width, height):
        self.targetImg = pygame.image.load('target.png')
        self.targetImg = pygame.transform.scale(self.targetImg, (30, 30))
        #location
        self.x = x
        self.y = y
        #size
        self.width = width
        self.height = height
    def main(self, display):
        display.blit(self.targetImg, (self.x, self.y))


#tank instance
player = Player(400, 300, 32, 32)
#append missiles
player_missile = []

shootingTarget = Target(400, 300, 20, 20)

while True:
    #background
    display.fill((70,70,70))

    #get mouse click position
    mouse_x , mouse_y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.QUIT

        #bullet clicks    
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                player_missile.append(Missile(player.x, player.y, mouse_x, mouse_y))

    #tank movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player.x -= 2
    if keys[pygame.K_d]:
        player.x += 2
    if keys[pygame.K_w]:
        player.y-= 2
    if keys[pygame.K_s]:
        player.y+= 2

    #dont go off screen
    if player.x <= 0:
        player.x = 0
    if player.x >= 766:
        player.x = 766
    if player.y <= 0:
        player.y = 0
    if player.y >= 566:
        player.y = 566 

    #display tank and bullets
    player.main(display)
    shootingTarget.main(display)
    for bullet in player_missile:
        bullet.main(display)

    #60 fps
    clock.tick(60)
    pygame.display.update()
