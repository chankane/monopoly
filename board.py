import pygame
from pygame.locals import *
import settings
import colors


class Board:
    back_ground_color = colors.GREEN

    def __init__(self):
        self.__size = min(settings.SCREEN_SIZE)

    def disp(self, screen):
        pygame.draw.rect(screen, Board.back_ground_color, Rect(10, 10, 80, 50), 5)


