#Import libraries
import pygame


#Background class: to be used for managing background images
#for the main menu and other levels.
class Background(pygame.sprite.Sprite):
    #Class constructor
    #parameters:
    #background_files: list of strings containing the path to the background images files,
    #                  with the first file being the main menu background and the remaining
    #                  being the level backgrounds in ascending order i.e. level 1, then 2 ...
    #loc: the location to display the background image from, default to upper left i.e. [0,0]
    def __init__(self,background_files, loc=[0,0]):
        #call sprite constructor
        pygame.sprite.Sprite.__init__(self)
        #list of background image files
        self.background_file_list = background_files
        #counter variable to keep track of which image in the list is being displayed
        self.level_background_num = 0
        #initialize first background image to use as the main menu background
        self.image = pygame.image.load(self.background_file_list[self.level_background_num])
        #set up rect object, location to display the background from and left and right fields of
        #rect
        self.rect = self.image.get_rect()
        self.loc = loc
        self.rect.left, self.rect.right = loc


    #function to change the background image to the one for the next level
    def increment_level_background(self):
        #increment the background level number to display the next level's background
        self.level_background_num += 1
        #update the image to the new background
        self.image = pygame.image.load(self.background_file_list[self.level_background_num])





