import pygame
from .constants import black, rows,white, square_size, cols,rows 
from .piece import Piece
class Board:
    def __init__(self):
        self.board = [[]]
        self.selected_piece = None 
        self.black_left = self.white_left = 12
        self.black_kings = self.white_kings = 0
        self.create_board()


    def draw_squares(self, win):
        win.fill(black)
        for row in range(rows):
            for col in range(row % 2,rows,2):
                pygame.draw.rect(win,white,(row* square_size, col * square_size, square_size, square_size))

    def create_board(self):
        for row in range (rows):
            self.board.append([])
            for col in range (cols):
                if col % 2 == ((row+1) % 2 ):
                    if row < 3 :
                        self.board[row].append(Piece,(row,col, white))
                    elif row > 4 :
                        self.board [row].append(Piece(row,col,black))
                else:
                    self.board [row].append(0)
            else:
                self.board [row].append(0)

    def draw (self,win):
        self.draw_squares(win)
        for row in range(rows):
            for col in range(cols):
                piece= self.board[row][col]
                if piece != 0:
                    piece.draw (win)