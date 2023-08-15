import copy

import numpy as np


class ConnectFour(object):
    """
    A class used to represent a game of Connect Four.

    Methods
    -------
    reset_game() -> None
        Reset the game.
    copy() -> copy
        Return a copy of the game.
    check_win() -> int
        Check if the game is won.
    legal_moves() -> list
        Return the legal moves.
    play(move: int) -> int
        Play a move.
    is_over() -> bool
        Check if the game is over.
    print_board() -> None
        Print the board.
    """

    def __init__(self) -> None:
        """
        Create a new game.
        """
        self.turn = 1
        self.win = 0
        self.board = np.zeros((6, 7), dtype=np.int8)
        self.last_move = []

    def reset_game(self) -> None:
        """
        Reset the game.

        Returns
        -------
        none
        """
        self.turn = 1
        self.win = 0
        self.board = np.zeros((6, 7), dtype=np.int8)
        self.last_move = []

    def copy(self) -> copy:
        """
        Return a copy of the game.

        Returns
        -------
        copy: a copy of the game
        """
        return copy.deepcopy(self)

    def check_win(self) -> int:
        """
        Check if the game is won.

        Returns
        -------
        win: 1 if player 1 wins, -1 if player 2 wins, 0 otherwise
        """
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

    def legal_moves(self) -> list:
        """
        Return the legal moves.

        Returns
        -------
        legal_moves: a list of legal moves
        """
        return [i for i in range(7) if self.board[0][i] == 0]

    def play(self, move: int) -> int:
        """
        Play a move.

        Parameters
        ----------
        move: the move to play

        Returns
        -------
        win: 1 if player 1 wins, -1 if player 2 wins, 0 otherwise
        """
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

    def is_over(self) -> bool:
        """
        Check if the game is over.

        Returns
        -------
        bool: True if the game is over, False otherwise
        """
        return self.win != 0 or len(self.legal_moves()) == 0

    def print_board(self) -> None:
        """
        Print the board.

        Returns
        -------
        none
        """
        print(self.board)
