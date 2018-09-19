class Nqueens:
    def __init__(self, size):
        self.size = size
        self.sol_num = 0
        self.solve_p()

    def solve_p(self):
        line = [0] * self.size
        self.create_queen(line, 0)
        print('Yeah', self.sol_num, 'possibilities')

    def create_queen(self, line, row):
        if row == self.size:
            self.sol_num += 1
            self.print_board(line)
        else:
            for col in range(self.size):
                if self.check_position(line, row, col):
                    line[row] = col
                    self.create_queen(line, row + 1)

    def check_position(self, line, row, col):
        for x in range(row):
            if line[x] == col \
                or line[x] - x == col - row \
                or line[x] + x == col + row:
                return False
        return True

    def print_board(self, line):
        for row in range(self.size):
            for col in range(self.size):
                if line[row] == col:
                    print("Q", end=" ")
                else:
                    print("*", end=" ")
            print()
        print()
Nqueens(8)
