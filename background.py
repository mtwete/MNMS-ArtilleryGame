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
        #set up rect object, location to display the background from, and left and top fields of
        #rect
        self.rect = self.image.get_rect()
        self.loc = loc
        self.rect.left, self.rect.top = loc


    #function to change the background image to the one for the next level,
    #if it is at the last level then it will go back to the main menu background
    def increment_level_background(self):
        #Check if the level counter is already at the max level, if so
        #go back to the main menu index (i.e. 0)
        if (self.level_background_num == len(self.background_file_list) - 1):
            self.level_background_num = 0
        #otherwise increment the background level number to the one for the next level's background
        else:
            self.level_background_num += 1
        #update the image to the new background
        self.image = pygame.image.load(self.background_file_list[self.level_background_num])


    #function to change the background image back to the one for the main menu
    def change_background_to_menu(self):
        #change the background level number back to the main menu background index
        self.level_background_num = 0
        #update the image to display the main menu image
        self.image = pygame.image.load(self.background_file_list[self.level_background_num])




