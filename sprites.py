import pygame
from settings import *

pygame.init()
pygame.font.init()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        # pygame.sprite.Sprite.__init__(self)
        super(Player, self).__init__()
        self.width = 130
        self.height = 20
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH / 2 - self.width / 2
        self.rect.y = HEIGHT - (self.height + 10)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.rect.x += 10
        if keys[pygame.K_LEFT]:
            self.rect.x -= 10

        self.bounds()

    def bounds(self):
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

class Ball(pygame.sprite.Sprite):
    def __init__(self, player):
        super(Ball, self).__init__()
        self.height = 15
        self.width = 15
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH /2, HEIGHT /2)
        self.x_vel = 8
        self.y_vel = -7
        self.p = player

    def update(self):
        self.rect.x+= self.x_vel
        self.rect.y+= self.y_vel
        self.bounds()
        self.collisions()

    def bounds(self):
        if self.rect.top <= 0:
            if self.rect.bottom >= HEIGHT:
                pass
            else:
                self.y_vel *= -1
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            if self.rect.bottom >= HEIGHT:
                pass
            else:
                self.x_vel *= -1

        if self.rect.bottom >= HEIGHT:
            pygame.quit()

    def collisions(self):
        if self.rect.bottom >= self.p.rect.top and (self.rect.x >= self.p.rect.left and self.rect.x <= self.p.rect.right):
            self.y_vel *= -1

class Brick(pygame.sprite.Sprite):
    def __init__(self, ball, x, y):
        super(Brick, self).__init__()
        self.image = pygame.Surface((95, 50))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.ball = ball

    def update(self):
        self.check_collisions()

    def check_collisions(self):
        if self.rect.colliderect(self.ball.rect):
            print("BOOM!")

            self.ball.y_vel *= -1
            self.kill()
