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
    
    """
    Target class for tank to shoot down.
    """
    def __init__(self):
        super().__init__()
        image = pygame.image.load(TARGET_IMAGE)
        target_attr = random.choice(list(TargetAttr))
        self.image = pygame.transform.scale(image, (target_attr.width, target_attr.height))
        self.name = target_attr.name
        self.points = target_attr.points
        self.rect = self.image.get_rect()
        #location
        self.rect.x = random.randint(0, DISPLAY_SIZE[0] - target_attr.width - 50) #-20 for edge buffer
        self.rect.y = random.randint(0, DISPLAY_SIZE[1] - target_attr.height - 50) #-20 for edge buffer

    def update(self, bullet, player):
        if (self.rect.collidepoint(bullet.x, bullet.y)):
            self.kill()
            return self.points
        elif pygame.Rect.colliderect(player.rect, self.rect):
            self.kill()
            return None

    # def spawn_new_target(self, targetSprites, player):
    #     self = Target()
    #     targetSprites.add(self)
    #     while pygame.Rect.colliderect(player.rect, self.rect):
    #         self.kill()
    #         self = Target()
    #         targetSprites.add(self)
    #     return self
