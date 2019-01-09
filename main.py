import pygame
import sys  # For exit()
import settings
import colors
from board import Board
from socketClient import Socket 

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
        size = img.get_size()
        print(size)
        size = (min(settings.SCREEN_SIZE), min(settings.SCREEN_SIZE))
        print(size)
        img = pygame.transform.scale(img, size)
        return img

    def __init__(self):
        pygame.init()
        pygame.display.set_caption(settings.TITLE)
        self.__screen = pygame.display.set_mode(settings.SCREEN_SIZE)
        self.__img_background = self.__load_img_background(settings.IMG_BACKGROUND)
        self.__board = Board()
        Socket.connectServer();

        while not Main.__has_exit():
            self.__loop()
            pygame.time.Clock().tick(settings.FPS)

        Socket.disconnectServer();
        pygame.quit()
        sys.exit()

    def __loop(self):
        self.__clear()
        self.__screen.blit(self.__img_background, (0, 0))  # Draw background
        self.__board.disp(self.__screen)
        pygame.display.update()
        self.__board.next()

    def __clear(self):
            self.__screen.fill(colors.BLACK)  # Fill background

if __name__ == "__main__":
    Main()
