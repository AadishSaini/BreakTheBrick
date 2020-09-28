import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        # pygame.sprite.Sprite.__init__(self)
        super(Player, self).__init__()
        self.image = pygame.Surface((100, 20))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 450

    def update(self):
        pass
