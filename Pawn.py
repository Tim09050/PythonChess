import pygame
from Piece import Piece


class Pawn(Piece):
    def __init__(self, board, column, row, isWhite):
        super().__init__(board, column, row, isWhite=isWhite, name="Pawn")
        self.xPos = column * board.tileSize
        self.yPos = row * board.tileSize

        self.sprite = self.get_pawn_sprite(isWhite)

    def get_pawn_sprite(self, isWhite):
        y = 0 if isWhite else self.sheetScale
        sprite = self.sheet.subsurface((5 * self.sheetScale, y, self.sheetScale, self.sheetScale))
        return pygame.transform.smoothscale(sprite, (self.board.tileSize, self.board.tileSize))

    def is_valid_movement(self, column, row):
        colorIndex = 1 if self.isWhite else -1

        # Moving one forward
        if column == self.column and row == self.row - colorIndex and self.board.get_piece(column, row) is None:
            return True
        # Moving two forward on first move
        if self.isFirstMove and column == self.column and row == self.row - colorIndex * 2 and self.board.get_piece(column, row) is None and self.board.get_piece(column, row + colorIndex) is None:
            return True
        # Capture left
        if column == self.column - 1 and row == self.row - colorIndex and self.board.get_piece(column, row) is not None:
            return True
        # Capture right
        if column == self.column + 1 and row == self.row - colorIndex and self.board.get_piece(column, row) is not None:
            return True
        # En passant
        if self.board.get_tile_number(column, row) == self.board.enPassantTile and column == self.column - 1 and row == self.row - colorIndex and self.board.get_piece(column, row + colorIndex) is not None:
            return True
        if self.board.get_tile_number(column, row) == self.board.enPassantTile and column == self.column + 1 and row == self.row - colorIndex and self.board.get_piece(column, row + colorIndex) is not None:
            return True
        return False
