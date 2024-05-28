import pygame
from Piece import Piece


class Queen(Piece):
    def __init__(self, board, column, row, isWhite):
        super().__init__(board, column, row, isWhite=isWhite, name="Queen")
        self.xPos = column * board.tileSize
        self.yPos = row * board.tileSize

        self.sprite = self.get_queen_sprite(isWhite)

    def get_queen_sprite(self, isWhite):
        y = 0 if isWhite else self.sheetScale
        sprite = self.sheet.subsurface((self.sheetScale, y, self.sheetScale, self.sheetScale))
        return pygame.transform.smoothscale(sprite, (self.board.tileSize, self.board.tileSize))

    def is_valid_movement(self, column, row):
        return self.column == column or self.row == row or abs(self.column - column) == abs(self.row - row)

    def move_collides_with_piece(self, column, row):
        if self.column == column or self.row == row:
            # Horizontal or vertical movement
            if self.column > column:  # left
                for c in range(self.column - 1, column, -1):
                    if self.board.get_piece(c, self.row) is not None:
                        return True
            elif self.column < column:  # right
                for c in range(self.column + 1, column):
                    if self.board.get_piece(c, self.row) is not None:
                        return True
            elif self.row > row:  # up
                for r in range(self.row - 1, row, -1):
                    if self.board.get_piece(self.column, r) is not None:
                        return True
            elif self.row < row:  # down
                for r in range(self.row + 1, row):
                    if self.board.get_piece(self.column, r) is not None:
                        return True
        else:
            # Diagonal movement
            if self.column > column and self.row > row:  # up-left diagonal
                for i in range(1, abs(self.column - column)):
                    if self.board.get_piece(self.column - i, self.row - i) is not None:
                        return True
            elif self.column < column and self.row > row:  # up-right diagonal
                for i in range(1, abs(self.column - column)):
                    if self.board.get_piece(self.column + i, self.row - i) is not None:
                        return True
            elif self.column > column and self.row < row:  # down-left diagonal
                for i in range(1, abs(self.column - column)):
                    if self.board.get_piece(self.column - i, self.row + i) is not None:
                        return True
            elif self.column < column and self.row < row:  # down-right diagonal
                for i in range(1, abs(self.column - column)):
                    if self.board.get_piece(self.column + i, self.row + i) is not None:
                        return True
        return False
