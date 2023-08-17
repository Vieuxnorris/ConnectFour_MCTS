from game import ConnectFour
from monte_carlo import MonteCarlo
from node import Node

if __name__ == "__main__":
    """
    Play a game of Connect Four against the computer.
    
    Parameters
    ----------
    none
    """
    game = ConnectFour()

    while not game.is_over():
        if game.turn == 1:
            player_move = int(input("Player 1 move: "))
            game.play(player_move)
        else:
            root = Node(game)
            monte_carlo = MonteCarlo()
            best_child, prob = monte_carlo.search(root)
            game.play(best_child)

        game.print_board()
        print(" ")

    if game.win == 0:
        print("Draw")
    else:
        print("Player {} wins".format(game.win))
