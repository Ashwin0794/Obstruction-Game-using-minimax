import board
import copy

class Solver:
    def __init__(self):
        self.board = board.Board(6,6)
        self.ai = ''
        self.human = ''
        print(self.board)
        return

    def freeSpace(self):
        space = 0
        for row in range(self.board.board_length):
            for col in range(self.board.board_breadth):
                if self.board.state[row][col] == '-':
                    space += 1
        return space

    def filledSpace(self):
        filled = 0
        for row in range(self.board.board_length):
            for col in range(self.board.board_breadth):
                if self.board.state[row][col] != '-':
                    filled += 1
        return filled

    def checkForFreeSpace(self, row, col):
        if self.board.state[row][col] != '-':
            return False
        return True

    def checkForWin(self):
        if self.freeSpace():
            return False
        return True

    def blockNeighbors(self, row, col, symbol):
        row_dir = [0, 0, -1, 1, -1, -1, 1, 1]
        col_dir = [-1, 1, 0, 0, -1, 1, -1, 1]
        for dir in range(8):
            curr_row = row + row_dir[dir]
            curr_col = col + col_dir[dir]
            if curr_row < 0 or curr_row >= self.board.board_length or curr_col < 0 or curr_col >= self.board.board_breadth:
                continue
            else:
                curr_mark = self.board.state[curr_row][curr_col]
                if  curr_mark == '-':
                    self.board.state[curr_row][curr_col] = symbol
        return

    def unblockNeighbors(self, row, col, symbol):

        row_dir = [0, 0, -1, 1, -1, -1, 1, 1]
        col_dir = [-1, 1, 0, 0, -1, 1, -1, 1]
        for dir in range(8):
            curr_row = row + row_dir[dir]
            curr_col = col + col_dir[dir]
            if curr_row < 0 or curr_row >= self.board.board_length or curr_col < 0 or curr_col >= self.board.board_breadth:
                continue
            else:
                if self.board.state[curr_row][curr_col] == symbol:
                    self.board.state[curr_row][curr_col] = '-'

        return

    def insertMove(self, row, col, mark):
        if self.checkForFreeSpace(row, col):
            self.board.state[row][col] = mark
            self.blockNeighbors(row, col, '/')
            print(self.board)
            if self.checkForWin():
                if mark == self.ai:
                    print("AI won!!")
                    exit()
                else:
                    print("You won!!")
                    exit()
        else:
            print("The position you entered is not free!!!")
            position = input("Enter the row and col again  :")
            row = (int(position.split()[0])) - 1
            col = (int(position.split()[1])) - 1
            if mark == self.ai:
                self.insertMove(row, col, self.ai)
            else:
                self.insertMove(row, col, self.human)
        return

    def humanMove(self):
        position = input("Enter the row and col for human :")
        row = (int(position.split()[0])) - 1
        col = (int(position.split()[1])) - 1
        print(self.board)
        self.insertMove(row, col, self.human)
        return

    def minimax(self, depth, isMaximizing):

        # first design depth limited and proceed.
        if depth > 1:
            return self.filledSpace()

        if (self.filledSpace()) == int(36):
            if isMaximizing:
                return -36
            return 36

        if (isMaximizing):
            #new_state_m = copy.deepcopy(state)
            #MAX player moves
            maxFilledSpace = -1000
            for row in range(self.board.board_length):
                for col in range(self.board.board_breadth):
                    if (self.board.state[row][col] == '-'):
                        self.board.state[row][col] = self.ai
                        self.blockNeighbors(row, col, '&')
                        depth += 1
                        value_max = self.minimax(depth, False)
                        print("value_max")
                        print(value_max)
                        self.board.state[row][col] = '-'
                        self.unblockNeighbors(row, col, '&')
                        if (value_max > maxFilledSpace):
                            maxFilledSpace = value_max
            return maxFilledSpace

        else:
            # MIN player move
            #new_state = copy.deepcopy(state)
            minFilledSpace = 1000
            for row in range(self.board.board_length):
                for col in range(self.board.board_breadth):
                    if (self.board.state[row][col] == '-'):
                        self.board.state[row][col] = self.human
                        self.blockNeighbors(row, col, '&')
                        depth += 1
                        value_min = self.minimax(depth, True)
                        print("value_min")
                        print(value_min)
                        self.board.state[row][col] = '-'
                        self.unblockNeighbors(row, col, '&')
                        if (value_min < minFilledSpace):
                            minFilledSpace = value_min
            return minFilledSpace


    def aiMove(self):
        maxFilledSpace = -1000
        bestRow, bestCol = 0, 0
        #new_state = copy.deepcopy(self.board.state)
        for row in range(self.board.board_length):
            for col in range(self.board.board_breadth):
                if (self.board.state[row][col] == '-'):
                    self.board.state[row][col] = self.ai
                    self.blockNeighbors(row, col, '&')
                    value = self.minimax(0, False)
                    print("printing value for every aiMove")
                    print(value)
                    print("printing row and col")
                    print(str(row) + " " + str(col))
                    self.board.state[row][col] = '-'
                    self.unblockNeighbors(row, col, '&')
                    if (value > maxFilledSpace):
                        maxFilledSpace = value
                        bestRow = row
                        bestCol = col
        print("maxFilledSpace b4 aiMove")
        print(maxFilledSpace)
        self.insertMove(bestRow, bestCol, self.ai)
        return

    def play(self, gameTurnOfAI):
        print("Welcome to Obstruction Game!!")
        while not self.checkForWin():
            if gameTurnOfAI == 1:
                self.ai = 'O'
                self.human = 'X'
                self.aiMove()
                self.humanMove()


            else:
                self.human = 'O'
                self.ai = 'X'
                self.humanMove()
                self.aiMove()
        return

