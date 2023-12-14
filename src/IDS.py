import queue
from State import State
from Board import Board 
class IDS:
    def __init__(self, s:State):
        self.init_state = s
        self.board = s.board
        self.num_targets = s.board.num_targets
        self.visited = [s.board]
        self.ids()
    
    def ids(self):
        l=0
        path = self.dfs(l)
        while path == None:
            l+=1
            self.visited = [self.init_state.board]

            path = self.dfs(l)


    def dfs(self,l):
        self.init_state.level = 0
        stack=[self.init_state]
        while len(stack)>0:
            s = stack.pop()
            if s.level == l:
                continue
            for next in s.successor():
                if self.is_visited(next)==False:
                    #print("notvisited")
                    next.parent = s
                    if next.board.get_number_of_targets() == 0:
                        print("Bingo!")
                        return self.get_path(next)
                    next.level = s.level + 1
                    stack.append(next)
                    self.visit(next)
        print("gigigigigi")
        
    def visit(self,state:State):
        self.visited.append(state.board)


    def is_visited(self, s:State):
        for v in self.visited:
            if v.is_equal(s.board):
                #print("visited")
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