import time 
import queue
from State import State
from Board import Board 

class BFS:
    def __init__(self, s:State):
        print("BFS started...")
        self.init_state = s
        self.board = s.board
        self.num_targets = s.board.num_targets
        self.visited = [s.board]
        start = time.time()
        self.bfs()
        end = time.time()
        print("Time spent for BFS:",end - start)
    
    def bfs(self):
        q=queue.Queue()
        self.init_state.level = 0
        q.put(self.init_state)
        while not q.empty():
            s = q.get()
            for next in s.successor():
                if self.is_visited(next)==False:
                    next.parent = s
                    if next.board.get_number_of_targets() == 0:
                        print("Bingo!")
                        return self.get_path(next)
                    next.level = s.level + 1
                    q.put(next)
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

