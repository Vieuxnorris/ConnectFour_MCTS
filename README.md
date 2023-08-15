# ConnectFour_MCTS
Integration of the monte-carlo algorithm with a search tree (MCTS) for the ConnectFour game

## Description
This project is a simple implementation of the Monte-Carlo algorithm with a search tree (MCTS) for the ConnectFour game. The game is played by two players, one after the other, on a 6x7 grid. The goal is to align 4 pieces of the same color horizontally, vertically or diagonally. The first player to do so wins the game. The game is played by two players, one after the other, on a 6x7 grid. The goal is to align 4 pieces of the same color horizontally, vertically or diagonally. The first player to do so wins the game. The game is played by two players, one after the other, on a 6x7 grid. The goal is to align 4 pieces of the same color horizontally, vertically or diagonally. The first player to do so wins the game.

## Installation
To install the project, you can clone the repository and then install the dependencies with the following command:
```
pip install -r requirements.txt
```

## Usage
To launch the game, you can run the following command:
```
python main.py
```
For change the parameters of the game, you can modify the file `config.py`.

## Project structure
The project is structured as follows:
- `main.py`: main file to launch the game
- `config.py`: file containing the parameters of the game
- `game.py`: file containing the class of the game
- `monte_carlo.py`: file containing the class of the MCTS algorithm
- `node.py`: file containing the class of the node of the search tree