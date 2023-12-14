import networkx as nx
import matplotlib.pyplot as plt
from Board import Board
from State import State

class DFS1:
    def __init__(self, board: Board) -> None:
        # Your existing initialization code
        self.board = board
        self.num_of_rows = board.rows
        self.num_of_cols = board.cols
        self.visited = [[False for _ in range(board.cols)] for _ in range(board.rows)]
        self.initial_state = board.get_initial_position()
        self.parents = [[(i, j) for j in range(board.cols)] for i in range(board.rows)]
        self.distance = [[0 for _ in range(board.cols)] for _ in range(board.rows)]
        self.dfs_tree = nx.Graph()  # Initialize an empty graph for the DFS tree

    def dfs(self, state: State, distance):
        r = state.row  # row
        c = state.col  # col
        self.visited[r][c] = True
        self.distance[r][c] = distance

        # Add node to the DFS tree
        parent_row, parent_col = self.parents[r][c]
        if (parent_row, parent_col) != (r, c):
            self.dfs_tree.add_edge((parent_row, parent_col), (r, c))

        suc = state.successor()
        for s in suc:
            if not self.visited[s.row][s.col]:
                self.parents[s.row][s.col] = (r, c)
                self.dfs(s, distance + 1)

    def plot_dfs_tree(self):
        # Plot the DFS tree using NetworkX and Matplotlib
        pos = nx.spring_layout(self.dfs_tree)
        nx.draw(self.dfs_tree, pos, with_labels=True, node_size=500, font_weight='bold')
        plt.show()

    # Other methods in your DFS class remain the same...
