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
target_group = pygame.sprite.Group()


#background music
pygame.mixer.init()
pygame.mixer.music.load(MUSIC_FILE_PATH)
pygame.mixer.music.set_volume(MUSIC_VOLUME_PERCENTAGE)
pygame.mixer.music.play(-1) # -1 to repeat song endlessly


#tank instance
player = Player(400, 300, 32, 32)

#Add a target sprite with random size
shootingTarget = Target()
target_group.add(shootingTarget)

#set up background object and skip menu background
game_background = Background(BACKGROUND_IMAGES_FILE_PATHS)
game_background.increment_level_background()

timer = Timer()

menu = Menu()
game_state = None
game_run = True

missile_group = pygame.sprite.Group()
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

        #check for events in game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                pygame.QUIT

            #bullet clicks    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    missile_group.add(Missile(player.x, player.y, mouse_x, mouse_y))

        #updates player movement
        player.update_player()

        #display tank, bullets and targets
        player.main(display)
        target_group.draw(display)
        
        #update and display all missiles
        missile_group.update()
        missile_group.draw(display)

        explosion_group.update()
        explosion_group.draw(display)
        pygame.sprite.groupcollide(explosion_group, missile_group, False, True)

        #check collision between target and missiles
        hits = pygame.sprite.groupcollide(target_group, missile_group, True, True)
        for target in hits:
            explosion_group.add(Explosion(target.rect.centerx, target.rect.centery))
            player.update_score(target.points)
            target_group.add(target.spawn_new_target(target_group, player))

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
