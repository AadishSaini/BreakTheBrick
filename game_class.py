import pygame

from sprites import *
from settings import *
import time

pygame.init()
pygame.font.init()

class Game:
    def __init__(self):
        self.win = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)

        self.running = True
        self.playing = True
        self.clock = pygame.time.Clock()

        self.all_sprites = pygame.sprite.Group()

        self.player = Player()
        self.ball = Ball(self.player)
        for a in range(10):
            self.brick = Brick(self.ball, self.player, a*100, 10)
            self.all_sprites.add(self.brick)
        for a in range(10):
            self.brick = Brick(self.ball, self.player,  a*100, 80)
            self.all_sprites.add(self.brick)

        self.all_sprites.add(self.player, self.ball)

    def new(self):
        self.win.fill(WHITE)
        self.draw()
        self.events()
        self.update()
        time.sleep(5)
        self.run()

    def run(self):
        while self.playing:
            self.clock.tick(FPS)
            self.win.fill(WHITE)
            self.draw()
            self.events()
            self.update()

    def draw(self):
        self.all_sprites.draw(self.win)

    def events(self):
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                if self.playing:
                    self.playing = False
                self.running = False

    def update(self):
        self.all_sprites.update()
        pygame.display.flip()

    def start_screen(self):
        pass

    def game_over_screen(self):
        pass
