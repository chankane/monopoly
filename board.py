import pygame
from pygame.locals import *
import settings
import colors


class Board:
    back_ground_color = colors.GREEN
    line_depth = 3
    grids = (
        {"top_left": (11, 11), "size": (2, 2)},
        {"top_left": (10, 11), "size": (1, 2)},
        {"top_left": (9, 11), "size": (1, 2)},
        {"top_left": (8, 11), "size": (1, 2)},
        {"top_left": (7, 11), "size": (1, 2)},
        {"top_left": (6, 11), "size": (1, 2)},
        {"top_left": (5, 11), "size": (1, 2)},
        {"top_left": (4, 11), "size": (1, 2)},
        {"top_left": (3, 11), "size": (1, 2)},
        {"top_left": (2, 11), "size": (1, 2)},

        {"top_left": (0, 11), "size": (2, 2)},
        {"top_left": (0, 10), "size": (2, 1)},
        {"top_left": (0, 9), "size": (2, 1)},
        {"top_left": (0, 8), "size": (2, 1)},
        {"top_left": (0, 7), "size": (2, 1)},
        {"top_left": (0, 6), "size": (2, 1)},
        {"top_left": (0, 5), "size": (2, 1)},
        {"top_left": (0, 4), "size": (2, 1)},
        {"top_left": (0, 3), "size": (2, 1)},
        {"top_left": (0, 2), "size": (2, 1)},

        {"top_left": (0, 0), "size": (2, 2)},
        {"top_left": (2, 0), "size": (1, 2)},
        {"top_left": (3, 0), "size": (1, 2)},
        {"top_left": (4, 0), "size": (1, 2)},
        {"top_left": (5, 0), "size": (1, 2)},
        {"top_left": (6, 0), "size": (1, 2)},
        {"top_left": (7, 0), "size": (1, 2)},
        {"top_left": (8, 0), "size": (1, 2)},
        {"top_left": (9, 0), "size": (1, 2)},
        {"top_left": (10, 0), "size": (1, 2)},

        {"top_left": (11, 0), "size": (2, 2)},
        {"top_left": (11, 2), "size": (2, 1)},
        {"top_left": (11, 3), "size": (2, 1)},
        {"top_left": (11, 4), "size": (2, 1)},
        {"top_left": (11, 5), "size": (2, 1)},
        {"top_left": (11, 6), "size": (2, 1)},
        {"top_left": (11, 7), "size": (2, 1)},
        {"top_left": (11, 8), "size": (2, 1)},
        {"top_left": (11, 9), "size": (2, 1)},
        {"top_left": (11, 10), "size": (2, 1)},
    )

    def __init__(self):
        self.__size = min(settings.SCREEN_SIZE)

    def disp(self, screen):
        size = self.__size / 13
        for e in Board.grids:
            pygame.draw.rect(
                screen,
                Board.back_ground_color,
                Rect(size * e["top_left"][0], size * e["top_left"][1], size * e["size"][0], size * e["size"][1]), Board.line_depth
            )


