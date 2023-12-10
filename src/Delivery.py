class Delivery:
    def __init__(self, row, col, energy):
        self.row = row
        self.col = col
        self.energy = energy

    # def successor(state: State):
    #     possible_states = []
    #     for move in moves:
    #         if state.can_move(move):
    #             newState = copy.deepcopy(state)
    #             possible_states.append(newState.move(move))

    #     return possible_states
