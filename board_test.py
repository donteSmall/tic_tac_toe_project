import unittest
from tic_tac_toe_board import Board

class EmptyBoardTest(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_spaces_are_all_empty(self):
        for space in range(0, 9):
            self.assertTrue(self.board.is_empty_at(space))

    def test_a_marked_space_isnt_empty(self):
        self.board.mark(0, 'x')
        self.assertFalse(self.board.is_empty_at(0))

    def test_a_marked_space_cant_be_remarked(self):
        self.board.mark(0, 'x')
        with self.assertRaises(ValueError):
            self.board.mark(0, 'x')

    def test_a_board_with_three_of_the_same_symbol_in_the_first_row_has_a_winner(self):
         #First you need a board
         #Next you need to check if three of same symbol are in the first row
         # If so, Who has won
         # board = [['x','x','x'],[' ', ' ',' '], [' ',' ',' ']]
         # for i in board:
         if self.board[0] == self.board[1] == self.board[2]:
             print("Three of the same sybols are in the first row")

             self.assertTrue(self.board.is_winner_of_board())

    def test_a_board_with_three_of_the_same_symbol_in_cols_rows_has_a_winner(self):

        if (self.board[0]== self.board[3] == self.board[6]) or (self.board[1]== self.board[4] == self.board[7]) or\
        (self.board[2]== self.board[5] == self.board[8]) :
            self.assertTrue(self.board.is_winner_of_board())


    def test_a_board_with_three_of_the_same_symbol_in_the_diag_row_has_a_winner(self):

        if ((self.board[0] == self.board[4] == self.board[8] ) or (self.board[2] == self.board[4] ==self.board[6])):

            self.assertTrue(self.board.is_winner_of_board())






    # do one for second row, third row
    # for diagonals, columns

    #who's the winner?

    # display the board - return a string representation


if __name__ == '__main__':
    unittest.main()
