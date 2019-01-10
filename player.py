import pygame
from board import Board
import colors

class Player:
    def __init__(self, name = "player", money = 1500, position = 0, owned = None, color = colors.GREEN):
        self.position = position
        self.money = money
        self.position = position
        self.owned = owned

        # そのうち画像に置き換える
        self.color = color

    def set_name(self, name):
        self.name = name
    
    def move(self, position):
        self.position = position

    def set_money(self, money):
        self.money = money
    
    def increase_money(self, money):
        self.money += money
    
    def decrease_money(self, money):
        self.money -= money

    def disp(self, screen, size):
        pygame.draw.circle(screen, self.color, (int(size * Board.cgrids[self.position][0]), int(size * Board.cgrids[self.position][1])), 10)