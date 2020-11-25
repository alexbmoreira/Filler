import random

class Color():

    def __init__(self, name):
        self.name = name
        self.count = 0
        self.player = 0

    def __repr__(self):
        return self.name
        
    def toJSON(self):
        return {"name": self.name,
                "count": self.count,
                "player": self.player}

class Board():
    colors = [
        Color("red"),
        Color("blue"),
        Color("green"),
        Color("purple"),
        Color("yellow"),
        Color("black")
    ]

    grid = []

    def __init__(self, size, grid = None):
        self.size = size
        if grid == None:
            self.createBoard()
        else:
            self.grid = grid

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

                if i == 0 and j == self.size - 1:
                    add_color.player = 1
                elif i == self.size - 1 and j == 0:
                    add_color.player = 2

                row.append(add_color)

                self.colors[self.colors.index(add_color)].count += 1
            self.grid.append(row)

    def toJSON(self):
        return {"size": self.size,
                "board": [[color.toJSON() for color in row] for row in self.grid]}

class Game():

    def __init__(self, board = None):
        if board == None:
            self.board = Board(8)
        else:
            self.board = Board(3, board)

    def __str__(self):
        return str(self.board)

    def toJSON(self):
        return {"board": self.board.toJSON()}