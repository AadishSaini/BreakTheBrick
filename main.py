import pygame

from game_class import *

"python.linting.pylintArgs": [
    "--disable=C0111"
]

g = Game()
g.start_screen()
while g.running:
    g.new()
    g.game_over_screen()
