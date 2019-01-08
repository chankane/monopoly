import pygame
from pygame.locals import *
import sys  # For exit()
import settings
import colors
import board as bd


def has_exit():
    # Events
    for event in pygame.event.get():
        if event.type == QUIT:  # Close button ("X" button)
            return True
    return False


def clear(screen, color=colors.BLACK):
    screen.fill(color)  # Fill background


def loop(screen, board):
    clear(screen)
    board.disp(screen)
    pygame.display.update()


def main():
    pygame.init()
    screen = pygame.display.set_mode(settings.SCREEN_SIZE)
    pygame.display.set_caption(settings.TITLE)
    board = bd.Board()

    while not has_exit():
        loop(screen, board)
        pygame.time.Clock().tick(settings.FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
