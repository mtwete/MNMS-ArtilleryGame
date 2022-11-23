from constants import *

class Explosion(pygame.sprite.Sprite):

    def __init__(self, center_x, center_y) -> None:
        super().__init__()
        self.images = []
        for num in range(5):
            img_path = os.path.join(IMAGES_DIR, f'explosions/explosion_{str(num)}.png')
            img = pygame.image.load(f"{img_path}")
            img = pygame.transform.scale(img, (100, 100))
            self.images.append(img)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (center_x, center_y)
        self.counter = 0

    def update(self):
        explosion_speed = 4
        self.counter += 1 #update explosion animation

        if self.counter >= explosion_speed and self.index < len(self.images) -1:
            self.counter = 0
            self.index += 1
            self.image = self.images[self.index]

        if self.index >= len(self.images) -1 and self.counter >= explosion_speed:
            self.kill()