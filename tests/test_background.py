import unittest
from utils import *
from background import Background


#Test class for background class
class TestBackground(unittest.TestCase):
    #Unit test for the constructor
    def test_constructor(self):
        background = Background(BACKGROUND_IMAGES_FILE_PATHS)
        #Make sure file index is initialized to 0, i.e. main menu
        self.assertEqual(0,background.level_background_num)
        #Make sure loc is initialized to [0,0]
        self.assertEqual([0,0],background.loc)
        #Make sure the list of files is stored correctly
        self.assertEqual(BACKGROUND_IMAGES_FILE_PATHS,background.background_file_list)
        #Make sure rect.left and rect.right are proper values
        self.assertEqual(0,background.rect.left)
        self.assertEqual(0,background.rect.top)


    #Unit test for the increment level function
    def test_increment_level(self):
        #Set up counter
        counter = 0
        #Set up background object
        background = Background(BACKGROUND_IMAGES_FILE_PATHS)
        #Make sure file index is initialized to 0, i.e. main menu
        self.assertEqual(counter,background.level_background_num)
        self.assertEqual(MENU_BACKGROUND, background.background_file_list[background.level_background_num])
        #Increment the level background
        background.increment_level_background()
        counter += 1
        #Make sure it increased properly
        self.assertEqual(counter,background.level_background_num)
        self.assertEqual(HEX_BACKGROUND, background.background_file_list[background.level_background_num])
        #Increment the level background again to make sure it loops back to the main menu index
        #if you go past the end of the list
        background.increment_level_background()
        # Make sure it increased properly
        self.assertEqual(0,background.level_background_num)
        self.assertEqual(MENU_BACKGROUND, background.background_file_list[background.level_background_num])


    # Unit test for the change_background_to_menu
    def test_change_background_to_menu(self):
        # Set up background object
        background = Background(BACKGROUND_IMAGES_FILE_PATHS)
        # Go to next background so I can check that it will go back to the main
        # menu background afterwards
        background.increment_level_background()
        background.change_background_to_menu()
        #Make sure the background level index is 0 and the image is the main menu one
        self.assertEqual(0, background.level_background_num)
        self.assertEqual(MENU_BACKGROUND,
                         background.background_file_list[background.level_background_num])

