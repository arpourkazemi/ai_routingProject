import time
import queue
from State import State
from Board import Board


class Astar:
    def __init__(self, s: State):
        self.init_state = s
        self.board = s.board
        self.num_targets = s.board.num_targets
        self.visited = [s]
        start = time.time()
        self.a_star()
        print("Time spent for A* : ", time.time()-start)

    def a_star(self):
        pq = queue.PriorityQueue()
        self.init_state.level = 0
        pq.put((self.get_cost(self.init_state), self.init_state))
        while not pq.empty():
            g, s = pq.get()
            print("----------------------------------")
            print("q.size: ", pq.qsize())
            for next in s.successor():
                print('\033[32m')
                next.print()
                print('\x1b[0m')
                if self.is_visited(next) == False:
                    next.parent = s
                    if next.board.get_number_of_targets() == 0:
                        print("Bingo!")
                        print(next.path)
                        return
                    next.level = s.level + 1
                    pq.put((self.get_cost(next), next))
                    self.visit(next)
        print("gigigigigi")

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
