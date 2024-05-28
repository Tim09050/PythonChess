import pygame
from Piece import Piece


class King(Piece):
    def __init__(self, board, column, row, isWhite):
        super().__init__(board, column, row, isWhite=isWhite, name="King")
        self.xPos = column * board.tileSize
        self.yPos = row * board.tileSize

        self.sprite = self.get_king_sprite(isWhite)

    def get_king_sprite(self, isWhite):
        y = 0 if isWhite else self.sheetScale
        sprite = self.sheet.subsurface((0, y, self.sheetScale, self.sheetScale))
        return pygame.transform.smoothscale(sprite, (self.board.tileSize, self.board.tileSize))

    def is_valid_movement(self, column, row):
        return abs((column - self.column) * (row - self.row)) == 1 or abs(column - self.column) + abs(row - self.row) == 1
    