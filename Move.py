class Move:
    def __init__(self, board, piece, newColumn, newRow):
        self.oldColumn = piece.column
        self.oldRow = piece.row
        self.newColumn = newColumn
        self.newRow = newRow

        self.piece = piece
        self.capture = board.get_piece(newColumn, newRow)
