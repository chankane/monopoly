from pygame.locals import QUIT, KEYDOWN, K_ESCAPE
import pygame
import numpy as np
from time import sleep
import threading

old = 0
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


def _check_input():
    global old
    thread_1 = threading.Thread(target=move, args=((200, 200), lambda: thread_1.join()))
    if pygame.mouse.get_pressed()[0] != 0 and old == 0:
        thread_1.start()
    old = pygame.mouse.get_pressed()[0]
    print(thread_1.is_alive())


def move(pos, on_finished=None):
    global player
    while np.linalg.norm(np.array(pos) - np.array(player)) > 5:
        player = lerp(player, pos, 0.1)
        sleep(0.02)
    player = pos
    if on_finished:
        on_finished()


def _loop(screen):
    screen.fill((0, 0, 0))  # Fill black
    pygame.draw.circle(screen, (0, 255, 0), (int(player[0]), int(player[1])), 30)
    pygame.display.update()


def main():
    pygame.init()
    screen = pygame.display.set_mode((300, 300))

    while not _has_exit():
        _check_input()
        _loop(screen)
        pygame.time.Clock().tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()

