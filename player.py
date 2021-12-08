import math
import random 

class Player:
    def __init__(self, letter):
        #letter is x or o
        self.letter = letter

    # want all players to get their next move given a name 
    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        #get a random valid spot for the next move
        square = random.choice(game.available_moves())
        return square

class HumanPlayer (Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-9):')
            #check that this is correct value by trying to cast it to an integer
            #if it is not an int, print invalid 
            #if spot on the board is unavailable, print invalid
            try:
                val = int(square)
                if val not in game. available_moves():
                    raise ValueError
                valid_square = True 
            except ValueError:
                print('Invalid square. Try again.')
        return val
