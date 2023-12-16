import time
import queue
from State import State
from Board import Board

from Utilities import print_yellow, print_red, print_purple


class IDS:

    def __init__(self, s: State):
        print("\033[33mIDS started...\n\033[m")
        self.init_state = s
        self.board = s.board
        self.num_targets = s.board.num_targets
        self.visited = [s]
        start = time.time()
        self.ids()
        end = time.time()
        print_red("Time spent for IDS: " + str(round(end - start, 3)))
        print("---------------------------------------------------")

    def ids(self):
        l = 0
        path = self.dfs(l)
        while path == None:
            l += 1
            self.visited = [self.init_state]
            path = self.dfs(l)

    # handle ids break when no route has been found

    def dfs(self, l):
        self.init_state.level = 0
        stack = [self.init_state]
        while len(stack) > 0:
            s = stack.pop()
            if s.level == l:
                continue
            for next in s.successor():
                if self.is_visited(next) == False:
                    next.parent = s
                    if next.board.get_number_of_targets() == 0:
                        print_purple("PATH: ")
                        print(next.path + "\n")
                        return next.path
                    next.level = s.level + 1
                    stack.append(next)
                    self.visit(next)

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
