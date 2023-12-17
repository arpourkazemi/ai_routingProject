import time
import queue
from Utilities.State import State
from Utilities.ColorPrint import print_yellow, print_green, print_purple, print_danger


class Astar:
    def __init__(self, s: State):
        print_yellow("A* started...\n")
        self.init_state = s
        self.board = s.board
        self.num_targets = s.board.num_targets
        self.visited = [s]
        start = time.time()
        self.a_star()
        end = time.time()
        print_green("Time spent for A*: " + str(round(end - start, 3)))
        print("---------------------------------------------------")

    def a_star(self):
        pq = queue.PriorityQueue()
        self.init_state.level = 0
        pq.put((self.get_cost(self.init_state), self.init_state))
        while not pq.empty():
            g, s = pq.get()
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
                    pq.put((self.get_cost(next), next))
                    self.visit(next)
        print_danger("There is no route!")

    def get_cost(self, s: State):
        h = s.heuristic()
        g = 500 - s.energy
        return h+g

    def visit(self, state: State):
        self.visited.append(state)

    def is_visited(self, s: State):
        for v in self.visited:
            if v.is_equal(s):
                return True
        return False