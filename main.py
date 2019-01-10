import pygame
import sys  # For exit()
import settings
import colors
from board import Board
from socketClient import Socket
from room import Room
from player import Player

screen = None
board = None


class Main:
    @staticmethod
    def __has_exit():
        # Events
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:  # Close button ("X" button)
                return True
        return False

    @staticmethod
    def __load_img_background(path):
        img = pygame.image.load(path).convert()
        size = (min(settings.SCREEN_SIZE), min(settings.SCREEN_SIZE))
        img = pygame.transform.scale(img, size)
        return img

    def __init__(self):
        pygame.init()
        pygame.display.set_caption(settings.TITLE)
        self.__screen = pygame.display.set_mode(settings.SCREEN_SIZE)
        self.__img_background = self.__load_img_background(settings.IMG_BACKGROUND)
        self.__board = Board()
        Socket.connect_server()

        # ↓ ----------デバッグ用----------
        self.room = Room()
        self.room.add_member(Player(name="プレイヤー1", position=0, color=colors.RED))
        self.room.add_member(Player(name="プレイヤー2", position=5, color=colors.GREEN))
        self.room.add_member(Player(name="プレイヤー3", position=10, color=colors.BLUE))
        self.room.add_member(Player(name="プレイヤー4", position=15, color=colors.YELLOW))
        # ↑ ----------デバッグ用----------

        while not Main.__has_exit():
            self.__loop()
            pygame.time.Clock().tick(settings.FPS)

        Socket.disconnect_server();
        pygame.quit()
        sys.exit()

    def __loop(self):
        self.__clear()
        self.__screen.blit(self.__img_background, (0, 0))  # Draw background
        self.__board.disp(self.__screen, self.room)
        pygame.display.update()
        self.__board.next()

    def __clear(self):
            self.__screen.fill(colors.BLACK)  # Fill background

if __name__ == "__main__":
    Main()
