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

         self.board.mark(0,'x')
         self.board.mark(1,'x')
         self.board.mark(2,'x')
         self.assertTrue(self.board.is_there_a_winner())

    def test_a_board_with_three_of_the_same_symbol_in_the_second_row_has_a_winner(self):

         self.board.mark(3,'x')
         self.board.mark(4,'x')
         self.board.mark(5,'x')
         self.assertTrue(self.board.is_there_a_winner())
         

    def test_a_board_with_three_of_the_same_symbol_in_the_third_row_has_a_winner(self):

         self.board.mark(6,'x')
         self.board.mark(7,'x')
         self.board.mark(8,'x')
         self.assertTrue(self.board.is_there_a_winner())

    def test_a_board_with_three_of_the_same_symbol_in_first_col_has_a_winner(self):

        self.board.mark(0,'o')
        self.board.mark(3,'o')
        self.board.mark(6,'o')
        self.assertTrue(self.board.is_there_a_winner())

    def test_a_board_with_three_of_the_same_symbol_in_second_col_has_a_winner(self):


        self.board.mark(1,'o')
        self.board.mark(4,'o')
        self.board.mark(7,'o')
        self.assertTrue(self.board.is_there_a_winner())

    def test_a_board_with_three_of_the_same_symbol_in_third_cols_has_a_winner(self):


        self.board.mark(2,'o')
        self.board.mark(5,'o')
        self.board.mark(8,'o')
        self.assertTrue(self.board.is_there_a_winner())

    def test_a_board_with_three_of_the_same_symbol_win_by_diagonal_Left_to_right(self):

        self.board.mark(0,'o')
        self.board.mark(4,'o')
        self.board.mark(8,'o')
        self.assertTrue(self.board.is_there_a_winner())

    def test_a_board_with_three_of_the_same_symbol_win_by_diagonal_right_to_left(self):

      self.board.mark(6,'x')
      self.board.mark(4,'x')
      self.board.mark(2,'x')
      self.assertTrue(self.board.is_there_a_winner())

    def test_draw_returns_a_string_description_of_the_board(self):
        expected_board = """
-------
| | | |
-------
| | | |
-------
| | | |
-------
"""

        self.assertEquals(expected_board.strip(), self.board.draw())

    def test_draw_returns_a_string_description_of_a_marked_board(self):
        expected_board = """
-------
|x|x| |
-------
| | | |
-------
| | | |
-------
"""
        self.board.mark(0,'x')
        self.board.mark(1,'x')
        self.assertEquals(expected_board.strip(), self.board.draw())






















    # do one for second row, third row
    # for diagonals, columns

    #who's the winner?

    # display the board - return a string representation


if __name__ == '__main__':
    unittest.main()
