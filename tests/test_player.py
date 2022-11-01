#Import libraries
import unittest
import pygame
from unittest.mock import MagicMock
from player import Player

#Test class for player class
class TestPlayer(unittest.TestCase):

    #test successful player creation
    def test_player_init(self):
        player = Player(400,300,32,32)
        self.assertIsNotNone(player)

    #unit test for the display_score method
    def test_display_score(self):
        #Set up pygame, needed to call the display_score method
        pygame.init()
        #Set up toy player object
        player = Player(400, 300, 32, 32)
        #Create a mock display object
        display = MagicMock()
        #call the method
        player.display_score(display)
        #Make sure display.blit was called
        display.blit.assert_called()




if __name__ == '__main__':
    unittest.main()