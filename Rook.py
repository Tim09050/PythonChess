import pygame
from Piece import Piece


class Rook(Piece):
    def __init__(self, board, column, row, isWhite):
        super().__init__(board, column, row, isWhite=isWhite, name="Rook")
        self.xPos = column * board.tileSize
        self.yPos = row * board.tileSize

        self.sprite = self.get_rook_sprite(isWhite)

    def get_rook_sprite(self, isWhite):
        y = 0 if isWhite else self.sheetScale
        sprite = self.sheet.subsurface((4 * self.sheetScale, y, self.sheetScale, self.sheetScale))
        return pygame.transform.smoothscale(sprite, (self.board.tileSize, self.board.tileSize))

    def is_valid_movement(self, column, row):
        return self.column == column or self.row == row

    def move_collides_with_piece(self, column, row):
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
        return False
