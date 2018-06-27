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



        #find out if someone's has won a ba
    def is_winner_of_board(self,space,symbol):
        if self.spaces[space]== 'x':
            print("Player" + symbol + "at"  + space + " has won the board")
        else:
            self.spaces[space]='o'
            print("Player" + symbol + "at"  + space + " has won the board")



    def draw():
        # initialize an empty board
        board = ""

        for i in range(5):
            if i%2 == 0:
                 board += "|    " * 4
            else:
                board += " --- " * 3
            board += "\n"

        print(board)

    draw()
