"""
This file contains the configuration of the MCTS algorithm.

Attributes
----------
ITERATION: int
    the number of iterations
EXPLORATION: float
    the exploration parameter
"""
import torch

# MCTS configuration
ITERATION = 500
EXPLORATION = 1.414

# Game configuration
ROW = 6
COLUMN = 7

# NN configuration
BATCH_SIZE = 10
EPOCHS = 1000
LEARNING_RATE = 5e-4
ITERATION_PER_EPOCH = 500
NUMBER_OF_GAMES = 10
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
MODEL_PATH = "model.pth"
