class Board:

    def __init__(self, length, breadth):
        self.state = []
        self.board_length = length
        self.board_breadth = breadth

        for row in range(self.board_length):
            empty = []
            for col in range(self.board_breadth):
                empty.append('-')
            self.state.append(empty)


    def __str__(self):
        board_string = ""
        for row in range(self.board_length):
            for col in range(self.board_breadth):
                if col != (self.board_breadth - 1):
                    board_string += self.state[row][col] + " "
                else:
                    board_string += self.state[row][col] + " "

            board_string += "\n"
            if row != (self.board_length - 1):
                board_string += "************"
                board_string += "\n"

        return board_string


