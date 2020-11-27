import unittest

from ..filler.models import *

class TestColor(unittest.TestCase):

    def test_toJSON(self):
        self.assertEqual(Color("red").toJSON(), {'name': 'red'})

class TestTile(unittest.TestCase):

    def test_toJSON(self):
        self.assertEqual(Tile("red", 1).toJSON(), {'player': 1, 'color': {'name': 'red'}})

class TestPlayer(unittest.TestCase):

    def test_toJSON(self):
        self.assertEqual(Player(1, "red", 0).toJSON(), {'player_num': 1, 'color': {'name': 'red'}, 'score': 0})

class TestBoard(unittest.TestCase):

    def test_toJSON(self):
        test_board = [[Tile("black", 1), Tile("blue", 0), Tile("red", 0)],
                    [Tile("yellow", 0), Tile("purple", 0), Tile("green", 0)],
                    [Tile("black", 0), Tile("blue", 0), Tile("red", 2)]]

        self.assertEqual(Board(3, test_board).toJSON(), {'size': 3,
                                                        'colors': ['red', 'blue', 'green', 'purple', 'yellow', 'black'],
                                                        'grid': [
                                                            [
                                                                {'player': 1, 'color': {'name': 'black'}},
                                                                {'player': 0, 'color': {'name': 'blue'}},
                                                                {'player': 0, 'color': {'name': 'red'}}
                                                            ],
                                                            [
                                                                {'player': 0, 'color': {'name': 'yellow'}},
                                                                {'player': 0, 'color': {'name': 'purple'}},
                                                                {'player': 0, 'color': {'name': 'green'}}
                                                            ],
                                                            [
                                                                {'player': 0, 'color': {'name': 'black'}},
                                                                {'player': 0, 'color': {'name': 'blue'}},
                                                                {'player': 2, 'color': {'name': 'red'}}
                                                            ]
                                                        ]})

class TestGame(unittest.TestCase):

    def test_toJSON(self):
        test_board = [[Tile("black", 1), Tile("blue", 0), Tile("red", 0)],
                    [Tile("yellow", 0), Tile("purple", 0), Tile("green", 0)],
                    [Tile("black", 0), Tile("blue", 0), Tile("red", 2)]]

        self.assertEqual(Game(test_board).toJSON(), {'player_1': {'player_num': 1, 'color': {'name': 'black'}, 'score': 1},
                                                    'board': {
                                                            'size': 3,
                                                            'colors': ['red', 'blue', 'green', 'purple', 'yellow', 'black'],
                                                            'grid': [
                                                                [
                                                                    {'player': 1, 'color': {'name': 'black'}},
                                                                    {'player': 0, 'color': {'name': 'blue'}},
                                                                    {'player': 0, 'color': {'name': 'red'}}
                                                                ],
                                                                [
                                                                    {'player': 0, 'color': {'name': 'yellow'}},
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

    def test_makeMove(self):
        test_board = [[Tile("black", 1), Tile("blue", 0), Tile("red", 0)],
                    [Tile("yellow", 0), Tile("purple", 0), Tile("green", 0)],
                    [Tile("black", 0), Tile("blue", 0), Tile("red", 2)]]
        test_game = Game(test_board)
        test_game.makeMove(test_game.player_1, Color('blue'))

        self.assertEqual(test_game.toJSON(), {'player_1': {'player_num': 1, 'color': {'name': 'blue'}, 'score': 2},
                                                'board': {
                                                        'size': 3,
                                                        'colors': ['red', 'blue', 'green', 'purple', 'yellow', 'black'],
                                                        'grid': [
                                                            [
                                                                {'player': 1, 'color': {'name': 'blue'}},
                                                                {'player': 1, 'color': {'name': 'blue'}},
                                                                {'player': 0, 'color': {'name': 'red'}}
                                                            ],
                                                            [
                                                                {'player': 0, 'color': {'name': 'yellow'}},
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

    def test_makeTwoMoves(self):
        test_board = [[Tile("black", 1), Tile("blue", 0), Tile("red", 0)],
                    [Tile("yellow", 0), Tile("purple", 0), Tile("green", 0)],
                    [Tile("black", 0), Tile("blue", 0), Tile("red", 2)]]
        test_game = Game(test_board)
        test_game.makeMove(test_game.player_1, Color('blue'))
        test_game.makeMove(test_game.player_1, Color('yellow'))

        self.assertEqual(test_game.toJSON(), {'player_1': {'player_num': 1, 'color': {'name': 'yellow'}, 'score': 3},
                                                'board': {
                                                        'size': 3,
                                                        'colors': ['red', 'blue', 'green', 'purple', 'yellow', 'black'],
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

    def test_determineMove(self):
        test_board = [[Tile("black", 1), Tile("blue", 0), Tile("red", 0)],
                    [Tile("yellow", 0), Tile("purple", 0), Tile("green", 0)],
                    [Tile("black", 0), Tile("blue", 0), Tile("red", 2)]]
        test_game = Game(test_board)

        self.assertEqual(test_game.determineBestMove(test_game.player_1), {'blue': 1, 'yellow': 1})

if __name__ == '__main__':
    unittest.main()