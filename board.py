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

    cgrids = (
        (12, 12), (10.5, 12), (9.5, 12), (8.5, 12), (7.5, 12), (6.5, 12), (5.5, 12), (4.5, 12), (3.5, 12), (2.5, 12),
        (1, 12), (1, 10.5), (1, 9.5), (1, 8.5), (1, 7.5), (1, 6.5), (1, 5.5), (1, 4.5), (1, 3.5), (1, 2.5),
        (1, 1), (2.5, 1), (3.5, 1), (4.5, 1), (5.5, 1), (6.5, 1), (7.5, 1), (8.5, 1), (9.5, 1), (10.5, 1),
        (12, 1), (12, 2.5), (12, 3.5), (12, 4.5), (12, 5.5), (12, 6.5), (12, 7.5), (12, 8.5), (12, 9.5), (12, 10.5),
    )

    def __init__(self):
        self.__size = min(settings.SCREEN_SIZE)
        self.__index = 0

    def disp(self, screen):
        size = self.__size / 13
        for e in Board.grids:
            pygame.draw.rect(
                screen,
                Board.back_ground_color,
                Rect(size * e["top_left"][0], size * e["top_left"][1], size * e["size"][0], size * e["size"][1]), Board.line_depth
            )
        for e in Board.cgrids:
            pygame.draw.rect(
                screen,
                Board.back_ground_color,
                Rect(size * e[0], size * e[1], 1, 1), Board.line_depth
            )
        pygame.draw.circle(screen, Board.back_ground_color, (int(size * Board.cgrids[self.__index][0]), int(size * Board.cgrids[self.__index][1])), 20)

    def next(self):
        self.__index = (self.__index + 1) % len(Board.cgrids)