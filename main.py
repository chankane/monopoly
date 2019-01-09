import pygame
import sys  # For exit()
import settings
import colors
from board import Board
from resource import Resource


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

    def __init__(self):
        pygame.init()
        pygame.display.set_caption(settings.TITLE)
        self.__screen = pygame.display.set_mode(settings.SCREEN_SIZE)
        self.__board = Board()
        #self.__resource = self.__load()

        while not Main.__has_exit():
            self.__loop()
            pygame.time.Clock().tick(settings.FPS)

        pygame.quit()
        sys.exit()

    #def __load(self):
        #return Resource.img_background

    def __loop(self):
        self.__clear()
        #screen.blit(Resource.IMG_BACKGROUND, (0, 0))  # Draw background
        self.__board.disp(self.__screen)
        pygame.display.update()
        self.__board.next()

    def __clear(self):
            self.__screen.fill(colors.BLACK)  # Fill background


if __name__ == "__main__":
    Main()
