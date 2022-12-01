from constants import *
from game_score import GameScore
from game_score_writer import ScoreFileWriter
from input_name import InputName
from player import Player
from missile import Missile
from target import Target
from background import Background
from menu import Menu
from timer import Timer
from explosion import Explosion
from score import Score
from score_file_reader import ScoreFileReader
from leaderboard import Leaderboard


#initialize pygame, display, clock, leaderboard, gamescorelist, and target sprites
pygame.init()
pygame.event.set_blocked([pygame.MOUSEMOTION, pygame.ACTIVEEVENT, pygame.WINDOWLEAVE, pygame.WINDOWENTER])
pygame.display.set_caption("MNMS-ArtilleryGame")
display = pygame.display.set_mode(DISPLAY_SIZE)
clock = pygame.time.Clock()
timer = Timer()
menu = Menu()
leaderboard_score_file = open(LEADERBOARD_SCORE_FILE_PATH, 'r')
score_file_reader = ScoreFileReader(leaderboard_score_file)
game_score_list = score_file_reader.read_scores()
leaderboard = Leaderboard(game_score_list.leaderboard_string())
input_name = InputName()

#sprite groups for the different classes of images
missile_group, explosion_group, score_group, target_group, player_group = create_sprite_groups(5)


player = Player(400, 300, 75, 75)
target_group.add(Target())

player_group.add(player)

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
        player.display_score(display)
        target_group.draw(display)
        player_group.draw(display)
        
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
            pygame.mixer.Sound.play(EXPLOSION_SFX)
            score_group.add(Score(target.points, target.rect.width, target.rect.center, display.get_rect()))
            player.update_score(target.points)
            target_group.add(Target())
        #checks for player tank / target collision. removes target with no explosion and no points given
        if (pygame.sprite.groupcollide(target_group, player_group, True, False)):
            target_group.add(Target())
            
        #countdown timer update
        timer.update_timer(display)
        if not timer.is_running():
            game_state = GET_NAME

    elif game_state == GET_NAME:
        display.blit(input_name.image, input_name.rect)
        input_name.draw()
        events = pygame.event.get()
        input_name.input_box_update(events)

        game_state = input_name.check_button_click()
        if game_state == LEADER_BOARD:
            game_score = GameScore(player.score, input_name.text_input_box.value)
            game_score_list.add_score(game_score)
            input_name.reset()
            # Need to create a new leaderboard in case the current score is in the top 10
            leaderboard.update_scores(game_score_list.leaderboard_string())

    elif game_state == LEADER_BOARD:
        # display the leaderboard and check for button clicks
        display.blit(leaderboard.image, leaderboard.rect)
        leaderboard.draw()
        game_state = leaderboard.check_button_click()

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
            
        #bullet fires with spacebar
        if event.type == pygame.KEYDOWN and game_state == START_GAME:
            if event.key == pygame.K_SPACE:
                missile_group.add(Missile(player.rect.x, player.rect.y, player))

    clock.tick(60)
    pygame.display.update()

#Write the leaderboard scores to the file
leaderboard_score_file = open(LEADERBOARD_SCORE_FILE_PATH, 'w')
game_score_writer = ScoreFileWriter(leaderboard_score_file,game_score_list)
game_score_writer.write_scores()
sys.exit()