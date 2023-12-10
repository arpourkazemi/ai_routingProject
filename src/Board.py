import re


class Board:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.num_targets = self.get_number_of_targets()

    def get_value(self, row, col):
        try:
            return int(re.findall(r'\d+', self.grid[row][col])[0])
        except Exception as e:
            return int(self.grid[row][col])

    def is_target(self, row, col):
        return re.sub(r'\d+', '', self.grid[row][col]) == 'T'

    def get_bonus(self, row, col):
        character = re.sub(r'\d+', '', self.grid[row][col])
        match character:
            case 'C':
                return 10
            case 'B':
                return 5
            case 'I':
                return 12
        return 0

    def is_wall(self, row, col):
        return re.sub(r'\d+', '', self.grid[row][col]) == 'X'

    def get_number_of_targets(self):
        count = 0
        for row in range(self.rows):
            for col in range(self.cols):
                if re.sub(r'\d+', '', self.grid[row][col]) == 'T':
                    count += 1
        return count

    def get_initial_position(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if re.sub(r'\d+', '', self.grid[row][col]) == 'R':
                    current_position = {
                        "row": row,
                        "col": col
                    }
                    return current_position
