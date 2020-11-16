import color as clr
import random

class Board():
    colors = [
        clr.Color("red"),
        clr.Color("blue"),
        clr.Color("green"),
        clr.Color("purple"),
        clr.Color("yellow"),
        clr.Color("black")
    ]

    grid = []

    def __init__(self, size):
        self.size = size
        self.createBoard()

    def __str__(self):
        return_string = ""

        for i in range(self.size):
            for j in range(self.size):
                return_string += f"{self.grid[i][j].name}"
                return_string += " " * (self.size - len(self.grid[i][j].name))
            return_string += "\n"

        return return_string

    def createBoard(self):
        above_color = ""
        for i in range(self.size):
            prev_color = ""
            row = []
            for j in range(self.size):
                above_color = self.grid[i - 1][j].name if i > 0 else ""
                valid_colors = [color for color in self.colors if color.name != prev_color and color.name != above_color]

                add_color = valid_colors[random.randint(0, len(valid_colors) - 1)]
                prev_color = add_color.name

                self.colors[self.colors.index(add_color)].count += 1
                row.append(add_color)
            self.grid.append(row)