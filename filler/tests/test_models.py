import unittest

from ..filler.models import (Board, Color, ColorChoice, Computer, Game, Player,
                             Tile)


class TestColor(unittest.TestCase):

    def test_toDict(self):
        # Arrange
        col = 'red'

        # Act
        color_json = Color(col).toDict()

        # Assert
        self.assertEqual(color_json, {'name': 'red'})

    def test_fromDict(self):
        # Arrange
        py_obj = Color('red')
        test_dict = {'name': 'red'}

        # Act
        color = Color.fromDict(test_dict)

        # Assert
        self.assertEqual(color.name, py_obj.name)

class TestTile(unittest.TestCase):

    def test_toDict(self):
        # Arrange
        tile_col = 'red'
        tile_player = 1

        # Act
        tile_json = Tile(tile_col, tile_player).toDict()

        # Assert
        self.assertEqual(tile_json['player'], 1)
        self.assertEqual(tile_json['color'], {'name': 'red'})

    def test_fromDict(self):
        # Arrange
        py_obj = Tile(Color('red'), 1)
        test_dict = {'player': 1, 'color': {'name': 'red'}}

        # Act
        tile = Tile.fromDict(test_dict)

        # Assert
        self.assertEqual(tile.player, py_obj.player)
        self.assertEqual(tile.color.name, py_obj.color.name)

class TestPlayer(unittest.TestCase):

    def test_toDict(self):
        # Arrange
        player_num = 1
        player_col = 'red'
        player_score = 1

        # Act
        player_json = Player(player_num, player_col, player_score).toDict()

        # Assert
        self.assertEqual(player_json['player_num'], 1)
        self.assertEqual(player_json['color'], {'name': 'red'})
        self.assertEqual(player_json['score'], 1)

    def test_fromDict(self):
        # Arrange
        py_obj = Player(1, Color('red'), 1)
        test_dict = {'player_num': 1, 'color': {'name': 'red'}, 'score': 1}

        # Act
        plyr = Player.fromDict(test_dict)

        # Assert
        self.assertEqual(plyr.player_num, py_obj.player_num)
        self.assertEqual(plyr.color.name, py_obj.color.name)
        self.assertEqual(plyr.score, py_obj.score)

class TestBoard(unittest.TestCase):

    def test_toDict(self):
        # Arrange
        test_board = [[Tile("black", 1), Tile("blue", 0), Tile("red", 0)],
                    [Tile("yellow", 0), Tile("purple", 0), Tile("green", 0)],
                    [Tile("black", 0), Tile("blue", 0), Tile("red", 2)]]
        test_size = 3

        # Act
        board_json = Board(test_size, test_board).toDict()

        # Assert
        self.assertEqual(board_json['size'], 3)
        self.assertEqual(board_json['colors'][0], {'name': 'red', 'available': True})
        self.assertEqual(board_json['colors'][1], {'name': 'blue', 'available': True})
        self.assertEqual(board_json['colors'][2], {'name': 'green', 'available': True})
        self.assertEqual(board_json['colors'][3], {'name': 'purple', 'available': True})
        self.assertEqual(board_json['colors'][4], {'name': 'yellow', 'available': True})
        self.assertEqual(board_json['colors'][5], {'name': 'black', 'available': True})
        self.assertEqual(board_json['grid'][0][0], {'player': 1, 'color': {'name': 'black'}})
        self.assertEqual(board_json['grid'][0][1], {'player': 0, 'color': {'name': 'blue'}})
        self.assertEqual(board_json['grid'][0][2], {'player': 0, 'color': {'name': 'red'}})
        self.assertEqual(board_json['grid'][1][0], {'player': 0, 'color': {'name': 'yellow'}})
        self.assertEqual(board_json['grid'][1][1], {'player': 0, 'color': {'name': 'purple'}})
        self.assertEqual(board_json['grid'][1][2], {'player': 0, 'color': {'name': 'green'}})
        self.assertEqual(board_json['grid'][2][0], {'player': 0, 'color': {'name': 'black'}})
        self.assertEqual(board_json['grid'][2][1], {'player': 0, 'color': {'name': 'blue'}})
        self.assertEqual(board_json['grid'][2][2], {'player': 2, 'color': {'name': 'red'}})

    def test_fromDict(self):
        # Arrange
        test_board = [[Tile("black", 1), Tile("blue", 0), Tile("red", 0)],
                    [Tile("yellow", 0), Tile("purple", 0), Tile("green", 0)],
                    [Tile("black", 0), Tile("blue", 0), Tile("red", 2)]]
        py_obj = Board(3, test_board)

        test_dict = py_obj.toDict()

        # Act
        brd = Board.fromDict(test_dict)

        # Assert
        brd_tiles = [[t.color.name for t in row] for row in brd.grid]
        pyo_tiles = [[t.color.name for t in row] for row in py_obj.grid]

        self.assertEqual(brd.size, py_obj.size)
        self.assertEqual([c.name for c in brd.colors], [c.name for c in py_obj.colors])
        self.assertEqual(brd_tiles, pyo_tiles)


class TestGame(unittest.TestCase):

    def test_toDict(self):
        # Arrange
        test_board = [[Tile("black", 1), Tile("blue", 0), Tile("red", 0)],
                    [Tile("yellow", 0), Tile("purple", 0), Tile("green", 0)],
                    [Tile("black", 0), Tile("blue", 0), Tile("red", 2)]]
        test_size = 3

        # Act
        game_json = Game(test_board, test_size).toDict()

        # Assert
        self.assertEqual(game_json['player_1']['player_num'], 1)
        self.assertEqual(game_json['player_1']['color'], {'name': 'black'})
        self.assertEqual(game_json['player_1']['score'], 1)
        self.assertEqual(game_json['computer']['player_num'], 2)
        self.assertEqual(game_json['computer']['color'], {'name': 'red'})
        self.assertEqual(game_json['computer']['score'], 1)
        self.assertEqual(game_json['board']['size'], 3)
        self.assertEqual(game_json['board']['colors'][0], {'name': 'red', 'available': True})
        self.assertEqual(game_json['board']['colors'][1], {'name': 'blue', 'available': True})
        self.assertEqual(game_json['board']['colors'][2], {'name': 'green', 'available': True})
        self.assertEqual(game_json['board']['colors'][3], {'name': 'purple', 'available': True})
        self.assertEqual(game_json['board']['colors'][4], {'name': 'yellow', 'available': True})
        self.assertEqual(game_json['board']['colors'][5], {'name': 'black', 'available': True})
        self.assertEqual(game_json['board']['grid'][0][0], {'player': 1, 'color': {'name': 'black'}})
        self.assertEqual(game_json['board']['grid'][0][1], {'player': 0, 'color': {'name': 'blue'}})
        self.assertEqual(game_json['board']['grid'][0][2], {'player': 0, 'color': {'name': 'red'}})
        self.assertEqual(game_json['board']['grid'][1][0], {'player': 0, 'color': {'name': 'yellow'}})
        self.assertEqual(game_json['board']['grid'][1][1], {'player': 0, 'color': {'name': 'purple'}})
        self.assertEqual(game_json['board']['grid'][1][2], {'player': 0, 'color': {'name': 'green'}})
        self.assertEqual(game_json['board']['grid'][2][0], {'player': 0, 'color': {'name': 'black'}})
        self.assertEqual(game_json['board']['grid'][2][1], {'player': 0, 'color': {'name': 'blue'}})
        self.assertEqual(game_json['board']['grid'][2][2], {'player': 2, 'color': {'name': 'red'}})

    def test_makeMove(self):
        # Arrange
        test_board = [[Tile("black", 1), Tile("blue", 0), Tile("red", 0)],
                    [Tile("yellow", 0), Tile("purple", 0), Tile("green", 0)],
                    [Tile("black", 0), Tile("blue", 0), Tile("red", 2)]]
        test_size = 3
        test_game = Game(test_board, test_size)

        move_color = 'blue'

        # Act
        test_game.player_1.makeMove(test_game.board, Color(move_color))

        # Assert
        self.assertEqual(test_game.player_1.score, 2)
        self.assertEqual(test_game.board.grid[0][0].player, 1)
        self.assertEqual(test_game.board.grid[0][0].color.name, move_color)
        self.assertEqual(test_game.board.grid[0][1].player, 1)
        self.assertEqual(test_game.board.grid[0][1].color.name, move_color)

    def test_makeTwoMoves(self):
        # Arrange
        test_board = [[Tile("black", 1), Tile("blue", 0), Tile("red", 0)],
                    [Tile("yellow", 0), Tile("purple", 0), Tile("green", 0)],
                    [Tile("black", 0), Tile("blue", 0), Tile("red", 2)]]
        test_size = 3
        test_game = Game(test_board, test_size)

        move_color = 'blue'
        sec_move_color = 'yellow'

        # Act
        test_game.player_1.makeMove(test_game.board, Color(move_color))
        test_game.player_1.makeMove(test_game.board, Color(sec_move_color))

        # Assert
        self.assertEqual(test_game.player_1.score, 3)
        self.assertEqual(test_game.board.grid[0][0].player, 1)
        self.assertEqual(test_game.board.grid[0][0].color.name, sec_move_color)
        self.assertEqual(test_game.board.grid[0][1].player, 1)
        self.assertEqual(test_game.board.grid[0][1].color.name, sec_move_color)
        self.assertEqual(test_game.board.grid[1][0].player, 1)
        self.assertEqual(test_game.board.grid[1][0].color.name, sec_move_color)

    def test_possibleMoves(self):
        # Arrange
        test_board = [[Tile("black", 1), Tile("blue", 0), Tile("red", 2)],
                    [Tile("yellow", 0), Tile("purple", 0), Tile("red", 2)],
                    [Tile("black", 0), Tile("red", 2), Tile("red", 2)]]
        test_size = 3
        test_game = Game(test_board, test_size)

        # Act
        possible_moves = test_game.computer.possibleMoves(test_game.board)

        # Assert
        self.assertEqual(possible_moves, {'black': 1, 'blue': 1, 'purple': 1, 'yellow': 0, 'green': 0, 'red': 0})

    def test_makeThenFindPossible(self):
        # Arrange
        test_board = [[Tile("black", 1), Tile("blue", 0), Tile("red", 0)],
                    [Tile("yellow", 0), Tile("purple", 0), Tile("green", 0)],
                    [Tile("black", 0), Tile("blue", 0), Tile("red", 2)]]
        test_size = 3
        test_game = Game(test_board, test_size)

        move_color = 'blue'

        # Act
        test_game.computer.makeMove(test_game.board, Color(move_color))
        possible_moves = test_game.computer.possibleMoves(test_game.board)

        # Assert
        self.assertEqual(test_game.computer.score, 2)
        self.assertEqual(test_game.board.grid[2][2].player, 2)
        self.assertEqual(test_game.board.grid[2][2].color.name, 'blue')
        self.assertEqual(test_game.board.grid[2][1].player, 2)
        self.assertEqual(test_game.board.grid[2][1].color.name, 'blue')
        self.assertEqual(possible_moves, {'black': 1, 'green': 1, 'purple': 1, 'yellow': 0, 'red': 0})
    
    def test_determineBest(self):
        # Arrange
        test_board = [[Tile("black", 1), Tile("black", 1), Tile("yellow", 0)],
                    [Tile("yellow", 0), Tile("purple", 0), Tile("green", 0)],
                    [Tile("purple", 0), Tile("red", 2), Tile("red", 2)]]
        test_size = 3
        test_game = Game(test_board, test_size)

        # Act
        best_move = test_game.computer.determineBestMove(test_game.board)

        # Assert
        self.assertEqual(best_move.name, 'purple')
    
    def test_aiMoveMaking(self):
        # Arrange
        test_board = [[Tile("black", 1), Tile("black", 1), Tile("yellow", 0)],
                    [Tile("yellow", 0), Tile("purple", 0), Tile("green", 0)],
                    [Tile("purple", 0), Tile("red", 2), Tile("red", 2)]]
        test_size = 3
        test_game = Game(test_board, test_size)
        test_game.computer.score = 2

        # Act
        test_game.computer.aiMakeMove(test_game.board)

        # Assert
        self.assertEqual(test_game.computer.score, 4)
        self.assertEqual(test_game.board.grid[2][2].player, 2)
        self.assertEqual(test_game.board.grid[2][2].color.name, 'purple')
        self.assertEqual(test_game.board.grid[2][1].player, 2)
        self.assertEqual(test_game.board.grid[2][1].color.name, 'purple')
        self.assertEqual(test_game.board.grid[2][0].player, 2)
        self.assertEqual(test_game.board.grid[2][0].color.name, 'purple')
        self.assertEqual(test_game.board.grid[1][1].player, 2)
        self.assertEqual(test_game.board.grid[1][1].color.name, 'purple')

if __name__ == '__main__':
    unittest.main()
