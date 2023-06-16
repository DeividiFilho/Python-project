from distutils.util import rfc822_escape


class TicTactoe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None 

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j+3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
        # moves = []
        #for (i, spot) in enumerate(self.board):
        #    if spot == ' ':
        #        moves.append(i)
        #return moves 

    def empty_square(self):
        return ' ' in self.board
    
    def num_empty_square(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] == letter

            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind +10) * 3]

        if all([spot == letter for spot in row]):
            return True

        col_ind = square % 3
        
def play(game, x_player, o_player, print_game = True):
    if print_game:
        game.print_board_nums()

    letter = 'X' 

    while game.empty_squares():
        if letter == '0':
            square = o_player.get_move(game)

        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + 'wins!')
            return letter