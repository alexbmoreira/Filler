import random

class Color():

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name
        
    def toJSON(self):
        return {"name": self.name}

class Tile():

    def __init__(self, color, player):
        self.player = player
        self.color = Color(color)

    def toJSON(self):
        return {"player": self.player,
                "color": self.color.toJSON()}

class Player():

    def __init__(self, player_num, color, score = 1):
        self.player_num = player_num
        self.color = Color(color)
        self.score = score

    def toJSON(self):
        return {"player_num": self.player_num,
                "color": self.color.toJSON(),
                "score": self.score}

class Board():
    colors = [
        "red",
        "blue",
        "green",
        "purple",
        "yellow",
        "black"
    ]

    grid = []

    def __init__(self, size, grid = None):
        self.size = size
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
                
                valid_colors = [color for color in self.colors if color != prev_color and color != above_color]

                add_color = valid_colors[random.randint(0, len(valid_colors) - 1)]
                prev_color = add_color

                new_tile = Tile(add_color, 0)

                if i == 0 and j == 0:
                    new_tile.player = 1
                elif i == self.size - 1 and j == self.size - 1:
                    new_tile.player = 2

                row.append(new_tile)

            new_grid.append(row)
        
        return new_grid

    def toJSON(self):
        return {"size": self.size,
                "colors": [color for color in self.colors],
                "grid": [[tile.toJSON() for tile in row] for row in self.grid]}

class Game():

    def __init__(self, board = None):
        if board == None:
            self.board = Board(8)
        else:
            self.board = Board(3, board)
        
        self.player_1 = Player(1, self.board.grid[0][0].color.name)

    def __str__(self):
        return str(self.board)

    def makeMove(self, player, color):
        change_tiles = []
        player.color = color

        for i in range(self.board.size):
            for j in range(self.board.size):
                tile = self.board.grid[i][j]

                if tile.player == player.player_num:
                    tile.color = color

                if tile.player == 0 and tile.color.name == color.name:
                    self.checkTile(i, j, self.board, player.player_num, change_tiles)
                
        while len(change_tiles) > 0:
            coords = change_tiles.pop(0)
            player.score += 1
            self.board.grid[coords[0]][coords[1]].player = player.player_num

    def checkTile(self, i, j, board, player_num, coords_list):
        # check above
        if i > 0 and board.grid[i - 1][j].player == player_num:
            coords_list.append((i, j))
        # check below
        if i < board.size - 1 and board.grid[i + 1][j].player == player_num:
            coords_list.append((i, j))
        # check left
        if j > 0 and board.grid[i][j - 1].player == player_num:
            coords_list.append((i, j))
        # check right
        if j < board.size - 1 and board.grid[i][j + 1].player == player_num:
            coords_list.append((i, j))

    def determineBestMove(self, player):
        pass

    def possibleMoves(self, player):
        adj_colors = {}
        adj_coords = []

        for i in range(self.board.size):
            for j in range(self.board.size):
                tile = self.board.grid[i][j]
                if tile.player == player.player_num:
                    self.checkAdj(i, j, self.board, player.player_num, adj_coords)

        while len(adj_coords) > 0:
            coords = adj_coords.pop(0)
            tile = self.board.grid[coords[0]][coords[1]]
            if tile.color.name in adj_colors:
                adj_colors[tile.color.name] += 1
            else:
                adj_colors[tile.color.name] = 1

        return adj_colors

    def checkAdj(self, i, j, board, player_num, coords_list):
        # check above
        if i > 0 and board.grid[i - 1][j].player != player_num:
            coords_list.append((i - 1, j))
        # check below
        if i < board.size - 1 and board.grid[i + 1][j].player != player_num:
            coords_list.append((i + 1, j))
        # check left
        if j > 0 and board.grid[i][j - 1].player != player_num:
            coords_list.append((i, j - 1))
        # check right
        if j < board.size - 1 and board.grid[i][j + 1].player != player_num:
            coords_list.append((i, j + 1))

    def toJSON(self):
        return {"player_1": self.player_1.toJSON(),
                "board": self.board.toJSON()}