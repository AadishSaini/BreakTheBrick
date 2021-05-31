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
        waiting = True
        while waiting:
            for event in pygame.event.get():
                keys = pygame.key.get_pressed()
                if event.type == pygame.QUIT :
                    waiting = False
                    if self.playing:
                        self.playing = False
                    self.running = False
                if keys[pygame.K_q]:
                    waiting = False
                    if self.playing:
                        self.playing = False
                    self.running = False
                if keys[pygame.K_p]:
                    waiting = False
            self.clock.tick(15)
            self.draw_text("Press P to play the game", 100, 100, 28, GREEN)
            self.draw_text("Press Q to exit ", 130, 100, 28, RED)
            self.draw_text("smh", 160, 100, 24, WHITE)
            pygame.display.flip()

    def game_over_screen(self):
        pass

    def draw_text(self, string, coordx, coordy, fontSize, color):
        font = pygame.font.Font('freesansbold.ttf', fontSize)
        text = font.render(string, True, color)
        self.win.blit(text, (coordx, coordx))
