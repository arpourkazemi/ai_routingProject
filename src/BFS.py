import queue
from State import State
from Board import Board 
class BFS:
    def __init__(self, s:State):
        self.init_state = s
        self.board = s.board
        self.num_targets = s.board.num_targets
        self.visited = [s.board]
        self.bfs()
    
    def bfs(self):
        q=queue.Queue()
        self.init_state.level = 0
        q.put(self.init_state)
        while not q.empty():
            s = q.get()
            print("q.size: ",q.qsize())
            for next in s.successor():
                if self.is_visited(next)==False:
                    #print("notvisited")
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
                print("visited")
                return True
        return False

    def get_path(self, state:State):
        path = [state]
        while state.parent != state:
            path.append(state.parent)
            state = state.parent
        for p in path:
            p.print()
        print(len(path))
        return path


#state =State(Board([['1R', '1', '1', '5', '5', '4', '2C', '1', '15', '1B'],
 ##       ['1', '1', '5', '3', '5', '5', '4', '5', 'X', 'X'],
 #       ['5', '1I', '1', '6', '2', '2', '2', '1', '1', '1T'],
  #      ['X', 'X', '1', '6', '5', '5', '2', '1', '1', 'X']  ,
   #     ['X', 'X', '1', 'X', 'X', '50', '2', '1C', '1', 'X'],
    #    ['1', '1', '1', '2', '2', '2T', '2', '1', '1', '1']]))


#b = BFS(state)
#print(b.is_visited(state))