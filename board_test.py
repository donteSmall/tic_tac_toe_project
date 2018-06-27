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
        self.board.mark(0, 'x')
        self.board.mark(1, 'x')
        self.board.mark(2, 'x')
        self.assertFalse(self.board.is_empty_at(0))
        self.assertFalse(self.board.is_empty_at(1))
        self.assertFalse(self.board.is_empty_at(2))

    def test_a_board_with_three_of_the_same_symbol_in_the_second_row_has_a_winner(self):
        self.board.mark(3, 'x')
        self.board.mark(4, 'x')
        self.board.mark(5, 'x')
        self.assertFalse(self.board.is_empty_at(3))
        self.assertFalse(self.board.is_empty_at(4))
        self.assertFalse(self.board.is_empty_at(5))


    def test_a_board_with_three_of_the_same_symbol_in_the_third_row_has_a_winner(self):
        self.board.mark(6, 'x')
        self.board.mark(7, 'x')
        self.board.mark(8, 'x')
        self.assertFalse(self.board.is_empty_at(6))
        self.assertFalse(self.board.is_empty_at(7))
        self.assertFalse(self.board.is_empty_at(8))

    def test_a_board_with_three_of_the_same_symbol_has_a_winner(self):
        self.board.is_winner_of_board(0,'x')
        self.board.is_winner_of_board(1,'x')
        self.board.is_winner_of_board(2,'x')



    # do one for second row, third row
    # for diagonals, columns

    #who's the winner?

    # display the board - return a string representation


if __name__ == '__main__':
    unittest.main()
