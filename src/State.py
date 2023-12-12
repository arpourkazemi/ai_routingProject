from Board import Board
from Moves import moves
from typing import List
import copy
import re


class State:
    def __init__(self, board: Board):
        self.board = board
        self.row = board.get_initial_position()["row"]
        self.col = board.get_initial_position()["col"]
        self.energy = 500 - board.get_value(self.row, self.col)
        self.visited_targets = 0

    def can_move(self, move):
        if self.col + move[1] == self.board.cols:
            return False
        elif self.col + move[1] == -1:
            return False
        elif self.row + move[0] == self.board.rows:
            return False
        elif self.row + move[0] == -1:
            return False
        elif self.board.is_wall(self.row + move[0], self.col + move[1]):
            return False
        return True

    def move(self, move):

        # delete R from current cell
        current_cell_value = self.board.get_value(self.row, self.col)
        self.board.grid[self.row][self.col] = str(current_cell_value)

        next_row = self.row + move[0]
        next_col = self.col + move[1]
        next_cell = (next_row, next_col)

        # visit next cell if it is target
        if (self.is_target(*next_cell)):
            self.visit_target(*next_cell)

        # use next cell if it has bonus
        if (self.board.get_bonus(*next_cell) != 0):
            self.use_bonus(*next_cell)
        self.energy -= self.board.get_value(*next_cell)

        # put R in next cell
        self.board.grid[next_row][next_col] = str(
            self.board.get_value(*next_cell)) + 'R'

        # move delivery to next cell
        self.row = next_row
        self.col = next_col

    def is_target(self, row, col):
        return re.sub(r'\d+', '', self.board.grid[row][col]) == 'T'

    def visit_target(self, row, col):
        if (self.is_target(row, col)):
            self.board.grid[row][col] = str(self.board.get_value(row, col))
            self.visited_targets += 1

    def use_bonus(self, row, col):
        bonus = self.board.get_bonus(row, col)
        if (bonus != 0):
            self.energy += bonus
            self.board.grid[row][col] = str(self.board.get_value(row, col))

    def successor(self) -> List['State']:
        possible_states = []
        for attr, value in vars(moves).items():
            if self.can_move(value):
                newState = copy.deepcopy(self)
                newState.move(value)
                possible_states.append(newState)
        return possible_states

    def print(self):
        print("\n" + "energy: " + str(self.energy))
        print("targets: " + str(self.board.num_targets))
        print("visited: " + str(self.visited_targets) + "\n")
        for row in self.board.grid:
            print(row)
