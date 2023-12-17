from Utilities.Board import Board
from Utilities.Moves import moves
from typing import List
import copy
import re


class State:
    def __init__(self, board: Board):
        self.board = board
        [self.row, self.col] = board.get_initial_position()
        self.energy = 500 - board.get_value(self.row, self.col)
        self.visited_targets = 0
        self.parent = self
        self.level = 0
        self.path = ''

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
        current_cell_value = self.board.get_value(self.row, self.col)
        self.board.grid[self.row][self.col] = str(current_cell_value)

        next_row = self.row + move[0]
        next_col = self.col + move[1]
        next_cell = (next_row, next_col)
        if (self.board.get_bonus(*next_cell) != 0):
            self.use_bonus(*next_cell)
        self.energy -= self.board.get_value(*next_cell)
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
        if (self.is_target(self.row, self.col)):
            newState = copy.deepcopy(self)
            newState.visit_target(self.row, self.col)
            possible_states.append(newState)
        for attr, value in vars(moves).items():
            if self.can_move(value):
                newState = copy.deepcopy(self)
                newState.move(value)
                newState.path += " " + str(attr)
                possible_states.append(newState)
        return possible_states

    def heuristic(self):
        if (self.visited_targets == self.board.num_targets):
            return 0
        manhattan_distance = 0
        while (manhattan_distance <= self.board.cols + self.board.rows):
            for i in range(manhattan_distance + 1):
                x = self.row + i
                y = self.col + (manhattan_distance - i)
                if (x >= 0 and x < self.board.rows and y >= 0 and y < self.board.cols):
                    if self.is_target(x, y):
                        return manhattan_distance + self.board.num_targets - self.visited_targets

                x = self.row - i
                y = self.col + (manhattan_distance - i)
                if (x >= 0 and x < self.board.rows and y >= 0 and y < self.board.cols):
                    if self.is_target(x, y):
                        return manhattan_distance + self.board.num_targets - self.visited_targets

                x = self.row + i
                y = self.col - (manhattan_distance - i)
                if (x >= 0 and x < self.board.rows and y >= 0 and y < self.board.cols):
                    if self.is_target(x, y):
                        return manhattan_distance + self.board.num_targets - self.visited_targets

                x = self.row - i
                y = self.col - (manhattan_distance - i)
                if (x >= 0 and x < self.board.rows and y >= 0 and y < self.board.cols):
                    if self.is_target(x, y):
                        return manhattan_distance + self.board.num_targets - self.visited_targets

            manhattan_distance += 1

    def __lt__(self, other):
        return self

    def print(self):
        print("\n" + "energy: " + str(self.energy))
        print("targets: " + str(self.board.num_targets))
        print("visited: " + str(self.visited_targets))
        print("heuristic: " + str(self.heuristic()))
        print("coordinate: (" + str(self.row) + ", " + str(self.col) + ")\n")
        for row in self.board.grid:
            print(row)

    def is_equal(self, state: 'State'):
        if self.visited_targets != state.visited_targets:
            return False
        if (self.row != state.row or self.col != state.col):
            return False
        for row in range(self.board.rows):
            for col in range(self.board.cols):
                if self.board.grid[row][col] != state.board.grid[row][col]:
                    return False
        return True
