import pygame
import os


class Piece:
    def __init__(self, board, column=0, row=0, value=0, isWhite=True, name=""):
        self.board = board
        self.column = column
        self.row = row
        self.value = value
        self.isWhite = isWhite
        self.name = name

        self.xPos = self.column * self.board.tileSize
        self.yPos = self.row * self.board.tileSize
        self.isFirstMove = True

        self.sheet = self.load_image("pieces.png")
        self.sheetScale = self.sheet.get_width() // 6
        self.sprite = self.get_sprite()

    def load_image(self, filename):
        try:
            filepath = os.path.join(os.path.dirname(__file__), filename)
            image = pygame.image.load(filepath)
            return image
        except pygame.error as e:
            print(f"Cannot load image: {filename}")
            raise SystemExit(e)

    def get_sprite(self):
        # This method needs to be implemented to extract the correct sprite from the sheet.
        # As an example, we'll just return a part of the sheet.
        return self.sheet.subsurface((0, 0, self.sheetScale, self.sheetScale))

    def is_valid_movement(self, column, row):
        return True

    def move_collides_with_piece(self, column, row):
        return False

    def paint(self, screen):
        screen.blit(self.sprite, (self.xPos, self.yPos))


# Example subclasses for different pieces
class Pawn(Piece):
    def __init__(self, board, column, row, isWhite):
        super().__init__(board, column, row, value=1, isWhite=isWhite, name="Pawn")


class Knight(Piece):
    def __init__(self, board, column, row, isWhite):
        super().__init__(board, column, row, value=3, isWhite=isWhite, name="Knight")


class Bishop(Piece):
    def __init__(self, board, column, row, isWhite):
        super().__init__(board, column, row, value=3, isWhite=isWhite, name="Bishop")


class Rook(Piece):
    def __init__(self, board, column, row, isWhite):
        super().__init__(board, column, row, value=5, isWhite=isWhite, name="Rook")


class Queen(Piece):
    def __init__(self, board, column, row, isWhite):
        super().__init__(board, column, row, value=9, isWhite=isWhite, name="Queen")


class King(Piece):
    def __init__(self, board, column, row, isWhite):
        super().__init__(board, column, row, value=0, isWhite=isWhite, name="King")
