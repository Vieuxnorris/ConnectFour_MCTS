class Node:
    """
    A node for the MCTS tree.

    :param state: the state of the game
    :param parent: the parent node
    """
    def __init__(self, state, parent=None):
        """
        Create a new node for the MCTS tree.

        :param state: the state of the game
        :param parent: the parent node
        """
        self.visits = 1
        self.reward = 0.0
        self.state = state
        self.children = []
        self.children_move = []
        self.parent = parent

    def add_child(self, child_state, move):
        """
        Add a child node to the tree.

        :param child_state: the state of the child node
        :param move: the move played to reach the child node
        """
        child = Node(child_state, self)
        self.children.append(child)
        self.children_move.append(move)

    def is_terminal(self):
        """
        Check if the node is terminal.

        :return: True if the node is terminal, False otherwise
        """
        return self.state.is_over()

    def update(self, reward):
        """
        Update the reward and visit count of the node.

        :param reward: the reward to add
        """
        self.reward += reward
        self.visits += 1

    def fully_explored(self):
        """
        Check if all the children of the node have been explored.

        :return: True if all the children have been explored, False otherwise
        """
        if len(self.children) == len(self.state.legal_moves()):
            return True
        return False
