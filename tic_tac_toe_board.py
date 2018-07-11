class Board():
    def __init__(self):
        self.spaces = [None] * 9

    def is_empty_at(self, space):
        return self.spaces[space] is None

    def mark(self, space, symbol):
        if self.is_empty_at(space):
            self.spaces[space] = symbol
        else:
            raise ValueError("Invalid Move !")

    def __getitem__(self,space):
         return self.spaces[space]


    def is_winner_of_board(self):

        winningCombos = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [6, 4, 2]]

        for group in winningCombos:

            if self.spaces[group[0]] == self.spaces[group[1]] == self.spaces[group[2]]:
                if self.spaces[group[0]] == 'x':
                    print("X won board")

                elif self.spaces[group[0]] == 'o':

                    print("O won board")

        return True


    def draw(foo):
        ttt_board = self.board
        print("-------        ")
        print("|{}|{}|{}| (1,2,3)".format(ttt_board[0], ttt_board[1], ttt_board[2]))
        print("|{}|{}|{}| (4,5,6)".format(ttt_board[3], ttt_board[4], ttt_board[5]))
        print("|{}|{}|{}| (7,8,9)".format(ttt_board[6], ttt_board[7], ttt_board[8]))
        print("-------        ")


        return draw()
