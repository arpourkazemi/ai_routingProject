import time
import queue
from State import State
from Board import Board 

class BestFS:

    def __init__(self, s:State):
        print("Best First Search started...")
        self.init_state = s
        self.board = s.board
        self.num_targets = s.board.num_targets
        self.visited = [s.board]
        start = time.time()
        self.bestFS()
        print("Time spent for Best First Search: ", time.time() - start)
    

    def bestFS(self):
        pq = queue.PriorityQueue()
        self.init_state.level = 0
        pq.put(( self.init_state.heuristic , self.init_state ))
        while not pq.empty():
            g, s = pq.get()
            for next in s.successor():
                if self.is_visited(next)==False:
                    next.parent = s
                    if next.board.get_number_of_targets() == 0:
                        print("Bingo!")
                        return self.get_path(next)
                    next.level = s.level + 1
                    pq.put((next.heuristic,next))
                    self.visit(next)
        print("gigigigigi")
        

    def visit(self,state:State):
        self.visited.append(state.board)


    def is_visited(self, s:State):
        for v in self.visited:
            if v.is_equal(s.board):
                return True
        return False

    def get_path(self, state:State):
        path = [state]
        while state.parent != state:
            path.append(state.parent)
            state = state.parent
        path.reverse()
        for p in path:
            p.print()
        print(f"number of moves: {len(path)} \nremained energy: {path[len(path)-1].energy}")
        return path
