import color
import board as brd
import random

class Game():
    colors = [
        color.Color("red", 0),
        color.Color("blue", 0),
        color.Color("green", 0),
        color.Color("purple", 0),
        color.Color("yellow", 0),
        color.Color("black", 0)
    ]

    board = brd.Board(8)

    def createBoard(self):
        above_color = ""
        for i in range(self.board.size):
            prev_color = ""
            row = []
            for j in range(self.board.size):
                above_color = self.board.grid[i - 1][j].color if i > 0 else ""
                valid_colors = [col for col in self.colors if col.color != prev_color and col.color != above_color]

                add_color = valid_colors[random.randint(0, len(valid_colors) - 1)]
                prev_color = add_color.color

                row.append(add_color)
            self.board.grid.append(row)

    def __str__(self):
        return str(self.board)

if __name__ == "__main__":
    game = Game()
    game.createBoard()
    print(str(game))