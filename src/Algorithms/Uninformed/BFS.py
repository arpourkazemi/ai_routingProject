import time
import queue
from Utilities.State import State
from Utilities.ColorPrint import print_yellow, print_blue, print_purple, print_danger


class BFS:
    def __init__(self, s: State):
        print("\033[33mBFS started...\n\033[m")
        self.init_state = s
        self.board = s.board
        self.num_targets = s.board.num_targets
        self.visited = [s]
        start = time.time()
        self.bfs()
        end = time.time()
        print_blue("Time spent for BFS: " + str(round(end - start, 3)))
        print("---------------------------------------------------")

    def bfs(self):
        q = queue.Queue()
        self.init_state.level = 0
        q.put(self.init_state)
        while not q.empty():
            s = q.get()
            for next in s.successor():
                if self.is_visited(next) == False:
                    next.parent = s
                    if next.board.get_number_of_targets() == 0:
                        print_purple("PATH: ")
                        print(next.path + "\n")
                        print(
                            f"Moves: {round(len(next.path)/2)} \n\nEnergy: {next.energy}\n")
                        return
                    next.level = s.level + 1
                    q.put(next)
                    self.visit(next)
        print_danger("There is no route!")

    def visit(self, state: State):
        self.visited.append(state)

    def is_visited(self, s: State):
        for v in self.visited:
            if v.is_equal(s):
                return True
        return False
