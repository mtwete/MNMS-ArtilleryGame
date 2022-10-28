import pygame


#<a href="https://www.freepik.com/free-vector/futuristic-technological-wallpaper_10987662.htm#query=gaming%20background&position=6&from_view=keyword">Image by coolvector</a> on Freepik


class Background:
    def __init__(self,background_file, loc=[0,0]):
        self.image = pygame.image.load(background_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.right = loc
