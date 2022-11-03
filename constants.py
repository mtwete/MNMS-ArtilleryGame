import os
import pygame
import sys
import random

DISPLAY_SIZE = (800, 600)

MAIN_DIR = os.path.dirname(__file__)
IMAGES_DIR = os.path.join(MAIN_DIR, "resources/images")

TARGET_IMAGE = os.path.join(IMAGES_DIR, "target.png")

#static variable holding the list of background image file paths
#with the first being the main menu image and the rest being the images for the
#levels in ascending order.
MENU_BACKGROUND = os.path.join(IMAGES_DIR, 'Menu-Background-Resized.jpg')
HEX_BACKGROUND = os.path.join(IMAGES_DIR, 'Hex-Background-Resized.jpg')
BACKGROUND_IMAGES_FILE_PATHS = [MENU_BACKGROUND, HEX_BACKGROUND]
