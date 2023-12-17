import time
import queue
from Utilities.State import State
from Utilities.ColorPrint import print_yellow, print_green, print_purple, print_danger


class BestFS:

    def __init__(self, s: State):
        print_yellow("Best First Search started...\n")
        self.init_state = s
        self.board = s.board
        s.board.help_h()
        self.num_targets = s.board.num_targets
        self.visited = [s]
        start = time.time()
        self.bestFS()
        end = time.time()
        print_green("Time spent for BESTFIRST: " + str(round(end - start, 3)))
        print("---------------------------------------------------")

    def bestFS(self):
        pq = queue.PriorityQueue()
        self.init_state.level = 0
        pq.put((self.init_state.heuristic, self.init_state))
        while not pq.empty():
            g, s = pq.get()
            for next in s.successor():
                if self.is_visited(next) == False:
                    next.parent = s
                    if next.board.get_number_of_targets() == 0:
                        print_purple("PATH: ")
                        print(next.path + "\n")
                        moves = round(len(next.path)/2)
                        energy = next.energy + ((moves + 1) * 20)
                        print(
                            f"Moves: {moves} \n\nEnergy: {energy}\n")
                        return
                    next.level = s.level + 1
                    pq.put((next.heuristic(), next))
                    self.visit(next)
        print_danger("There is no route!")

    def visit(self, state: State):
        self.visited.append(state)

    def is_visited(self, s: State):
        for v in self.visited:
            if v.is_equal(s):
                return True
        return False
