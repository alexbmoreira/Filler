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

        self.assertEqual(Game(test_board).toJSON(), {'player_1': {'player_num': 1, 'color': {'name': 'black'}, 'score': 0},
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

if __name__ == '__main__':
    unittest.main()