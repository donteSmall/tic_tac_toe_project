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
         board = self.board
         board.mark(0,'x')
         board.mark(1,'x')
         board.mark(2,'x')
         self.assertTrue(board.is_winner_of_board())

    def test_a_board_with_three_of_the_same_symbol_in_the_second_row_has_a_winner(self):
         second_row = self.board
         second_row.mark(3,'x')
         second_row.mark(4,'x')
         second_row.mark(5,'x')
         self.assertTrue(second_row.is_winner_of_board())

    def test_a_board_with_three_of_the_same_symbol_in_the_third_row_has_a_winner(self):
         third_row = self.board
         third_row.mark(6,'x')
         third_row.mark(7,'x')
         third_row.mark(8,'x')
         self.assertTrue(third_row.is_winner_of_board())

    def test_a_board_with_three_of_the_same_symbol_in_first_col_has_a_winner(self):
        first_cols = self.board
        first_cols.mark(0,'o')
        first_cols.mark(3,'o')
        first_cols.mark(6,'o')
        self.assertTrue(first_cols.is_winner_of_board())

    def test_a_board_with_three_of_the_same_symbol_in_second_col_has_a_winner(self):

        second_col_board = self.board
        second_col_board.mark(1,'o')
        second_col_board.mark(4,'o')
        second_col_board.mark(7,'o')
        self.assertTrue(second_col_board.is_winner_of_board())

    def test_a_board_with_three_of_the_same_symbol_in_third_cols_has_a_winner(self):

        third_col_board = self.board
        third_col_board.mark(2,'o')
        third_col_board.mark(5,'o')
        third_col_board.mark(8,'o')
        self.assertTrue(third_col_board.is_winner_of_board())
        self.draw()

    def test_a_board_with_three_of_the_same_symbol_win_by_diagonal_Left_to_right(self):
        win_by_diagonal_board = self.board
        win_by_diagonal_board.mark(0,'o')
        win_by_diagonal_board.mark(4,'o')
        win_by_diagonal_board.mark(8,'o')
        self.assertTrue(win_by_diagonal_board.is_winner_of_board())

    def test_a_board_with_three_of_the_same_symbol_win_by_diagonal_right_to_left(self):
      diagonal_right_to_left = self.board
      diagonal_right_to_left.mark(6,'x')
      diagonal_right_to_left.mark(4,'x')
      diagonal_right_to_left.mark(2,'x')
      self.assertTrue(diagonal_right_to_left.is_winner_of_board())

















    # do one for second row, third row
    # for diagonals, columns

    #who's the winner?

    # display the board - return a string representation


if __name__ == '__main__':
    unittest.main()
