from game import ConnectFour
from monte_carlo import MonteCarlo
from node import Node
from model import ConnectFourNN

import config
import torch
import torch.nn as nn
import torch.optim as optim


class Train:
    """
    Training session for the ConnectFour neural network model.

    Methods
    -------
    train() -> none
        Train the model.
    train_batch(train_data: list) -> none
        Train the model on a batch of data.
    """
    def __init__(self):
        """
        Create a new training session.
        """
        self.model = ConnectFourNN()
        self.optimizer = optim.Adam(self.model.parameters(), lr=config.LEARNING_RATE)
        self.loss = nn.MSELoss()
        self.mcts = MonteCarlo()

    def train(self):
        """
        Train the model.

        Returns
        -------
        none
        """
        train_data = []

        for episode in range(config.EPOCHS):
            game = ConnectFour()
            current_player = -game.turn

            while not game.is_over():
                root = Node(game)
                best_child, prob = self.mcts.search(root)
                train_data.append((game.board, current_player, prob))
                game.play(best_child)
                current_player = -game.turn

            if game.win == 0:
                print("Draw")
            else:
                print("Player {} wins".format(game.win))

            if episode % config.BATCH_SIZE == 0:
                self.train_batch(train_data)
                train_data = []

    def train_batch(self, train_data):
        """
        Train the model on a batch of data.

        Parameters
        ----------
        train_data: records of the game

        Returns
        -------
        none
        """
        self.model.train()
        for epoch in range(config.EPOCHS):
            batch_idx = 0
            for board, current_player, prob in train_data:
                board = torch.tensor(board, dtype=torch.float).view(-1, 42)
                prob = torch.tensor(prob, dtype=torch.float).view(-1, 7)
                self.optimizer.zero_grad()
                pi, v = self.model(board)
                loss = self.loss(pi, prob) + self.loss(
                    v, torch.tensor([current_player], dtype=torch.float)
                )
                loss.backward()
                self.optimizer.step()
                batch_idx += 1
                if batch_idx % config.BATCH_SIZE == 0:
                    print("Epoch: {}, Loss: {}".format(epoch, loss.item()))
                    self.model.save_model(config.MODEL_PATH)
                    return


if __name__ == "__main__":
    train = Train()
    train.train()
