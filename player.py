import pygame

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