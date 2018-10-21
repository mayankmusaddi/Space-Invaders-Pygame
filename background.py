import pygame
pygame.init()


class Board:
    white = (255, 255, 255)
    black = (0, 0, 0)

    def __init__(self, width, height, caption):
        self.sw = width
        self.sh = height
        self.window = 0
        self.blockw = width*(1/8)
        self.blockh = height*(1/8)
        self.caption = caption

    def printboard(self):
        self.window = pygame.display.set_mode((self.sw, self.sh))
        self.window.fill(Board.white)
        pygame.display.set_caption(self.caption)
