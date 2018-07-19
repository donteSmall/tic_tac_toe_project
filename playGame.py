import unittest
from tic_tac_toe_board import Board



class playGame(object):

    def __init__(self):
        self.board = Board()

    def prompt_player(self):
         name = raw_input("Hello what's your name? ")
         while (name == "" or name == None):
             name = raw_input("What is your name? ")

         if (name != "" or None):
             print("Your name is :", name)
             type(name)
         else:
            print("Invalid input !! ")


    def pick_a_game_symbol(self):
         symbol= raw_input("What Player goes first: X or O ?")
         while not (symbol == 'X'.lower() or symbol =='O'.lower()):
             symbol = raw_input("What Player goes first: X or O ?")
             print("Great you picked : ",symbol)

         if symbol== "x".upper().lower():
             print("{Player_1} is X and Player_2 is O")
         else:
            print("{Player_1} : O and {Player_2} is X")




    def mark_an_empty_space_with_player_symbol(self,board):
        while True:
            try:
                indx = int(raw_input('Choose number input 1-9 '))
                if indx in range(0, 8) and board.is_empty_at(indx):
                    #board.mark(indx, symbol)
                    return indx
            except ValueError:
                pass

    def start_game(self):
        players = self.pick_a_game_symbol() # X or O
        player_one = 'x'


        while True:
            #import pdb; pdb.set_trace()

            indx = self.mark_an_empty_space_with_player_symbol(self.board)

            if player_one == "x":
                player_one= "O"
            else:
                player_one = "X"

            self.board[indx] = player_one
            print(self.board.draw())

            if self.board.is_there_a_winner():
                print('Congratulations ! You have won the game!')
            

            elif not [space for space in self.board if space is None]:
                    print('Congratulations ! The game is a tie!')

            player_one= "X" if player_one == "X" else "O"






a =playGame()
a.start_game()
# a.mark_an_empty_space_with_player_symbol(board)
#
# print(a.mark_an_empty_space_with_player_symbol(board))
