from game import ConnectFour
from monte_carlo import MonteCarlo
from node import Node

if __name__ == "__main__":
    """
    Play a game of Connect Four against the Monte Carlo Tree Search algorithm.

    The algorithm is initialized with 10000 iterations and an exploration parameter of 1.414.
    """
    game = ConnectFour()

    while not game.is_over():
        if game.turn == 1:
            player_move = int(input("Player 1 move: "))
            game.play(player_move)
        else:
            root = Node(game)
            monte_carlo = MonteCarlo(iteration=10000)
            best_child = monte_carlo.search(root)
            game.play(best_child)

        game.print_board()
        print(" ")

    if game.win == 0:
        print("Draw")
    else:
        print("Player {} wins".format(game.win))
