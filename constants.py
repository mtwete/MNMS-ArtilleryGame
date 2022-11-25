import os
import pygame
import sys
import random
import math

DISPLAY_SIZE = (800, 600)
TIMER_SECONDS = 100

MUSIC_VOLUME_PERCENTAGE = .00
MUSIC_FILE_PATH = 'resources/Disco_Heavy.mp3'


MAIN_DIR = os.path.dirname(__file__)
IMAGES_DIR = os.path.join(MAIN_DIR, "resources/images")

TARGET_IMAGE = os.path.join(IMAGES_DIR, "target.png")

#static variable holding the list of background image file paths
#with the first being the main menu image and the rest being the images for the
#levels in ascending order.
MENU_BACKGROUND = os.path.join(IMAGES_DIR, 'Menu-Background-Resized.jpg')
HEX_BACKGROUND = os.path.join(IMAGES_DIR, 'Hex-Background-Resized.jpg')
BACKGROUND_IMAGES_FILE_PATHS = [MENU_BACKGROUND, HEX_BACKGROUND]

RED_VIOLET = (202, 22, 142)
CLAIRVOYANT = (100, 14, 110)

START_GAME = "Start Game"
LEADER_BOARD = "Leader Board"
EXIT_GAME = "Exit Game"

EXPLOSION_PADDING = 30