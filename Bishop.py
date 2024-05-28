import pygame
from Piece import Piece


class Bishop(Piece):
    def __init__(self, board, column, row, isWhite):
        super().__init__(board, column, row, isWhite=isWhite, name="Bishop")
        self.xPos = column * board.tileSize
        self.yPos = row * board.tileSize

        self.sprite = self.get_bishop_sprite(isWhite)

    def get_bishop_sprite(self, isWhite):
        y = 0 if isWhite else self.sheetScale
        sprite = self.sheet.subsurface((2 * self.sheetScale, y, self.sheetScale, self.sheetScale))
        return pygame.transform.smoothscale(sprite, (self.board.tileSize, self.board.tileSize))

    def is_valid_movement(self, column, row):
        return abs(self.column - column) == abs(self.row - row)

    def move_collides_with_piece(self, column, row):
        # Up-left diagonal
        if self.column > column and self.row > row:
            for i in range(1, abs(self.column - column)):
                if self.board.get_piece(self.column - i, self.row - i) is not None:
                    return True
        # Up-right diagonal
        if self.column < column and self.row > row:
            for i in range(1, abs(self.column - column)):
                if self.board.get_piece(self.column + i, self.row - i) is not None:
                    return True
        # Down-left diagonal
        if self.column > column and self.row < row:
            for i in range(1, abs(self.column - column)):
                if self.board.get_piece(self.column - i, self.row + i) is not None:
                    return True
        # Down-right diagonal
        if self.column < column and self.row < row:
            for i in range(1, abs(self.column - column)):
                if self.board.get_piece(self.column + i, self.row + i) is not None:
                    return True
        return False
