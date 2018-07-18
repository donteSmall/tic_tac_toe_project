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
             print "Your name is :", name
             type(name)
         else:
            print"Invalid input !! "


    def pick_a_game_symbol(self):
         symbol= raw_input("What Player goes first: X or O ?")
         while not (symbol == 'X'.lower() or symbol =='O'.lower()):
             symbol = raw_input("What Player goes first: X or O ?")
             print "Great you picked : ",symbol

         if symbol== "x".upper().lower():
             print "{Player_1} is X and Player_2 is O"
         else:
            print "{Player_1} : O and {Player_2} is X"




    def mark_an_empty_space_with_player_symbol(self,board):
        while True:
            try:
                indx = int(raw_input('Choose number input 1-9 '))
                if indx in range(1, 9) and board[position] == ' ':
                    return indx
            except ValueError:
                pass

    def start_game(self):
        board = self.board
        players = self.pick_a_game_symbol() # X or O
        player_one = 'x'
        player_two = 'o'

        while True:
            indx = self.mark_an_empty_space_with_player_symbol(board)
            board[indx] = player_one if "x" else "o"
            import pdb; pdb.set_trace()
            board.draw()
            if is_there_a_winner(board):
                print('Congratulations ! You have won the game!')

            if is_the_game_board_Full(board):
                print("There was a tie between both opponents")





a =playGame()
a.start_game()
# a.mark_an_empty_space_with_player_symbol(board)
#
# print(a.mark_an_empty_space_with_player_symbol(board))
