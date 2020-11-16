import board as brd

class Game():

    board = brd.Board(8)

    def __str__(self):
        return str(self.board)

if __name__ == "__main__":
    game = Game()

    print(str(game))