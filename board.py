from rook import Rook
from pawn import Pawn
from knight import Knight
from queen import Queen
from king import King
from bishop import Bishop

class Board:
    def __init__(self):

        self.__positions__ = []

        for _ in range(8):
            col = []
            for _ in range(8):
                col.append(None)
            self.__positions__.append(col)

        self.__positions__[0][0] = Rook("BLACK") # Black
        self.__positions__[0][7] = Rook("BLACK") # Black
        self.__positions__[7][7] = Rook("WHITE") # White
        self.__positions__[7][0] = Rook("WHITE") # White

        #caballos
        self.__positions__[0][1] = Knight("BLACK")  # Black
        self.__positions__[0][6] = Knight("BLACK")  # Black
        self.__positions__[7][1] = Knight("WHITE")  # White
        self.__positions__[7][6] = Knight("WHITE")  # White

        #alfiles
        self.__positions__[0][2] = Bishop("BLACK")  # Black
        self.__positions__[0][5] = Bishop("BLACK")  # Black
        self.__positions__[7][2] = Bishop("WHITE")  # White
        self.__positions__[7][5] = Bishop("WHITE")  # White

        #reinas
        self.__positions__[0][3] = Queen("BLACK")  # Black
        self.__positions__[7][3] = Queen("WHITE")  # White

        #reyes
        self.__positions__[0][4] = King("BLACK")  # Black
        self.__positions__[7][4] = King("WHITE")  # White

        #peones
        for i in range(8):
            self.__positions__[1][i] = Pawn("BLACK")  # Black
            self.__positions__[6][i] = Pawn("WHITE")  # White

class MovePiece:
    
    def __init__(self, board):
        self.board = board

    def move_piece(self, start_position, end_position):
        piece = self.board.get_piece(start_position[0], start_position[1])

        if piece is None:
            print("No hay ninguna pieza en la posición inicial")
            return
        
        
        
        
        


