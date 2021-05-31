import pygame

pygame.init()
pygame.font.init()
class Text:
    def __init__(self, string, coords, fontSize, color):
        self.string = string
        self.coordx = coords[0]
        self.coordy = coords[1]
        self.fontSize = fontSize
        self.color = color

    @staticmethod
    def draw_text(win, string, coordx, coordy, fontSize, color):
        font = pygame.font.Font('freesansbold.ttf', fontSize)
        text = font.render(string, True, color)
        win.blit(text, (coordx, coordy))


class Button:
    def __init__(self, win, color, text, position, size, command):
        self.win = win
        self.color = color
        self.text = text
        self.coordx = position[0]
        self.coordy = position[1]
        self.width = size[0]
        self.height = size[1]
        self.command = command
        r = 0
        g = 0
        b = 0
        if(color[0] >= 10):
            r = color[0] - 10
        if(color[1] >= 10):
            g = color[1] - 10
        if(color[2] >= 10):
            b = color[2] - 10

        self.lightColor = (r, g, b)

        self.isClicked = False

    def render(self):
        while True:
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    pygame.quit()
                if(event.type == pygame.MOUSEBUTTONDOWN):
                    if(self.coordx < mouse[0] < self.coordx + self.width) and (self.coordy < mouse[1] < self.coordy + self.height):
                        self.command()
                        self.isClicked = True

            if(self.coordx < mouse[0] < self.coordx + self.width) and (self.coordy < mouse[1] < self.coordy + self.height):

                pygame.draw.rect(self.win, self.lightColor, [self.coordx, self.coordy, self.width, self.height])
            else:
                pygame.draw.rect(self.win, self.color, [self.coordx, self.coordy, self.width, self.height])

            Text.draw_text(self.win, self.text.string, self.text.coordx, self.text.coordy, self.text.fontSize, self.text.color)
            pygame.display.update()
