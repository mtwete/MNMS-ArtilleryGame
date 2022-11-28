from constants import *
from player import Player
from missile import Missile
from target import Target
from background import Background
from menu import Menu
from timer import Timer
from explosion import Explosion
from score import Score

#initialize pygame, display, clock and target sprites
pygame.init()
pygame.event.set_blocked([pygame.MOUSEMOTION, pygame.ACTIVEEVENT, pygame.WINDOWLEAVE, pygame.WINDOWENTER])
pygame.display.set_caption("MNMS-ArtilleryGame")
display = pygame.display.set_mode(DISPLAY_SIZE)
clock = pygame.time.Clock()
timer = Timer()
menu = Menu()

missile_group, explosion_group, score_group, target_group = create_sprite_groups(4)

#background music
pygame.mixer.init()
pygame.mixer.music.load(MUSIC_FILE_PATH)
pygame.mixer.music.set_volume(MUSIC_VOLUME_PERCENTAGE)
pygame.mixer.music.play(-1) # -1 to repeat song endlessly


player = Player(400, 300, 32, 32)
target_group.add(Target())

#set up background object and skip menu background
game_background = Background(BACKGROUND_IMAGES_FILE_PATHS)
game_background.increment_level_background()

game_state = None
game_run = True
while game_run:
    if game_state == START_GAME:
        if not timer.is_running():
            timer.start_timer()

        display.blit(game_background.image,game_background.loc)

        #Display the current score of the player
        player.display_score(display)

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
        score_group.update()
        score_group.draw(display)

        #check collision between target and missiles
        hits = pygame.sprite.groupcollide(target_group, missile_group, True, True)
        for target in hits:
            explosion_group.add(Explosion(target.rect.centerx, target.rect.centery, target.rect.size))
            score_group.add(Score(target.points, target.rect.width, target.rect.center))
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
            game_run = False
        #bullet clicks    
        if event.type == pygame.MOUSEBUTTONDOWN and game_state == START_GAME:
            if event.button == 1:
                mouse_x , mouse_y = pygame.mouse.get_pos()
                missile_group.add(Missile(player.x, player.y, mouse_x, mouse_y))

    clock.tick(60)
    pygame.display.update()

sys.exit()