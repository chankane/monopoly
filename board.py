import pygame
from pygame.locals import *
import settings
import colors
import grid


class Board:
    back_ground_color = colors.GREEN
    __GRIDS = None

    @classmethod
    def __init_grids(cls):
        cls.__GRIDS = grid.calc_pos_of_grids()

    def __init__(self):
        Board.__init_grids()
        self.__size = min(settings.SCREEN_SIZE)
        self.__index = 0

    def disp(self, screen, room):
        size = min(settings.SCREEN_SIZE)
        for e in Board.__GRIDS:
            pygame.draw.rect(
                screen,
                colors.RED,
                Rect(size * e[0], size * e[1], 3, 3), 3
            )
        room.disp(screen, size, (Board.__GRIDS))

    def next(self):
        self.__index = (self.__index + 1) % len(Board.__GRIDS)