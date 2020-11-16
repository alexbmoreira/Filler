import color
import random

class Board():
    colors = [
        color.Color("red", 0),
        color.Color("blue", 0),
        color.Color("green", 0),
        color.Color("purple", 0),
        color.Color("yellow", 0),
        color.Color("black", 0)
    ]

    grid = []

    def __init__(self, size):
        self.size = size
        self.createBoard()

    def __str__(self):
        return_string = ""

        for i in range(self.size):
            for j in range(self.size):
                return_string += f"{self.grid[i][j].color}"
                return_string += " " * (self.size - len(self.grid[i][j].color))
            return_string += "\n"

        return return_string

    def createBoard(self):
        above_color = ""
        for i in range(self.size):
            prev_color = ""
            row = []
            for j in range(self.size):
                above_color = self.grid[i - 1][j].color if i > 0 else ""
                valid_colors = [col for col in self.colors if col.color != prev_color and col.color != above_color]

                add_color = valid_colors[random.randint(0, len(valid_colors) - 1)]
                prev_color = add_color.color

                row.append(add_color)
            self.grid.append(row)