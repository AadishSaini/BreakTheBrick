import pygame

from sprites import *
from settings import *

"python.linting.pylintArgs": [
    "--disable=C0111"
]

class Game:
    def __init__(self):
        self.win = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("BreakTheBrick")

        self.running = True
        self.playing = True
        self.clock = pygame.time.Clock()

    def new(self):
        self.run()

    def run(self):
        while self.playing:
            self.draw()
            self.events()
            self.update()

    def draw(self):
        self.clock.tick(FPS)
        self.win.fill(WHITE)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def update(self):
        pygame.display.flip()

    def start_screen(self):
        pass

    def game_over_screen(self):
        pass