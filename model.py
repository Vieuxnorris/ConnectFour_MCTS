import torch
import torch.nn as nn
import torch.nn.functional as F

import config


class ConnectFourNN(nn.Module):
    """
    Neural network model for ConnectFour

    Methods
    -------
    forward(x: torch.Tensor) -> torch.Tensor
        Forward propagation of the neural network.
    predict(x: torch.Tensor) -> torch.Tensor
        Predict the value of the input state.
    save_model(path: str) -> None
        Save the model.
    load_model(path: str) -> None
        Load the model.
    """

    def __init__(self):
        """
        Create a new ConnectFour neural network model
        """
        super(ConnectFourNN, self).__init__()

        self.board_size = config.ROW * config.COLUMN
        self.action_size = config.COLUMN
        self.output_size = 1

        # ConnectFour is terminal game, so there is only one output = column index
        self.fc1 = nn.Linear(self.board_size, 64)
        self.fc2 = nn.Linear(64, 32)
        self.fc3 = nn.Linear(32, self.output_size)

    def forward(self, x):
        """
        Forward propagation of the neural network

        x: input state
        """
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.relu(self.fc3(x))

        return F.softmax(x, dim=1), torch.tanh(x)

    def predict(self, x):
        """
        Predict the value of the input state

        x: input state
        """
        return self.forward(x)

    def save_model(self, path):
        """
        Save the model

        path: path to save the model
        """
        torch.save(self.state_dict(), path)

    def load_model(self, path):
        """
        Load the model

        path: path to load the model
        """
        self.load_state_dict(torch.load(path))
