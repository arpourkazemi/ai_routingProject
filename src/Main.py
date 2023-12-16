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

# print("---------------------")
b = BFS(initial_state)
d = DFS(initial_state)
i = IDS(initial_state)
u = UCS(initial_state)
best = BestFS(initial_state)
A = Astar(initial_state)
