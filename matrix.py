class Matrix:
    def __init__(self, matrix_string):
        self.matrix = [row.split(" ") for row in matrix_string.splitlines()]
        self.matrix = [[int(number) for number in row] for row in self.matrix]

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        return [row[index - 1] for row in self.matrix]
