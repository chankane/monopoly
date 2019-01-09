from pygame.locals import QUIT, KEYDOWN, K_ESCAPE
import pygame
import numpy as n
import threading


player = (100, 100)


def lerp(val0, val1, rate):
    a = np.array(val0)
    b = np.array(val1)
    return (rate * (b - a) + a).tolist()


def _has_exit():
    # Events
    for event in pygame.event.get():
        if event.type == QUIT:  # Close button ("X" button)
            return True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            return True
    return False


def tmp(player, pos):
    player = lerp(player, pos, 0.1)

def move(pos, on_finished):
    global player
    thread = threading.Thread(target=tmp(player, pos)).start()


def _loop(screen):
    screen.fill((0, 0, 0))  # Fill black
    move((200, 200))
    pygame.draw.circle(screen, (0, 255, 0), (int(player[0]), int(player[1])), 30)
    pygame.display.update()


def main():
    pygame.init()
    screen = pygame.display.set_mode((300, 300))

    while not _has_exit():
        _loop(screen)
        print(player)
        pygame.time.Clock().tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
#print(lerp(a, b, 0.2))
