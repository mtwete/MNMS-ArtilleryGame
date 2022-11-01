from constants import *
from player import Player
from missile import Missile
from target import Target
from background import Background


#initialize pygame, display, clock and target sprites
pygame.init()
display = pygame.display.set_mode(DISPLAY_SIZE)
clock = pygame.time.Clock()
targetSprites = pygame.sprite.Group()


#tank instance
player = Player(400, 300, 32, 32)
#append missile
player_missile = []

#Add a target sprite with random size
shootingTarget = Target()
targetSprites.add(shootingTarget)
while True:
    #background
    #set up background object
    background = Background(BACKGROUND_IMAGES_FILE_PATHS)
    #display the background image underneath everything else
    display.blit(background.image,background.loc)
    #Display the current score of the player
    player.display_score(display)

    #get mouse click position
    mouse_x , mouse_y = pygame.mouse.get_pos()

    #check for events in game
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
    targetSprites.draw(display)
    for bullet in player_missile:
        bullet.main(display)
        points = shootingTarget.update(bullet)
        if points is not None:
            player.update_score(points)
        if len(targetSprites.sprites()) == 0:
            shootingTarget = Target()
            targetSprites.add(shootingTarget)

    #60 fps
    clock.tick(60)
    pygame.display.update()
