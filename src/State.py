from Board import Board
from Delivery import Delivery
from Moves import moves
from typing import List
import copy
import re


class State:
    def __init__(self, board: Board):
        self.board = board
        self.delivery = Delivery(
            board.get_initial_position()["row"], board.get_initial_position()["col"], 500 - board.get_value(board.get_initial_position()["row"], board.get_initial_position()["col"]))
        self.visited_targets = 0

    def can_move(self, move):
        if self.delivery.col + move[1] == self.board.cols or self.delivery.col + move[1] == -1 or self.delivery.row + move[0] == self.board.rows or self.delivery.row + move[0] == -1 or self.board.is_wall(self.delivery.row + move[0], self.delivery.col + move[1]):
            return False
        return True

    def move(self, move):
        if (self.can_move(move)):
            self.board.grid[self.delivery.row][self.delivery.col] = str(self.board.get_value(
                self.delivery.row, self.delivery.col))

            if (self.is_target(self.delivery.row + move[0], self.delivery.col + move[1])):
                self.visit_target(
                    self.delivery.row + move[0], self.delivery.col + move[1])
            elif (self.board.get_bonus(self.delivery.row + move[0], self.delivery.col + move[1]) != 0):
                self.use_bonus(self.delivery.row +
                               move[0], self.delivery.col + move[1])
            self.delivery.energy -= self.board.get_value(
                self.delivery.row + move[0], self.delivery.col + move[1])

            self.board.grid[self.delivery.row + move[0]][self.delivery.col + move[1]] = str(
                self.board.get_value(self.delivery.row + move[0], self.delivery.col + move[1])) + 'R'

            self.delivery.row = self.delivery.row + move[0]
            self.delivery.col = self.delivery.col + move[1]

    def is_target(self, row, col):
        return re.sub(r'\d+', '', self.board.grid[row][col]) == 'T'

    def visit_target(self, row, col):
        if (self.is_target(row, col)):
            self.board.grid[row][col] = self.board.get_value(row, col)
            self.visited_targets += 1

    def use_bonus(self, row, col):
        bonus = self.board.get_bonus(row, col)
        if (bonus != 0):
            self.delivery.energy += bonus
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
        print("\n" + "energy: " + str(self.delivery.energy))
        print("targets: " + str(self.board.num_targets))
        print("visited: " + str(self.visited_targets) + "\n")
        for row in self.board.grid:
            print(row)
