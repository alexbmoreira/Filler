import random

class Color():

    def __init__(self, name):
        self.name = str(name)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name
        
    def toDict(self):
        return {'name': self.name}

    @classmethod
    def fromDict(cls, d):
        return cls(d['name'])

class ColorChoice(Color):
    def __init__(self, name, available = True):
        super().__init__(name)
        self.available = available

    def toDict(self):
        return {'name': self.name,
                'available': self.available}

    @classmethod
    def fromDict(cls, d):
        return cls(d['name'], d['available'])

class Tile():

    def __init__(self, color, player):
        self.color = Color(color)
        self.player = player

    def toDict(self):
        return {'player': self.player,
                'color': self.color.toDict()}

    @classmethod
    def fromDict(cls, d):
        col = Color.fromDict(d['color'])
        return cls(col, d['player'])

class Player():

    def __init__(self, player_num, color, score = 1):
        self.player_num = player_num
        self.color = Color(color)
        self.score = score

    def makeMove(self, board, color):
        change_tiles = []
        [color for color in board.colors if color.name == self.color.name][0].available = True
        self.color = color
        [color for color in board.colors if color.name == self.color.name][0].available = False

        for i in range(board.size):
            for j in range(board.size):
                tile = board.grid[i][j]

                if tile.player == self.player_num:
                    tile.color = color

                if tile.player == 0 and tile.color.name == color.name and (i, j) not in change_tiles:
                    self.checkTile(i, j, board, change_tiles)
                
        while len(change_tiles) > 0:
            coords = change_tiles.pop(0)
            self.score += 1
            board.grid[coords[0]][coords[1]].player = self.player_num

    def checkTile(self, i, j, board, coords_list):
        # check above
        if i > 0 and board.grid[i - 1][j].player == self.player_num:
            coords_list.append((i, j))
        # check below
        elif i < board.size - 1 and board.grid[i + 1][j].player == self.player_num:
            coords_list.append((i, j))
        # check left
        elif j > 0 and board.grid[i][j - 1].player == self.player_num:
            coords_list.append((i, j))
        # check right
        elif j < board.size - 1 and board.grid[i][j + 1].player == self.player_num:
            coords_list.append((i, j))

    def toDict(self):
        return {'player_num': self.player_num,
                'color': self.color.toDict(),
                'score': self.score}

    @classmethod
    def fromDict(cls, d):
        col = Color.fromDict(d['color'])
        return cls(d['player_num'], col, d['score'])

class Computer(Player):

    def aiMakeMove(self, board):
        super().makeMove(board, self.determineBestMove(board))

    def possibleMoves(self, board):
        adj_colors = {}
        adj_coords = []

        for i in range(board.size):
            for j in range(board.size):
                tile = board.grid[i][j]
                if tile.player == 0 and [color for color in board.colors if color.name == tile.color.name][0].available == True:
                    self.checkTile(i, j, board, adj_coords)

        while len(adj_coords) > 0:
            coords = adj_coords.pop(0)
            tile = board.grid[coords[0]][coords[1]]
            if tile.color.name in adj_colors:
                adj_colors[tile.color.name] += 1
            else:
                adj_colors[tile.color.name] = 1

        for color in board.colors:
            if color.available == True and color.name not in adj_colors:
                adj_colors[color.name] = 0

        return adj_colors

    def determineBestMove(self, board):
        return Color(max(self.possibleMoves(board), key=self.possibleMoves(board).get))

class Board():
    colors = [
        ColorChoice("red"),
        ColorChoice("blue"),
        ColorChoice("green"),
        ColorChoice("purple"),
        ColorChoice("yellow"),
        ColorChoice("black")
    ]

    grid = []

    def __init__(self, size, grid = None, colors = None):
        self.size = size

        if colors == None:
            self.colors = [ColorChoice(color.name) for color in self.colors]
        else:
            self.colors = colors

        if grid == None:
            self.grid = self.createBoard()
        else:
            self.grid = grid

    def __str__(self):
        return_string = ""

        for i in range(self.size):
            for j in range(self.size):
                return_string += f"{self.grid[i][j].color.name}"
                return_string += " " * (self.size - len(self.grid[i][j].color.name))
            return_string += "\n"

        return return_string

    def createBoard(self):
        new_grid = []

        above_color = ""
        for i in range(self.size):
            prev_color = ""
            row = []
            for j in range(self.size):
                above_color = new_grid[i - 1][j].color.name if i > 0 else ""
                
                if i == self.size - 1 and j == self.size - 1:
                    valid_colors = [color.name for color in self.colors if color.available and color.name != prev_color and color.name != above_color]
                else:
                    valid_colors = [color.name for color in self.colors if color.name != prev_color and color.name != above_color]

                add_color = valid_colors[random.randint(0, len(valid_colors) - 1)]
                prev_color = add_color

                new_tile = Tile(add_color, 0)

                if i == 0 and j == 0:
                    new_tile.player = 1
                    [color for color in self.colors if color.name == new_tile.color.name][0].available = False
                elif i == self.size - 1 and j == self.size - 1:
                    new_tile.player = 2
                    [color for color in self.colors if color.name == new_tile.color.name][0].available = False

                row.append(new_tile)

            new_grid.append(row)
        
        return new_grid

    def toDict(self):
        return {'size': self.size,
                'colors': [color.toDict() for color in self.colors],
                'grid': [[tile.toDict() for tile in row] for row in self.grid]}

    @classmethod
    def fromDict(cls, d):
        grid = [[Tile.fromDict(d) for d in row] for row in d['grid']]
        c_choices = [ColorChoice.fromDict(col) for col in d['colors']]
        return cls(d['size'], grid, c_choices)

class Game():

    def __init__(self, board = None, board_size = 3, player_1 = None, computer = None):
        if board == None:
            self.board = Board(8)
        else:
            if type(board) is list:
                self.board = Board(board_size, board)
            else:
                self.board = board
        
        if player_1 == None and computer == None:
            end_loc = self.board.size - 1
            self.player_1 = Player(1, self.board.grid[0][0].color.name)
            self.computer = Computer(2, self.board.grid[end_loc][end_loc].color.name)
        else:
            self.player_1 = player_1
            self.computer = computer

    def __str__(self):
        return str(self.board)

    def toDict(self):
        return {'player_1': self.player_1.toDict(),
                'computer': self.computer.toDict(),
                'board': self.board.toDict()}

    @classmethod
    def fromDict(cls, d):
        p_1 = Player.fromDict(d['player_1'])
        comp = Computer.fromDict(d['computer'])
        board = Board.fromDict(d['board'])
        return cls(board, player_1=p_1, computer=comp)