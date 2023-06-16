import math
import random
from idna import valid_label_length

from numpy import square 

class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass

class RandonComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())

class HumanPlayerr(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None

        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-9): ')
            
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True 
            except ValueError:
                print('Invalid square. Try again.')

        return val