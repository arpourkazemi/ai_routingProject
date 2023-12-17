import Utilities.Input as Input
from Utilities.Board import Board
from Utilities.State import State
from Algorithms.Uninformed.BFS import BFS
from Algorithms.Uninformed.DFS import DFS
from Algorithms.Uninformed.IDS import IDS
from Algorithms.Uninformed.UCS import UCS
from Algorithms.Informed.BestFS import BestFS
from Algorithms.Informed.Astar import Astar

file_path = './test/6.txt'

matrix = Input.read_file(file_path)

board = Board(matrix)

initial_state = State(board)

print("---------------------------------------------------")
b = BFS(initial_state)
d = DFS(initial_state)
i = IDS(initial_state)
u = UCS(initial_state)
best = BestFS(initial_state)
A = Astar(initial_state)
