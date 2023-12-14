import Input
from Board import Board
from State import State
from Moves import moves
from BFS import BFS
from DFS import DFS
from IDS import IDS
from UCS import UCS
from BestFS import BestFS
from Astar import Astar
file_path = './test/1.txt'

matrix = Input.read_file(file_path)

board = Board(matrix)

initial_state = State(board)

print(board.is_equal(initial_state.board))

for state in initial_state.successor():
    print(board.is_equal(state.board))


print("---------------------")
#b= BFS(initial_state)
#d= DFS(initial_state)
#i= IDS(initial_state)
#u= UCS(initial_state)
#best = BestFS(initial_state)
A = Astar(initial_state)
"""
['1R', '1', '1', '5', '5', '4', '2C', '1', '15', '1B']
['1', '1', '5', '3', '5', '5', '4', '5', 'X', 'X']
['5', '1I', '1', '6', '2', '2', '2', '1', '1', '1T']
['X', 'X', '1', '6', '5', '5', '2', '1', '1', 'X']
['X', 'X', '1', 'X', 'X', '50', '2', '1C', '1', 'X']
['1', '1', '1', '2', '2', '2T', '2', '1', '1', '1']


['1R', '1', '1', '5', '5', '4', '2C', '1', '15', '1B']
['1', '1', '5', '3', '5', '5', '4', '5', 'X', 'X']
['5', '1I', '1', '6', '2', '2', '2', '1', '1', '1T']
['X', 'X', '1', '6', '5', '5', '2', '1', '1', 'X']
['X', 'X', '1', 'X', 'X', '50', '2', '1C', '1', 'X']
['1', '1', '1', '2', '2', '2T', '2', '1', '1', '1']
"""

#d= DFS1(board)
#d.dfs(initial_state,0)
#d.plot_dfs_tree()

# initial_state.print()

# initial_state.move(moves.right)

# initial_state.print()

# initial_state.move(moves.down)

# initial_state.print()

# initial_state.move(moves.down)

# initial_state.print()

# initial_state.move(moves.right)

# initial_state.print()

# initial_state.move(moves.right)

# initial_state.print()

# initial_state.move(moves.right)

# initial_state.print()

# initial_state.move(moves.right)

# initial_state.print()

# initial_state.move(moves.right)

# initial_state.print()

# initial_state.move(moves.right)

# initial_state.print()

# initial_state.move(moves.right)

# initial_state.print()

# initial_state.move(moves.right)

# initial_state.print()

# initial_state.move(moves.left)

# initial_state.print()
