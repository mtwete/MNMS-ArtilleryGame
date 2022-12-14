from utils import *
from target import Target

class Explosion(pygame.sprite.Sprite):

    def __init__(self, target: Target) -> None:
        super().__init__()
        self.images = []
        for num in range(5):
            img_path = os.path.join(IMAGES_DIR, f'explosions/explosion_{str(num)}.png')
            img = pygame.image.load(f"{img_path}")
            img = pygame.transform.scale(img, (target.rect.size[0] + 30, target.rect.size[1] + 30))
            self.images.append(img)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = target.rect.center
        self.explosion_speed = 6
        self.speed_counter = 0

    def update(self):
        self.speed_counter += 1 #update explosion animation

        if self.speed_counter >= self.explosion_speed and self.index < len(self.images) -1:
            self.speed_counter = 0
            self.index += 1
            self.image = self.images[self.index]

        if self.index >= len(self.images) -1 and self.speed_counter >= self.explosion_speed:
            self.kill()