from constants import *
from enum import Enum


class TargetAttr(Enum):
    X_SMALL = (20, 20, 9)
    SMALL = (30, 30, 7)
    MEDIUM = (50, 50, 5)
    LARGE = (70, 70, 3)
    X_LARGE = (90, 90, 1)

    def __init__(self, width: int, height: int, points: int):
        super().__init__()
        self.width = width
        self.height = height
        self.points = points


class Target(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        image_file = os.path.join(IMAGES_DIR, "target.png")
        image = pygame.image.load(image_file)
        target_attr = random.choice(list(TargetAttr))
        self.points = target_attr.points
        self.image = pygame.transform.scale(image, (target_attr.width, target_attr.height))
        self.rect = self.image.get_rect()
        #location
        self.rect.x = random.randint(0, DISPLAY_SIZE[0] - target_attr.width)
        self.rect.y = random.randint(0, DISPLAY_SIZE[1] - target_attr.height)
        self.radius = target_attr.width//2 - 1
        #size
        self.hitbox = (self.rect.x + target_attr.width//2, self.rect.y + target_attr.height//2)

    def update(self, bullet):
        if ((bullet.y <=  self.hitbox[1] + self.radius) and (bullet.y >= self.hitbox[1] - self.radius)
                    and (bullet.x <= self.hitbox[0] + self.radius) and (bullet.x >= self.hitbox[0] - self.radius)):
            self.kill()
            return self.points
