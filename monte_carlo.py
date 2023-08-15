import math
import random
import config
from typing import Optional

from game import ConnectFour
from node import Node


class MonteCarlo(object):
    """
    Monte Carlo Tree Search algorithm.

    Methods
    -------
    search(root: Node) -> int
        Search the best move from the root node.
    selection(node: Node, turn: int) -> (Node, int)
        Select the best node to expand.
    expansion(node: Node) -> Node
        Expand the node by adding a new child.
    simulation(state_init: ConnectFour, turn: int) -> float
        Simulate a random game from the initial state.
    backpropagation(node: Node, reward: float, turn: int) -> None
        Backpropagate the reward of the simulation to the root node.
    best_child(node: Node) -> Node
        Return the best child of the node.
    """
    def __init__(
        self, iteration: Optional[int] = config.INTERATION, exploration: Optional[float] = config.EXPLORATION
    ):
        """
        Initialize the Monte Carlo Tree Search algorithm.

        Parameters
        ----------
        iteration: the number of iterations
        exploration: the exploration parameter
        """
        self.iteration = iteration
        self.exploration = exploration

    def search(self, root: Node) -> int:
        """
        Search the best move from the root node.

        Parameters
        ----------
        root: the root node of the search tree

        Returns
        -------
        int: the best move
        """
        for _ in range(self.iteration):
            node, turn = self.selection(root, -1)
            reward = self.simulation(node.state, turn)
            self.backpropagation(node, reward, turn)

        ans = self.best_child(root)
        print(f"{[child.reward / child.visits for child in root.children]}")
        return ans.state.last_move[1]

    def selection(self, node: Node, turn: int) -> (Node, int):
        """
        Select the best node to expand.

        Parameters
        ----------
        node: the node to start the selection from
        turn: the turn of the player who played the move leading to this node

        Returns
        -------
        node: the node to expand
        turn: the turn of the player who played the move leading to this node
        """
        while not node.is_terminal():
            if not node.fully_explored():
                return self.expansion(node), -1 * turn
            else:
                node = self.best_child(node)
                turn *= -1

        return node, turn

    @staticmethod
    def expansion(node: Node) -> Node:
        """
        Expand the node by adding a new child.

        Parameters
        ----------
        node: the node to expand

        Returns
        -------
        node: the new child
        """
        free_cols = node.state.legal_moves()

        for col in free_cols:
            if col not in node.children_move:
                new_state = node.state.copy()
                new_state.play(col)
                node.add_child(new_state, col)
                break

        return node.children[-1]

    @staticmethod
    def simulation(state_init: ConnectFour, turn: int) -> float:
        """
        Simulate a random game from the initial state.

        Parameters
        ----------
        state_init: the initial state of the game
        turn: the turn of the player who played the move leading to this node

        Returns
        -------
        reward: the reward of the simulated game
        """
        state = state_init.copy()

        while not state.is_over():
            state.play(random.choice(state.legal_moves()))
            turn *= -1

        reward_bool = state.is_over()

        if reward_bool and turn == -1:
            reward = 1.0
        elif reward_bool and turn == 1:
            reward = -1.0
        else:
            reward = 0.0
        return reward

    @staticmethod
    def backpropagation(node: Node, reward: float, turn: int) -> None:
        """
        Backpropagate the reward of the simulation to the root node.

        Parameters
        ----------
        node: the node to start the backpropagation from
        reward: the reward of the simulation
        turn: the turn of the player who played the move leading to this node

        Returns
        -------
        none
        """
        while node is not None:
            node.visits += 1
            node.reward -= turn * reward
            node = node.parent
            turn *= -1

    def best_child(self, node: Node) -> Node:
        """
        Return the best child of the node.

        Parameters
        ----------
        node: the node to select the best child from

        Returns
        -------
        node: the best child
        """
        best_score = -float("inf")
        best_children = []

        for child in node.children:
            exploitation = child.reward / child.visits
            exploration = math.sqrt(math.log2(node.visits) / child.visits)
            score = exploitation + self.exploration * exploration

            if score == best_score:
                best_children.append(child)
            elif score > best_score:
                best_score = score
                best_children = [child]

        return random.choice(best_children)
