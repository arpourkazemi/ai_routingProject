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
        if self.col + move[1] == self.board.cols or self.col + move[1] == -1 or self.row + move[0] == self.board.rows or self.row + move[0] == -1 or self.board.is_wall(self.row + move[0], self.col + move[1]):
            return False
        return True

    def move(self, move):
        if (self.can_move(move)):
            self.board.grid[self.row][self.col] = str(self.board.get_value(
                self.row, self.col))

            if (self.is_target(self.row + move[0], self.col + move[1])):
                self.visit_target(
                    self.row + move[0], self.col + move[1])
            elif (self.board.get_bonus(self.row + move[0], self.col + move[1]) != 0):
                self.use_bonus(self.row +
                               move[0], self.col + move[1])
            self.energy -= self.board.get_value(
                self.row + move[0], self.col + move[1])

            self.board.grid[self.row + move[0]][self.col + move[1]] = str(
                self.board.get_value(self.row + move[0], self.col + move[1])) + 'R'

            self.row = self.row + move[0]
            self.col = self.col + move[1]

    def is_target(self, row, col):
        return re.sub(r'\d+', '', self.board.grid[row][col]) == 'T'

    def visit_target(self, row, col):
        if (self.is_target(row, col)):
            self.board.grid[row][col] = self.board.get_value(row, col)
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
