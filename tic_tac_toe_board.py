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

        #find out if someone's has won a ba
    # def is_winner_of_board(self, board):
    #     for i  in range(len(board)
    #     if board[i]== 'x':
    #         print("Player" + symbol + "at"  + space + " has won the board")
    #     else:
    #         print("Player" + symbol + "at"  + space + " has won the board")
    #
    def is_winner_of_board(self):

        winningCombos = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [6, 4, 2]]

        for group in winningCombos:

            if self.spaces[group[0]] == self.spaces[group[1]] == self.spaces[group[2]]:
                if self.spaces[group[0]] == 'x':
                    return 0

                elif self.spaces[group[0]] == 'o':

                    return -1


        return 1
