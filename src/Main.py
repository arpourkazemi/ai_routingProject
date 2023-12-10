import Input
from Board import Board
from State import State
from Moves import Moves

file_path = './test/1.txt'

matrix = Input.read_file(file_path)

board = Board(matrix)

moves = Moves()

initial_state = State(board)

print(board.compare(initial_state.board))


for state in initial_state.successor():
    print(board.compare(state.board))

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
