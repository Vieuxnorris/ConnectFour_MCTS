import random
import math


class MonteCarlo(object):
    """
    Monte Carlo Tree Search algorithm.

    :param iteration: the number of iterations to perform
    :param exploration: the exploration parameter of the UCB formula
    """
    def __init__(self, iteration=1000, exploration=1.414):
        self.iteration = iteration
        self.exploration = exploration

    def search(self, root):
        """
        Search the best move from the current game state.

        :param root: the current game state
        :return: the best move to play
        """
        for _ in range(self.iteration):
            node, turn = self.selection(root, -1)
            reward = self.simulation(node.state, turn)
            self.backpropagation(node, reward, turn)

        ans = self.best_child(root)
        print(f"{[child.reward / child.visits for child in root.children]}")
        return ans.state.last_move[1]

    def selection(self, node, turn):
        """
        Select the best child of the node according to the UCB formula until a terminal node is reached.

        :param node: the node to start from
        :param turn: the turn of the player who played the move leading to this node
        :return: the selected node
        """
        while not node.is_terminal():
            if not node.fully_explored():
                return self.expansion(node), -1 * turn
            else:
                node = self.best_child(node)
                turn *= -1

        return node, turn

    def expansion(self, node):
        """
        Expand the node by adding a new child.

        :param node: the node to expand
        :return: the new child node
        """
        free_cols = node.state.legal_moves()

        for col in free_cols:
            if col not in node.children_move:
                new_state = node.state.copy()
                new_state.play(col)
                break

        node.add_child(new_state, col)
        return node.children[-1]

    def simulation(self, state_init, turn):
        """
        Simulate a random game from the initial state.

        :param state_init: the initial state of the game
        :return: the reward of the game
        """
        state = state_init.copy()

        while not state.is_over():
            state.play(random.choice(state.legal_moves()))
            turn *= -1

        reward_bool = state.is_over()

        if reward_bool and turn == -1:
            reward = 1
        elif reward_bool and turn == 1:
            reward = -1
        else:
            reward = 0
        return reward

    def backpropagation(self, node, reward, turn):
        """
        Update the node reward and visit count recursively.

        :param node: the node to update
        :param reward: the reward to propagate
        :param turn: the turn of the player who played the move leading to this node
        """
        while node != None:
            node.visits += 1
            node.reward -= turn * reward
            node = node.parent
            turn *= -1

    def best_child(self, node):
        """
        Select the child with the highest UCB score.

        :param node: the node whose children to consider
        :return: the child with the highest UCB score
        """
        best_score = -float("inf")
        best_children = []

        for child in node.children:
            exploitation = child.reward / child.visits
            exploration = math.sqrt(2.0 * math.log(node.visits) / float(child.visits))
            score = exploitation + self.exploration * exploration

            if score == best_score:
                best_children.append(child)
            elif score > best_score:
                best_score = score
                best_children = [child]

        return random.choice(best_children)
