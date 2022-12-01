from background import Background
from utils import *
from button import Button
from pygame_textinput import TextInputVisualizer, TextInputManager


class InputName(pygame.sprite.Sprite):
    #Constructor
    def __init__(self):
        super().__init__()
        #Instruction and re-enter name strings
        self.instruction_string = "Please input your name(must be between 1 and 15 characters) below:"
        self.reenter_string = "Your name must be at least 1 character, please try again"
        self.max_len = 15
        #Set up background
        self.image = Background(BACKGROUND_IMAGES_FILE_PATHS).image.convert()
        self.rect = self.image.get_rect()
        #Display the instructions for inputting a name
        self.instruction_text = pygame.font.SysFont("arialblack", 20).render(self.instruction_string, True, 'white')
        self.instruction_textpos = self.instruction_text.get_rect(centerx=self.rect.width / 2, centery=self.rect.height / 3)
        self.image.blit(self.instruction_text, self.instruction_textpos)
        #Set up re-enter string text objects
        self.reenter_text = pygame.font.SysFont("arialblack", 16).render(self.reenter_string, True, 'red')
        self.reenter_textpos = self.reenter_text.get_rect(centerx=self.rect.width / 2,
                                                                  centery=self.rect.height / 1.5)

        #Manager for the TextInputVisualizer, it will stop inputs from being less than 0 and greater than 15
        self.manager = TextInputManager(validator = lambda input: len(input) <= self.max_len and len(input) > 0)

        #Generate instruction_text input box
        green_rgb = (0,145,0)
        white_rgb = (255,255,255)
        self.input_text_font = pygame.font.SysFont("arial", 24)
        self.text_input_box = TextInputVisualizer(manager= self.manager, font_object=self.input_text_font,
                                                  font_color=green_rgb, cursor_color=white_rgb)

        # Single character width, used to calculated background box size behind the text input and other locations
        self.single_char_width, self.single_char_height = self.input_text_font.size("a")
        #make the surface height the same as the font and the width the same as the max name length (the just +2 makes the graphics look cleaner)
        self.input_text_background = pygame.Surface((self.single_char_width * 15 + 2, self.single_char_height))
        self.input_text_background.fill(white_rgb)
        #put input box in the center of the screen but offset to the left by half the max length of characters
        self.image.blit(self.input_text_background, (self.rect.width / 2 - self.single_char_width * (self.max_len / 2), self.rect.height / 2))

        #Copy the original input name screen
        self.image_original = self.image.copy()
        #Set up a current image, will switch to an image with the re-enter text if an invalid input is received
        self.current_image = self.image_original

        #Set up the enter button
        self.enter_button = Button(ENTER, center_x=self.rect.width / 2, center_y=self.rect.height / 2 + 160)
        self.button_group = pygame.sprite.Group()
        self.button_group.add(self.enter_button)

    #Method to draw the input name screen
    def draw(self):
        self.image.blit(self.current_image, self.rect)
        input_box_surface, input_box_loc = self.input_box_surface_and_loc()
        self.image.blit(input_box_surface,input_box_loc)
        self.button_group.update()
        self.button_group.draw(self.image)


    #Method to get the text_input_box surface and proper location
    def input_box_surface_and_loc(self):
        return self.text_input_box.surface, (self.rect.width / 2 - self.single_char_width*(self.max_len/2), self.rect.height / 2)

    #Wrapper for the update method of text_input_box
    #events = pygame events
    def input_box_update(self, events):
        self.text_input_box.update(events)

    #Method to check for button clicks
    def check_button_click(self):
        #Check for enter button click
        if self.enter_button.check_click() != None:
            name = self.text_input_box.value
            name_len = len(name)
            #Check if the name length is not in the right range
            if name_len == 0 or name_len > 15:
                #If the user tried to enter but the text was too short or long, blit the re-enter instructions
                #on the screen until the user enters an appropriate name
                self.image.blit(self.reenter_text, self.reenter_textpos)
                self.reenter_image = self.image.copy()
                self.current_image = self.reenter_image
            #If it is an ok length, return LEADER_BOARD to go to that screen
            else:
                return LEADER_BOARD
        #Otherwise return GET_NAME until a proper input is received
        return GET_NAME

    #Reset method to clear the text in the input box and reset the background to the original image
    def reset(self):
        #Need to clear the input otherwise it will still be there next time the screen shows up
        self.text_input_box.value = ""
        #Reset the current image in case the reenter text was displayed
        self.current_image = self.image_original
        self.draw()



