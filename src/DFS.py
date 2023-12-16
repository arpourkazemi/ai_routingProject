import time
import queue
from State import State
from Board import Board
from Utilities import print_yellow, print_red, print_purple, print_danger


class DFS:
    def __init__(self, s: State):
        print("\033[33mDFS started...\n\033[m")
        self.init_state = s
        self.board = s.board
        self.num_targets = s.board.num_targets
        self.visited = [s]
        start = time.time()
        self.dfs()
        end = time.time()
        print_red("Time spent for DFS: " + str(round(end - start, 3)))
        print("---------------------------------------------------")

    def dfs(self):
        self.init_state.level = 0
        stack = [self.init_state]
        while len(stack) > 0:
            s = stack.pop()
            for next in s.successor():
                if self.is_visited(next) == False:
                    next.parent = s
                    if next.board.get_number_of_targets() == 0:
                        print_purple("PATH: ")
                        print(next.path + "\n")
                        return
                    next.level = s.level + 1
                    stack.append(next)
                    self.visit(next)
        print_danger("There is no route!")

    def visit(self, state: State):
        self.visited.append(state)

    def is_visited(self, s: State):
        for v in self.visited:
            if v.is_equal(s):
                return True
        return False

    def get_path(self, state: State):
        path = [state]
        while state.parent != state:
            path.append(state.parent)
            state = state.parent
        path.reverse()
        for p in path:
            p.print()
        print(
            f"number of moves: {len(path)} \nremained energy: {path[len(path)-1].energy}")
        return path
