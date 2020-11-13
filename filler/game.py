import color
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

    board = []

    def createBoard(self):
        above_color = ""
        for i in range(8):
            prev_color = ""
            row = []
            for j in range(8):
                above_color = self.board[i - 1][j].color if i > 0 else ""
                valid_colors = [col for col in self.colors if col.color != prev_color and col.color != above_color]

                add_color = valid_colors[random.randint(0, len(valid_colors) - 1)]
                prev_color = add_color.color

                row.append(add_color)
            self.board.append(row)

    def __str__(self):
        return_string = ""


        for i in range(8):
            for j in range(8):
                return_string += f"{self.board[i][j].color}"
                return_string += " " * (8 - len(self.board[i][j].color))
            return_string += "\n"

        return return_string

if __name__ == "__main__":
    game = Game()
    game.createBoard()
    print(str(game))