class Board:
    def __init__(self, height, width, symbols=('X', 'O')):
        self.height = height
        self.width = width
        self.board = self.board_init()
        self.symbols = symbols

    def board_init(self):
        return [["%d" % (x * self.height + y) for y in range(self.width)] for x in range(self.height)]

    def get_board(self):
        return self.board

    def print_board(self):
        for i in range(self.height):
            print("%10s" % "", end="")
            for j in range(self.width):
                if j == self.width - 1:
                    print("%3s" % self.board[i][j], end="")
                else:
                    print("%3s   | " % self.board[i][j], end="")
            print()

    def update_board(self, x, y, symbol):
        self.board[x][y] = symbol

    def is_place_valid(self, x, y):
        if x < 0 or y < 0 or x >= self.height or y >= self.width:
            return False
        if self.board[x][y] in self.symbols:
            return False
        return True

    def is_board_full(self):
        for i in range(self.height):
            for j in range(self.height):
                if self.board[i][j] not in self.symbols:
                    return False
        return True

    def get_row(self, row):
        row_array = []
        for col_number in range(self.width):
            row_array.append(self.board[row][col_number])
        return row_array

    def get_col(self, col):
        col_array = []
        for row_number in range(self.height):
            col_array.append(self.board[row_number][col])
        return col_array

    def get_left_diagonal(self, x, y):
        left_diagonal_array = []
        while x > 0 and y > 0:
            x -= 1
            y -= 1

        while x < self.height and y < self.width:
            left_diagonal_array.append(self.board[x][y])
            x += 1
            y += 1

        return left_diagonal_array

    def get_right_diagonal(self, x, y):
        right_diagonal_array = []
        x, y = y, x
        while x < self.height and y < self.width:
            right_diagonal_array.append(self.board[y][x])
            x += 1
            y -= 1

        return right_diagonal_array
