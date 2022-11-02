import pygame
pygame.init()

#Screen Size
SCREEN_WIDTH = 800 #Pixels
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

#Game Window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('Tanker') #Window Title
icon = pygame.image.load('tank.png')
pygame.display.set_icon(icon)

#framerate
clock = pygame.time.Clock()
FPS = 60 #frame limit

#player action variables
moving_left = False
moving_right = False
moving_up = False
moving_down = False
shoot = False

bullet_img = pygame.image.load('bullet.png').convert_alpha()


BG = (144,201,120) #background color (RGB)

def draw_bg():
    screen.fill(BG)

class Tank(pygame.sprite.Sprite):
    def __init__(self, char_type, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.char_type = char_type
        self.speed = speed
        self.direction = 1
        self.flip = False
        img = pygame.image.load(f'{self.char_type}.png')
        self.image = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale))) #Tank Image Sclaing
        self.rect = self.image.get_rect() #boundary box
        self.rect.center = (x, y) #boundary co-ordinates

    def move(self, moving_left, moving_right, moving_up, moving_down):
        #reset movement variables
        dx = 0
        dy = 0


        # assign movement variables if moving directions
        if moving_left: #left
            dx = -self.speed
            self.flip = True
            self.direction = -1
        if moving_right: #right
            dx = self.speed
            self.flip = False
            self.direction = 1
        if moving_up: #up
            dy = -self.speed
            #no need of flip function
            self.direction = -1
        if moving_down: #down
            dy = self.speed
            # no need of flip function
            self.direction = 1

        #update rectangle position
        self.rect.x += dx
        self.rect.y += dy



    def draw(self): #blit function

        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)





player = Tank('player', 100, 200, 4, 5)
enemy = Tank('player',400, 300, 3, 3)



x = 100
y = 100
scale = 3 #tank scale

run = True
while run:

    #calling Functions
    clock.tick(FPS)
    draw_bg()
    player.draw()
    enemy.draw()




    player.move(moving_left, moving_right, moving_up, moving_down)

    for event in pygame.event.get(): #Events

        if event.type == pygame.QUIT: #Quit game
            run = False


        if event.type == pygame.KEYDOWN: #keyboard controls
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_d:
                moving_right = True
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_w:
                moving_up = True
            if event.key == pygame.K_s:
                moving_down = True
            if event.key == pygame.K_SPACE:
                shoot = True

        if event.type == pygame.KEYUP: #keyboard release
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False
            if event.key == pygame.K_w:
                moving_up = False
            if event.key == pygame.K_s:
                moving_down = False
            if event.key == pygame.K_SPACE:
                shoot = False


    pygame.display.update()

pygame.quit()
