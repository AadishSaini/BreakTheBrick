import pygame
import pygame.gfxdraw

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
        if(color[0] >= 15):
            r = color[0] - 15
        if(color[1] >= 15):
            g = color[1] - 15
        if(color[2] >= 15):
            b = color[2] - 15

        self.lightColor = (r, g, b)

        self.isClicked = False

    '''
    credits: https://stackoverflow.com/a/61961971/13136192
    '''
    def draw_rounded_rect(self, surface, rect, color, corner_radius):
        ''' Draw a rectangle with rounded corners.
        Would prefer this:
            pygame.draw.rect(surface, color, rect, border_radius=corner_radius)
        but this option is not yet supported in my version of pygame so do it ourselves.

        We use anti-aliased circles to make the corners smoother
        '''
        if rect.width < 2 * corner_radius or rect.height < 2 * corner_radius:
            raise ValueError(f"Both height (rect.height) and width (rect.width) must be > 2 * corner radius ({corner_radius})")

        # need to use anti aliasing circle drawing routines to smooth the corners
        pygame.gfxdraw.aacircle(surface, rect.left+corner_radius, rect.top+corner_radius, corner_radius, color)
        pygame.gfxdraw.aacircle(surface, rect.right-corner_radius-1, rect.top+corner_radius, corner_radius, color)
        pygame.gfxdraw.aacircle(surface, rect.left+corner_radius, rect.bottom-corner_radius-1, corner_radius, color)
        pygame.gfxdraw.aacircle(surface, rect.right-corner_radius-1, rect.bottom-corner_radius-1, corner_radius, color)

        pygame.gfxdraw.filled_circle(surface, rect.left+corner_radius, rect.top+corner_radius, corner_radius, color)
        pygame.gfxdraw.filled_circle(surface, rect.right-corner_radius-1, rect.top+corner_radius, corner_radius, color)
        pygame.gfxdraw.filled_circle(surface, rect.left+corner_radius, rect.bottom-corner_radius-1, corner_radius, color)
        pygame.gfxdraw.filled_circle(surface, rect.right-corner_radius-1, rect.bottom-corner_radius-1, corner_radius, color)

        rect_tmp = pygame.Rect(rect)

        rect_tmp.width -= 2 * corner_radius
        rect_tmp.center = rect.center
        pygame.draw.rect(surface, color, rect_tmp)

        rect_tmp.width = rect.width
        rect_tmp.height -= 2 * corner_radius
        rect_tmp.center = rect.center
        pygame.draw.rect(surface, color, rect_tmp)



    def render(self, bool):
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
                rect = pygame.rect.Rect(self.coordx, self.coordy, self.width, self.height)
                self.draw_rounded_rect(self.win, rect, self.lightColor, 10)
            else:
                rect = pygame.rect.Rect(self.coordx, self.coordy, self.width, self.height)
                self.draw_rounded_rect(self.win, rect, self.color, 10)

            Text.draw_text(self.win, self.text.string, self.text.coordx, self.text.coordy, self.text.fontSize, self.text.color)
            pygame.display.update()

            if(self.isClicked):
                break;
