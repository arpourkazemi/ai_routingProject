from Board import Board
from Delivery import Delivery
import re


class State:
    def __init__(self, board: Board):
        self.board = board
        self.delivery = Delivery(
            board.get_initial_position()["row"], board.get_initial_position()["col"], 500 - board.get_value(board.get_initial_position()["row"], board.get_initial_position()["col"]))

    def can_move(self, move):
        if self.delivery.col + move[1] == self.board.cols or self.delivery.col + move[1] == -1 or self.delivery.row + move[0] == self.board.rows or self.delivery.row + move[0] == -1 or self.board.is_wall(self.delivery.row + move[0], self.delivery.col + move[1]):
            return False
        return True

    def move(self, move):
        if (self.can_move(move)):
            self.board.grid[self.delivery.row][self.delivery.col] = str(self.board.get_value(
                self.delivery.row, self.delivery.col))

            if (self.is_target(self.delivery.row + move[0], self.delivery.col + move[1])):
                self.board.visit_target(
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

    def use_bonus(self, row, col):
        bonus = self.board.get_bonus(row, col)
        if (bonus != 0):
            self.delivery.energy += bonus
            self.board.grid[row][col] = str(self.board.get_value(row, col))

    def print(self):
        print("\n" + str(self.delivery.energy) + "\n")
        for row in self.board.grid:
            print(row)
