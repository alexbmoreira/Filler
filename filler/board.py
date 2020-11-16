class Board():
    
    grid = []

    def __init__(self, size):
        self.size = size

    def __str__(self):
        return_string = ""

        for i in range(self.size):
            for j in range(self.size):
                return_string += f"{self.grid[i][j].color}"
                return_string += " " * (self.size - len(self.grid[i][j].color))
            return_string += "\n"

        return return_string