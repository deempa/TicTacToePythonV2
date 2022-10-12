class Board:
    def __init__(self, height, width, symbols=('X', 'O')):
        self.__height = height
        self.__width = width
        self.__board = self.boardInit()
        self.symbols = symbols

    def boardInit(self):
        return [["%d" % (x * self.__height + y) for y in range(self.__width)] for x in range(self.__height)]

    def getBoard(self):
        return self.__board

    def printBoard(self):
        for i in range(self.__height):
            print("%10s" % "", end="")
            for j in range(self.__width):
                if j == self.__width - 1:
                    print("%3s" % self.__board[i][j], end="")
                else:
                    print("%3s   | " % self.__board[i][j], end="")
            print()

    def updateBoard(self, x, y, symbol):
        self.__board[x][y] = symbol

    def placeIsValid(self, x, y):
        if x < 0 or y < 0 or x >= self.__height or y >= self.__width:
            return False
        # if self.__board[x][y] == 'X' or self.__board[x][y] == 'O':
        if self.__board[x][y] in self.symbols:
            return False
        return True

    def boardIsFull(self):
        for i in range(self.__height):
            for j in range(self.__height):
                if self.__board[i][j] not in self.symbols:
                    return False
        return True

    def getRow(self, row):
        row_array = []
        for col_number in range(self.__width):
            row_array.append(self.__board[row][col_number])
        return row_array

    def getCol(self, col):
        col_array = []
        for row_number in range(self.__height):
            col_array.append(self.__board[row_number][col])
        return col_array

    def getLeftDiagonal(self, x, y):
        left_diagonal_array = []
        if x > y:
            x -= y
            y -= y
        elif x < y:
            y -= x
            x -= x
        else:
            x -= x
            y -= y

        while x < self.__height and y < self.__width:
            left_diagonal_array.append(self.__board[x][y])
            x += 1
            y += 1
        return left_diagonal_array

    def getRightDiagonal(self, x, y):
        right_diagonal_array = []
        x, y = y, x
        while x < self.__height and y < self.__width:
            right_diagonal_array.append(self.__board[y][x])
            x += 1
            y -= 1
        return right_diagonal_array
