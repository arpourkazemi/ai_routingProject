import time
import queue
from State import State
from Board import Board

from Utilities import print_yellow, print_red, print_purple, print_green, print_danger


class IDS:

    def __init__(self, s: State):
        print("\033[33mIDS started...\n\033[m")
        self.init_state = s
        self.board = s.board
        self.num_targets = s.board.num_targets
        self.visited = [s]
        max_level = 2**(self.board.cols * self.board.rows)
        self.start = time.time()
        self.ids(max_level)
        end = time.time()
        print_red("Time spent for IDS: " + str(round(end - self.start, 3)))
        print("---------------------------------------------------")

    def ids(self, max_level=1000):
        l = 0
        path = self.dfs(l)
        while path == None and l<max_level:
            l += 1
            self.visited = [self.init_state]
            path = self.dfs(l)
            if time.time() - self.start > 10:
                break
        print_danger("There is no route!")
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
