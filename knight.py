from piece import Piece


class Knight(Piece):
    
    def is_valid_move(self, start_position, end_position, board):
        start_x, start_y = start_position
        end_x, end_y = end_position
