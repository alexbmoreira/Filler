import unittest

from ..filler.models import (Board, Color, ColorChoice, Computer, Game, Player,
                             Tile)


class TestColor(unittest.TestCase):

    def test_toJSON(self):
        # Arrange
        col = 'red'

        # Act
        color_json = Color(col).toJSON()

        # Assert
        self.assertEqual(color_json, {'name': 'red'})

class TestTile(unittest.TestCase):

    def test_toJSON(self):
        # Arrange
        tile_col = 'red'
        tile_player = 1

        # Act
        tile_json = Tile(tile_col, tile_player).toJSON()

        # Assert
        self.assertEqual(tile_json['player'], 1)
        self.assertEqual(tile_json['color'], {'name': 'red'})

class TestPlayer(unittest.TestCase):

    def test_toJSON(self):
        # Arrange
        player_num = 1
        player_col = 'red'
        player_score = 0

        # Act
        player_json = Player(player_num, player_col, player_score).toJSON()

        # Assert
        self.assertEqual(player_json['player_num'], 1)
        self.assertEqual(player_json['color'], {'name': 'red'})
        self.assertEqual(player_json['score'], 0)

class TestBoard(unittest.TestCase):

    def test_toJSON(self):
        # Arrange
        test_board = [[Tile("black", 1), Tile("blue", 0), Tile("red", 0)],
                    [Tile("yellow", 0), Tile("purple", 0), Tile("green", 0)],
                    [Tile("black", 0), Tile("blue", 0), Tile("red", 2)]]
        test_size = 3

        # Act
        board_json = Board(test_size, test_board).toJSON()

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


class TestGame(unittest.TestCase):

    def test_toJSON(self):
        # Arrange
        test_board = [[Tile("black", 1), Tile("blue", 0), Tile("red", 0)],
                    [Tile("yellow", 0), Tile("purple", 0), Tile("green", 0)],
                    [Tile("black", 0), Tile("blue", 0), Tile("red", 2)]]
        test_size = 3

        # Act
        game_json = Game(test_board, test_size).toJSON()

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

        # Act

        # Assert
        test_board = [[Tile("black", 1), Tile("blue", 0), Tile("red", 0)],
                    [Tile("yellow", 0), Tile("purple", 0), Tile("green", 0)],
                    [Tile("black", 0), Tile("blue", 0), Tile("red", 2)]]
        test_game = Game(test_board)
        test_game.player_1.makeMove(test_game.board, Color('blue'))
        test_game.player_1.makeMove(test_game.board, Color('yellow'))

        self.assertEqual(test_game.toJSON(), {'player_1': {'player_num': 1, 'color': {'name': 'yellow'}, 'score': 3},
                                                'computer': {'player_num': 2, 'color': {'name': 'red'}, 'score': 1},
                                                'board': {
                                                        'size': 3,
                                                        'colors': [
                                                            {'name': 'red', 'available': True},
                                                            {'name': 'blue', 'available': True},
                                                            {'name': 'green', 'available': True},
                                                            {'name': 'purple', 'available': True},
                                                            {'name': 'yellow', 'available': False},
                                                            {'name': 'black', 'available': True}
                                                            ],
                                                        'grid': [
                                                            [
                                                                {'player': 1, 'color': {'name': 'yellow'}},
                                                                {'player': 1, 'color': {'name': 'yellow'}},
                                                                {'player': 0, 'color': {'name': 'red'}}
                                                            ],
                                                            [
                                                                {'player': 1, 'color': {'name': 'yellow'}},
                                                                {'player': 0, 'color': {'name': 'purple'}},
                                                                {'player': 0, 'color': {'name': 'green'}}
                                                            ],
                                                            [
                                                                {'player': 0, 'color': {'name': 'black'}},
                                                                {'player': 0, 'color': {'name': 'blue'}},
                                                                {'player': 2, 'color': {'name': 'red'}}
                                                            ]
                                                        ]}
                                                    })

    def test_possibleMoves(self):
        # Arrange

        # Act

        # Assert
        test_board = [[Tile("black", 1), Tile("blue", 0), Tile("red", 2)],
                    [Tile("yellow", 0), Tile("purple", 0), Tile("red", 2)],
                    [Tile("black", 0), Tile("red", 2), Tile("red", 2)]]
        test_game = Game(test_board)

        self.assertEqual(test_game.computer.possibleMoves(test_game.board), {'black': 1, 'blue': 1, 'purple': 1})

    def test_makeThenFindPossible(self):
        # Arrange

        # Act

        # Assert
        test_board = [[Tile("black", 1), Tile("blue", 0), Tile("red", 0)],
                    [Tile("yellow", 0), Tile("purple", 0), Tile("green", 0)],
                    [Tile("black", 0), Tile("blue", 0), Tile("red", 2)]]
        test_game = Game(test_board)
        test_game.computer.makeMove(test_game.board, Color('blue'))

        self.assertEqual(test_game.computer.possibleMoves(test_game.board), {'black': 1, 'green': 1, 'purple': 1})
    
    def test_determineBest(self):
        # Arrange

        # Act

        # Assert
        test_board = [[Tile("black", 1), Tile("black", 1), Tile("yellow", 0)],
                    [Tile("yellow", 0), Tile("purple", 0), Tile("green", 0)],
                    [Tile("purple", 0), Tile("red", 2), Tile("red", 2)]]
        test_game = Game(test_board)

        self.assertEqual(test_game.computer.determineBestMove(test_game.board).toJSON(), {'name': 'purple'})
    
    def test_aiMoveMaking(self):
        # Arrange

        # Act

        # Assert
        test_board = [[Tile("black", 1), Tile("black", 1), Tile("yellow", 0)],
                    [Tile("yellow", 0), Tile("purple", 0), Tile("green", 0)],
                    [Tile("purple", 0), Tile("red", 2), Tile("red", 2)]]
        test_game = Game(test_board)
        test_game.player_1.score = 2
        test_game.computer.score = 2
        test_game.computer.aiMakeMove(test_game.board)

        self.assertEqual(test_game.toJSON(), {'player_1': {'player_num': 1, 'color': {'name': 'black'}, 'score': 2},
                                                'computer': {'player_num': 2, 'color': {'name': 'purple'}, 'score': 4},
                                                'board': {
                                                        'size': 3,
                                                        'colors': [
                                                            {'name': 'red', 'available': True},
                                                            {'name': 'blue', 'available': True},
                                                            {'name': 'green', 'available': True},
                                                            {'name': 'purple', 'available': False},
                                                            {'name': 'yellow', 'available': True},
                                                            {'name': 'black', 'available': True}
                                                            ],
                                                        'grid': [
                                                            [
                                                                {'player': 1, 'color': {'name': 'black'}},
                                                                {'player': 1, 'color': {'name': 'black'}},
                                                                {'player': 0, 'color': {'name': 'yellow'}}
                                                            ],
                                                            [
                                                                {'player': 0, 'color': {'name': 'yellow'}},
                                                                {'player': 2, 'color': {'name': 'purple'}},
                                                                {'player': 0, 'color': {'name': 'green'}}
                                                            ],
                                                            [
                                                                {'player': 2, 'color': {'name': 'purple'}},
                                                                {'player': 2, 'color': {'name': 'purple'}},
                                                                {'player': 2, 'color': {'name': 'purple'}}
                                                            ]
                                                        ]}
                                                    })

if __name__ == '__main__':
    unittest.main()
