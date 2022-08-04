# Globals for the directions
# Change the values as you see fit

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.coordinates = (x_pos, y_pos)

    
    def move(self, movements):
        for movement in movements:
            if movement == "L":
                self.direction = (self.direction - 1) % 4
            if movement == "R":
                self.direction = (self.direction + 1) % 4
            if movement == "A":
                self.advance()
                
