import pygame 
import sys
from player import Player
from missile import Missile
from background import Background

MENU_BACK = "docs/Menu-Background.jpg"
LEVEL1_BACK = "docs/Hex-Background.jpg"

pygame.init()
display = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()


#tank instance
player = Player(400, 300, 32, 32)
#append missiles
player_missile = []

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
    for bullet in player_missile:
        bullet.main(display)

    #60 fps
    clock.tick(60)
    pygame.display.update()
