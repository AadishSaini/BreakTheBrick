import pygame

from game_class import *

g = Game()
g.start_screen()
while g.running:
    g.new()
    g.game_over_screen()
