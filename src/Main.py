import Input
from Board import Board
from State import State
from Moves import Moves

file_path = './test/1.txt'

matrix = Input.read_file(file_path)

board = Board(matrix)

moves = Moves()

initial_state = State(board)


# check it a cell can be T and I
# check a cell like 50T in string seperation
# count number of all targets and visited targets for end of algorithm

initial_state.print()

initial_state.move(moves.right)

initial_state.print()

initial_state.move(moves.down)

initial_state.print()

initial_state.move(moves.down)

initial_state.print()

initial_state.move(moves.right)

initial_state.print()

initial_state.move(moves.right)

initial_state.print()

initial_state.move(moves.right)

initial_state.print()

initial_state.move(moves.right)

initial_state.print()

initial_state.move(moves.right)

initial_state.print()

initial_state.move(moves.right)

initial_state.print()

initial_state.move(moves.right)

initial_state.print()

initial_state.move(moves.right)

initial_state.print()

initial_state.move(moves.left)

initial_state.print()
