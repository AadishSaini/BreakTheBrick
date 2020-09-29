# coding=utf-8

# imports the Pygame library
import pygame

# colors
shape_color = (40, 210, 250)


def main():
    # initializes Pygame
    pygame.init()

    # sets the window title
    pygame.display.set_caption(u'Draw a circle')

    # sets the window size
    screen = pygame.display.set_mode((400, 400))

    # draws 3 circles
    pygame.draw.circle(screen, shape_color, (105, 105), 80, 1)
    pygame.draw.circle(screen, shape_color, (290, 105), 80, 4)
    pygame.draw.circle(screen, shape_color, (105, 290), 80, 0)

    # updates the screen
    pygame.display.flip()

    # infinite loop
    while True:
        # returns a single event from the queue
        event = pygame.event.wait()

        # if the 'close' button of the window is pressed
        if event.type == pygame.QUIT:
            # stops the application
            break

    # finalizes Pygame
    pygame.quit()


if __name__ == '__main__':
    main()
