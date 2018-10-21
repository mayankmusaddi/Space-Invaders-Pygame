from background import *


class Spaceship():
    def __init__(self, x, y, img, board):
        self.x = x
        self.y = y
        self.board = board
        self.icon = pygame.image.load(img)
        self.icon = pygame.transform.scale(
            self.icon, (int(board.blockw), int(board.blockh)))

    def print(self):
        self.board.window.blit(self.icon, (self.x, self.y))


class Alien():
    def __init__(self, x, y, img, board):
        self.x = x
        self.y = y
        self.sptime = 0
        self.killed = False
        self.board = board
        self.icon = pygame.image.load(img)
        self.icon = pygame.transform.scale(
            self.icon, (int(board.blockw), int(board.blockh)))

    def print(self):
        self.board.window.blit(self.icon, (self.x, self.y))
