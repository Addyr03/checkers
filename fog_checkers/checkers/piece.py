import pygame
from pygame import Color
from .constants import white,black,square_size,grey 

class Piece:
        PADDING = 10
        OUTLINE = 2

    def __init__ (self,row,col,color):
        self.row = row
        self.col = col
        self.color = Color
        self.king = False

        if self.color == black:
            self.direction = -1
        else: 
            self.direction = 1

        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = square_size * self.col + square_size // 2
        self.x = square_size * self.row + square_size // 2

    def make_king(self):
        self.king = True

    def draw(self, window):
        radius = square_size // 2 - self.PADDING 
        ptgame.draw.circle (window, grey,(self.x,self.y), radius + self.OUTLINE)
        pygame.draw.circle (window, self.color,(self.x,self.y), radius)

    def __repr__ (self):
        return str(self.color)