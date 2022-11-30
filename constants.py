import os
import pygame
import sys
import random
import math

DISPLAY_SIZE = (800, 600)
TIMER_SECONDS = 100

MUSIC_VOLUME_PERCENTAGE = .03
MUSIC_FILE_PATH = 'resources/Disco_Heavy.mp3'


MAIN_DIR = os.path.dirname(__file__)
IMAGES_DIR = os.path.join(MAIN_DIR, "resources/images")
TANKS_DIR = os.path.join(MAIN_DIR, "resources/images/tanks")

TARGET_IMAGE = os.path.join(IMAGES_DIR, "target.png")
TANK_LEFT = os.path.join(TANKS_DIR, "tank_left.png")
TANK_UP =os.path.join(TANKS_DIR, "tank_up.png")
TANK_RIGHT = os.path.join(TANKS_DIR, "tank_right.png")
TANK_DOWN = os.path.join(TANKS_DIR, "tank_down.png")

#static variable holding the list of background image file paths
#with the first being the main menu image and the rest being the images for the
#levels in ascending order.
MENU_BACKGROUND = os.path.join(IMAGES_DIR, 'Menu-Background-Resized.jpg')
HEX_BACKGROUND = os.path.join(IMAGES_DIR, 'Hex-Background-Resized.jpg')
BACKGROUND_IMAGES_FILE_PATHS = [MENU_BACKGROUND, HEX_BACKGROUND]

#Leaderboard static variables
LEADERBOARD_SCORE_FILE_PATH = os.path.join(MAIN_DIR, "resources/leaderboard_scores.txt")
LEADERBOARD_TITLE = 'TOP SCORES:'

RED_VIOLET = (202, 22, 142)
CLAIRVOYANT = (100, 14, 110)

START_GAME = "Start Game"
LEADER_BOARD = "Leader Board"
GET_NAME = "Get Name"
EXIT_GAME = "Exit Game"
MAIN_MENU = "Main Menu"
ENTER = "Enter"

def create_sprite_groups(number_of_groups: int = 1):
    if number_of_groups == 1:
        return pygame.sprite.Group()

    groups = []
    for it in range(number_of_groups):
        groups.append(pygame.sprite.Group())
    return groups