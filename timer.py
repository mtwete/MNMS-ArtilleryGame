from constants import *

class Timer():

    def __init__(self):
        # set the font and the starting ticks for calculating timer
        self.font = pygame.freetype.SysFont(None, 34) #34 font size
        self.font.origin=True
        self.start_ticks =  0
        self.running = False

    def start_timer(self):
        if not self.running:
            self.start_ticks =  pygame.time.get_ticks() 
            self.running = True


    def update_timer(self, clock, display):
        total_ticks = pygame.time.get_ticks()

        seconds = TIMER_SECONDS - int((total_ticks - self.start_ticks) /1000) #divided by millisconds

        #when the timer ends, may want to change this to switch pages instead of quit
        if seconds < 0:
            self.running = False
            sys.exit()

        #display the timer
        out = '{seconds:02d}'.format(seconds=seconds)
        self.font.render_to(display, (DISPLAY_SIZE[0] // 2.1, DISPLAY_SIZE[1] // 20), out, pygame.Color('White'))
        pygame.display.flip()
        clock.tick(60)