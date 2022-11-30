from background import Background
from constants import *
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

        self.manager = TextInputManager(validator = lambda input: len(input) <= self.max_len and len(input) > 0)

        #Generate instruction_text input box
        blue_rgb = (0,0,204)
        white_rgb = (255,255,255)
        self.input_text_font = pygame.font.SysFont("arial", 24)
        #Single character width, used to calculated background box
        self.single_char_width, self.single_char_height = self.input_text_font.size("a")


        #self.text_input_manager = TextInputManager()
        #self.text_input_box = TextInputVisualizer(manager=self.input_text_font, font_object=self.input_text_font, font_color=blue_rgb,cursor_color=white_rgb)
        self.text_input_box = TextInputVisualizer(manager= self.manager, font_object=self.input_text_font,
                                                  font_color=blue_rgb, cursor_color=white_rgb)


        #Copy the original input name screen
        self.image_original = self.image.copy()

        #Set up the enter button
        self.enter_button = Button(ENTER, center_x=self.rect.width / 2, center_y=self.rect.height / 2 + 160)
        self.button_group = pygame.sprite.Group()
        self.button_group.add(self.enter_button)

    #Method to draw the leaderboard screen
    def draw(self):
        self.image.blit(self.image_original, self.rect)
        self.button_group.update()
        self.button_group.draw(self.image)


    #Method to check for button clicks
    def check_button_click(self):
        #Check for enter button click
        if self.enter_button.check_click() != None:
            name = self.text_input_box.value
            name_len = len(name)
            #Check if the name length is in the right range
            if name_len == 0 or name_len > 15:
                # If the user tried to enter but the text was too short or long, blit the re-enter instructions
                # on the screen until the user enters an appropriate name
                self.image.blit(self.reenter_text, self.reenter_textpos)
                self.image_original = self.image.copy()
            #If is an ok length, return none to break the loop in run
            else:
                #Need to clear the input otherwise it will still be there next time the screen shows up
                self.text_input_box.value = ""
                return LEADER_BOARD
        return GET_NAME



