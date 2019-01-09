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
        size = (min(settings.SCREEN_SIZE), min(settings.SCREEN_SIZE))
        img = pygame.transform.scale(img, size)
        return img
    
    @staticmethod
    def __load_img_dice(path):
        img = pygame.image.load(path).convert_alpha()
        size = (min(settings.DICE_SIZE), min(settings.DICE_SIZE))
        img = pygame.transform.scale(img, size)
        return img


    def __init__(self):
        pygame.init()
        pygame.display.set_caption(settings.TITLE)
        self.__screen = pygame.display.set_mode(settings.SCREEN_SIZE)
        self.__img_background = self.__load_img_background(settings.IMG_BACKGROUND)
        self.__img_dice = self.__load_img_dice(settings.IMG_DICE)
        self.diceRect = pygame.Rect(settings.DICE_POS, self.__img_dice.get_rect().size)
        self.__board = Board()
        Socket.connect_server()

        while not Main.__has_exit():
            self.__loop()
            pygame.time.Clock().tick(settings.FPS)

        Socket.disconnect_server()
        pygame.quit()
        sys.exit()

    def __loop(self):
        self.__clear()
        self.__screen.blit(self.__img_background, (0, 0))  # Draw background
        self.__screen.blit(self.__img_dice, settings.DICE_POS) # Draw dice
        self.__board.disp(self.__screen)
        pygame.display.update()
        
        if(pygame.mouse.get_pressed()[0] == 1):
                if self.diceRect.collidepoint(pygame.mouse.get_pos()):
                    print("push")
        self.__board.next()

    def __clear(self):
            self.__screen.fill(colors.BLACK)  # Fill background

if __name__ == "__main__":
    Main()
