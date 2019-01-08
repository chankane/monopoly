import pygame
from pygame.locals import *
import sys  # For exit()
import settings
import colors
import board as bd


def has_exit():
    # イベント処理
    for event in pygame.event.get():
        if event.type == QUIT:  # 閉じるボタンが押されたら終了
            return True
    return False


def loop(screen, board):
    screen.fill(colors.BLACK)  # 画面を塗りつぶし
    board.disp(screen)
    pygame.display.update()  # 画面を更新


def main():
    pygame.init()
    screen = pygame.display.set_mode(settings.SCREEN_SIZE)
    pygame.display.set_caption(settings.TITLE)
    board = bd.Board()

    while not has_exit():
        loop(screen, board)
        pygame.time.Clock().tick(settings.FPS)

    pygame.quit()  # Pygame の終了(画面閉じられる)
    sys.exit()


if __name__ == "__main__":
    main()
