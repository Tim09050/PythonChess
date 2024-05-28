import pygame
from Move import Move


class Input:
    def __init__(self, board):
        self.board = board

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.mouse_pressed(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            self.mouse_released(event)
        elif event.type == pygame.MOUSEMOTION and event.buttons[0]:
            self.mouse_dragged(event)

    def mouse_pressed(self, event):
        x, y = event.pos
        column = x // self.board.tileSize
        row = y // self.board.tileSize

        pieceXY = self.board.get_piece(column, row)
        if pieceXY:
            self.board.selectedPiece = pieceXY

    def mouse_released(self, event):
        x, y = event.pos
        column = x // self.board.tileSize
        row = y // self.board.tileSize
        if self.board.selectedPiece:
            move = Move(self.board, self.board.selectedPiece, column, row)
            if self.board.is_valid_move(move):
                self.board.make_move(move)
            else:
                self.board.selectedPiece.xPos = self.board.selectedPiece.column * self.board.tileSize
                self.board.selectedPiece.yPos = self.board.selectedPiece.row * self.board.tileSize

        self.board.selectedPiece = None
        self.board.paint_component()

    def mouse_dragged(self, event):
        if self.board.selectedPiece:
            x, y = event.pos
            self.board.selectedPiece.xPos = x - self.board.tileSize // 2
            self.board.selectedPiece.yPos = y - self.board.tileSize // 2

            self.board.paint_component()
