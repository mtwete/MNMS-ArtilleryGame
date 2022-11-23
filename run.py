from constants import *
from player import Player
from missile import Missile
from target import Target
from background import Background
from menu import Menu
from timer import Timer
from explosion import Explosion

#initialize pygame, display, clock and target sprites
pygame.init()
display = pygame.display.set_mode(DISPLAY_SIZE)
clock = pygame.time.Clock()
targetSprites = pygame.sprite.Group()


#background music
pygame.mixer.init()
pygame.mixer.music.load(MUSIC_FILE_PATH)
pygame.mixer.music.set_volume(MUSIC_VOLUME_PERCENTAGE)
pygame.mixer.music.play(-1) # -1 to repeat song endlessly


#tank instance
player = Player(400, 300, 32, 32)
player_missile = []

#Add a target sprite with random size
shootingTarget = Target()
targetSprites.add(shootingTarget)

#set up background object and skip menu background
game_background = Background(BACKGROUND_IMAGES_FILE_PATHS)
game_background.increment_level_background()

timer = Timer()

menu = Menu()
game_state = None
game_run = True

explosion_group = pygame.sprite.Group()

while game_run:
    if game_state == START_GAME:
        if not timer.is_running():
            timer.start_timer()

        display.blit(game_background.image,game_background.loc)

        #Display the current score of the player
        player.display_score(display)

        #get mouse click position
        mouse_x , mouse_y = pygame.mouse.get_pos()

        explosion_group.draw(display)
        explosion_group.update()

        #check for events in game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                pygame.QUIT

            #bullet clicks    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    player_missile.append(Missile(player.x, player.y, mouse_x, mouse_y))
                    explosion = Explosion(mouse_x, mouse_y)
                    explosion_group.add(explosion)

        #updates player movement
        player.update_player()


        #display tank, bullets and targets
        player.main(display)
        targetSprites.draw(display)
        for bullet in player_missile:
            bullet.main(display)
            points = shootingTarget.update(bullet)
            if points is not None:
                player.update_score(points)
            if len(targetSprites.sprites()) == 0:
                shootingTarget = shootingTarget.spawn_new_target(targetSprites, player)

        timer.update_timer(display)

    elif game_state == LEADER_BOARD:
        print("game state:", game_state)
        game_state = None

    elif game_state == EXIT_GAME:
        game_run = False

    else:
        display.blit(menu.image, menu.rect)
        menu.draw()
        game_state = menu.check_button_click()

        #check for events in game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                pygame.QUIT

    clock.tick(60)
    pygame.display.update()
