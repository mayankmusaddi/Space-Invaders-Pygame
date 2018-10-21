from players import *
from missiles import *
import random
import time

board = Board(600, 600, 'Space Invaders')
board.printboard()
sp = Spaceship(0, 7*board.blockh, "spacecraft_2_T.png", board)
al = Alien(0, 0, "green-alien-clip-art-343671.png", board)
al.sptime = time.time()
alien = [al]
mis = []
GameOver = False
kills = 0

ptime = time.time()
clock = pygame.time.Clock()
while not GameOver:
    board.window.fill(Board.black)
    sp.print()
    if time.time() - ptime > 10:
        al = Alien(0, 0, "green-alien-clip-art-343671.png", board)
        al.x = random.randint(0, 7)*board.blockw
        al.y = random.randint(0, 1)*board.blockh
        al.killed = False
        al.sptime = time.time()
        alien.append(al)
        ptime = time.time()
    i = 0
    for al in alien:
        if time.time() - al.sptime <= 8 and not al.killed:
            al.print()
        else:
            alien.pop(i)
        i += 1

    i = 0
    for mis1 in mis:
        mis1.print()
        j = 0
        for al in alien:
            if not al.killed and mis1.x == al.x and len(mis) != 0:
                if mis1.speed == 1 and mis1.y == al.y and len(alien) != 0:
                    kills += 1
                    print("KILL ", kills)
                    al.killed = True
                    alien.pop(j)
                    mis.pop(i)

                if mis1.speed == 2:
                    if (mis1.y == al.y or mis1.y == al.y-board.blockh):
                        al.sptime = time.time()-3
                        al.icon = pygame.image.load('frozen.png')
                        al.icon = pygame.transform.scale(
                            al.icon, (int(board.blockw), int(board.blockh)))
                        mis.pop(i)
            j += 1

        if time.time() - mis1.sptime > 1:
            mis1.y -= board.blockh*mis1.speed
            if mis1.y < 0 and len(mis) != 0:
                mis.pop(i)
            mis1.sptime = time.time()
        i += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                GameOver = True
            if event.key == pygame.K_SPACE:
                mis1 = Missile1(sp.x, sp.y-board.blockh, board)
                mis1.sptime = time.time()
                mis.append(mis1)
            if event.key == pygame.K_s:
                mis2 = Missile2(sp.x, sp.y-board.blockh, board)
                mis2.sptime = time.time()
                mis.append(mis2)
            if event.key == pygame.K_a:
                sp.x = sp.x-board.blockw
                if sp.x < 0:
                    sp.x = 0
            if event.key == pygame.K_d:
                sp.x = sp.x+board.blockw
                if sp.x > board.sw-board.blockw:
                    sp.x = board.sw-board.blockw
    pygame.display.update()
    clock.tick(60)
pygame.quit()
print("FINAL SCORE : ", kills)
