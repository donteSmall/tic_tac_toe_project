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

    def is_there_a_winner(self):
        winningCombos = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                        [0, 3, 6], [1, 4, 7], [2, 5, 8],
                        [0, 4, 8], [6, 4, 2]]

        for group in winningCombos:

            if self.spaces[group[0]] == self.spaces[group[1]] == self.spaces[group[2]]:
                return True
            elif:
                return False
            else :
                return None







    def has_a_winner(self):

        if self.spaces[space] == 'x':
            print "x has won this board"
        else:
            print "o has won this board"


    def draw(self):
        #ttt_board var could be changed to just self.spaces
        nones_to_spaces = [ " " if s is None else s for s in self.spaces]
        return """
-------
|{}|{}|{}|
-------
|{}|{}|{}|
-------
|{}|{}|{}|
-------
        """.strip().format(*nones_to_spaces)
