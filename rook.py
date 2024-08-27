from piece import Piece

class Rook(Piece):

    def is_valid_move(self, start_position, end_position, board):
        start_x, start_y = start_position
        end_x, end_y = end_position
        
        #Movimiento línea recta
        if start_x != end_x and start_y != end_y:
            return False