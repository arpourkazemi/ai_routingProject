import Input
from Board import Board
from State import State
from Moves import Moves

file_path = './test/1.txt'

matrix = Input.read_file(file_path)

board = Board(matrix)

moves = Moves()

initial_state = State(board)


for state in initial_state.successor():
    state.print()

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
