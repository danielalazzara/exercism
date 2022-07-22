class Queen:
    def __init__(self, row, column):
        if row < 0: 
            raise ValueError("row not positive")
        if row > 7:
            raise ValueError("row not on board")
        if column < 0:
            raise ValueError("column not positive")
        if column > 7:
            raise ValueError("column not on board")

        self.row = row
        self.column = column

    def can_attack(self, another_queen):
        if self.row == another_queen.row and self.column == another_queen.column:
            raise ValueError("Invalid queen position: both queens in the same square")
        if self.row == another_queen.row or self.column == another_queen.column:
            return True
        if self.row > another_queen.row:
            if self.column > another_queen.column:
                return self.row - another_queen.row == self.column - another_queen.column
            else:
                return self.row - another_queen.row == another_queen.column - self.column
        else:
            if self.column > another_queen.column:
                return another_queen.row - self.row == self.column - another_queen.column 
            else:
                return another_queen.row - self.row == another_queen.column - self.column
                return 
              
