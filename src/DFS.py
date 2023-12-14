from Board import Board
from State import State


class DFS:
    def __init__(self, board: Board) -> None:
        self.board = board
        self.num_of_rows = board.rows
        self.num_of_cols = board.cols
        self.visited = [[False for _ in range(
            board.cols)] for _ in range(board.rows)]
        self.initial_state = board.get_initial_position()
        self.parents = [[(i, j) for j in range(board.cols)]
                        for i in range(board.rows)]
        # can become a feature in state class
        self.distance = [[0 for _ in range(board.cols)]
                         for _ in range(board.rows)]

    def dfs(self, state: State, distance):
        r = state.row  # row
        c = state.col  # col
        self.visited[r][c] = True
        self.distance[r][c] = distance
        
        ######
        print(state.row, state.col)
        state.print()
        self.print()
        print('----------------------------')
        
        suc = state.successor()
        for s in suc:
            if self.visited[s.row][s.col] == False:
                self.parents[s.row][s.col] = (r, c)
                self.dfs(s, distance+1)

    def print(self):
        for i in self.parents:
            print(i)
        # print("Visited:",(str(self.visited[i])+"\n" for i in range(self.visited)))
        #for i in range(len(self.visited)):
         #   print(self.visited[i])
