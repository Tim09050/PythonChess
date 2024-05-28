import pygame
from Queen import Queen
from Rook import Rook
from Bishop import Bishop
from Knight import Knight
from King import King
from Pawn import Pawn
from Input import Input
from Move import Move


class Board:
    def __init__(self):
        self.tileSize = 75
        self.column = 8
        self.row = 8
        self.pieceList = []
        self.selectedPiece = None
        self.input = Input(self)
        self.enPassantTile = -1

        self.current_player = 'white'

        pygame.init()
        self.screen = pygame.display.set_mode((self.column * self.tileSize, self.row * self.tileSize))
        self.add_pieces()

    def get_piece(self, column, row):
        for piece in self.pieceList:
            if piece.column == column and piece.row == row:
                return piece
        return None

    def make_move(self, move):
        if move.piece.name == "Pawn":
            self.move_pawn(move)
        else:
            move.piece.column = move.newColumn
            move.piece.row = move.newRow

            move.piece.xPos = move.newColumn * self.tileSize
            move.piece.yPos = move.newRow * self.tileSize

            move.piece.isFirstMove = False

            self.capture(move.capture)


    def move_pawn(self, move):
        colorIndex = 1 if move.piece.isWhite else -1

        if self.get_tile_number(move.newColumn, move.newRow) == self.enPassantTile:
            move.capture = self.get_piece(move.newColumn, move.newRow + colorIndex)

        if abs(move.piece.row - move.newRow) == 2:
            self.enPassantTile = self.get_tile_number(move.newColumn, move.newRow + colorIndex)
        else:
            self.enPassantTile = -1

        colorIndex = 0 if move.piece.isWhite else 7
        if move.newRow == colorIndex:
            self.promotion(move)

        move.piece.column = move.newColumn
        move.piece.row = move.newRow

        move.piece.xPos = move.newColumn * self.tileSize
        move.piece.yPos = move.newRow * self.tileSize

        move.piece.isFirstMove = False

        self.capture(move.capture)

    def promotion(self, move):
        options = ["Queen", "Rook", "Bishop", "Knight"]
        choice = options[0]  # Default choice for now (e.g., can be made interactive with a GUI library like tkinter)

        if choice == "Queen":
            self.pieceList.append(Queen(self, move.newColumn, move.newRow, move.piece.isWhite))
        elif choice == "Rook":
            self.pieceList.append(Rook(self, move.newColumn, move.newRow, move.piece.isWhite))
        elif choice == "Bishop":
            self.pieceList.append(Bishop(self, move.newColumn, move.newRow, move.piece.isWhite))
        elif choice == "Knight":
            self.pieceList.append(Knight(self, move.newColumn, move.newRow, move.piece.isWhite))

        self.capture(move.piece)

    def capture(self, piece):
        if piece:
            self.pieceList.remove(piece)

    def is_valid_move(self, move):
        if self.same_team(move.piece, move.capture):
            return False
        if not move.piece.is_valid_movement(move.newColumn, move.newRow):
            return False
        if move.piece.move_collides_with_piece(move.newColumn, move.newRow):
            return False
        return True

    def same_team(self, firstPiece, secondPiece):
        if firstPiece is None or secondPiece is None:
            return False
        return firstPiece.isWhite == secondPiece.isWhite

    def get_tile_number(self, column, row):
        return row * self.row + column

    def add_pieces(self):
        for p in range(8):
            self.pieceList.append(Pawn(self, p, 1, False))
            self.pieceList.append(Pawn(self, p, 6, True))

        self.pieceList.append(Knight(self, 1, 0, False))
        self.pieceList.append(Knight(self, 6, 0, False))
        self.pieceList.append(Knight(self, 1, 7, True))
        self.pieceList.append(Knight(self, 6, 7, True))

        self.pieceList.append(Bishop(self, 2, 0, False))
        self.pieceList.append(Bishop(self, 5, 0, False))
        self.pieceList.append(Bishop(self, 2, 7, True))
        self.pieceList.append(Bishop(self, 5, 7, True))

        self.pieceList.append(Rook(self, 0, 0, False))
        self.pieceList.append(Rook(self, 7, 0, False))
        self.pieceList.append(Rook(self, 0, 7, True))
        self.pieceList.append(Rook(self, 7, 7, True))

        self.pieceList.append(Queen(self, 3, 0, False))
        self.pieceList.append(Queen(self, 3, 7, True))

        self.pieceList.append(King(self, 4, 0, False))
        self.pieceList.append(King(self, 4, 7, True))

    def paint_component(self):
        blue = (71, 117, 171)
        white = (214, 221, 229)
        for r in range(self.row):
            for c in range(self.column):
                color = white if (r + c) % 2 == 0 else blue
                pygame.draw.rect(self.screen, color,
                                 pygame.Rect(c * self.tileSize, r * self.tileSize, self.tileSize, self.tileSize))

        if self.selectedPiece:
            for r in range(self.row):
                for c in range(self.column):
                    if self.is_valid_move(Move(self, self.selectedPiece, c, r)):
                        color = (68, 179, 57, 190)
                        pygame.draw.rect(self.screen, color,
                                         pygame.Rect(c * self.tileSize, r * self.tileSize, self.tileSize,
                                                     self.tileSize))

        for piece in self.pieceList:
            piece.paint(self.screen)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                else:
                    self.input.handle_event(event)

            self.paint_component()
            pygame.display.flip()
        pygame.quit()
