from background import *


class Missile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sptime = 0


class Missile1(Missile):
    def __init__(self, x, y, board):
        super(Missile1, self).__init__(x, y)
        self.board = board
        self.typ = 'rocket-146109_640.png'
        self.icon = pygame.image.load(self.typ)
        self.icon = pygame.transform.scale(
            self.icon, (int(self.board.blockw), int(self.board.blockh)))
        self.speed = 1

    def print(self):
        self.board.window.blit(self.icon, (self.x, self.y))


class Missile2(Missile):
    def __init__(self, x, y, board):
        super(Missile2, self).__init__(x, y)
        self.board = board
        self.typ = 'rocket-clipart-transparent-background-16.png'
        self.icon = pygame.image.load(self.typ)
        self.icon = pygame.transform.scale(
            self.icon, (int(self.board.blockw), int(self.board.blockh)))
        self.speed = 2

    def print(self):
        self.board.window.blit(self.icon, (self.x, self.y))
