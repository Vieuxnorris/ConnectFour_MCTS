import copy
import numpy as np


class ConnectFour(object):
    """
    Connect Four game.

    The board is represented by a 6x7 numpy array.
    0 means empty, 1 means player 1, -1 means player 2.
    """

    def __init__(self):
        """Initialize the game"""
        self.turn = 1
        self.win = 0
        self.board = np.zeros((6, 7), dtype=np.int8)
        self.last_move = []

    def reset_game(self):
        """Reset the game"""
        self.turn = 1
        self.win = 0
        self.board = np.zeros((6, 7), dtype=np.int8)
        self.last_move = []

    def copy(self):
        """Copy the game"""
        return copy.deepcopy(self)

    def check_win(self):
        """Check if there is a winner"""
        # Check horizontal
        for i in range(6):
            for j in range(4):
                if (
                    self.board[i, j]
                    == self.board[i, j + 1]
                    == self.board[i, j + 2]
                    == self.board[i, j + 3]
                    != 0
                ):
                    return self.board[i, j]
        # Check vertical
        for i in range(3):
            for j in range(7):
                if (
                    self.board[i, j]
                    == self.board[i + 1, j]
                    == self.board[i + 2, j]
                    == self.board[i + 3, j]
                    != 0
                ):
                    return self.board[i, j]
        # Check diagonal
        for i in range(3):
            for j in range(4):
                if (
                    self.board[i, j]
                    == self.board[i + 1, j + 1]
                    == self.board[i + 2, j + 2]
                    == self.board[i + 3, j + 3]
                    != 0
                ):
                    return self.board[i, j]
        for i in range(3):
            for j in range(3, 7):
                if (
                    self.board[i, j]
                    == self.board[i + 1, j - 1]
                    == self.board[i + 2, j - 2]
                    == self.board[i + 3, j - 3]
                    != 0
                ):
                    return self.board[i, j]
        return 0

    def legal_moves(self):
        """Return the legal moves"""
        return [i for i in range(7) if self.board[0][i] == 0]

    def play(self, move):
        """Play a move"""
        if move not in self.legal_moves():
            raise ValueError("Illegal move")
        for i in range(5, -1, -1):
            if self.board[i][move] == 0:
                self.board[i][move] = self.turn
                self.last_move = [i, move]
                break
        self.turn *= -1
        self.win = self.check_win()
        return self.win

    def is_over(self):
        """Check if the game is over"""
        return self.win != 0 or len(self.legal_moves()) == 0

    def print_board(self):
        """Print the board"""
        print(self.board)
