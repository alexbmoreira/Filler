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
        test_board = [[Color("black"), Color("blue"), Color("red")],
                    [Color("yellow"), Color("purple"), Color("green")],
                    [Color("black"), Color("blue"), Color("red")]]

        self.assertEqual(Board(3, test_board).toJSON(), {'size': 3,
                                                        'colors': ['red', 'blue', 'green', 'purple', 'yellow', 'black'],
                                                        'grid': [
                                                            [
                                                                {'name': 'black'},
                                                                {'name': 'blue'},
                                                                {'name': 'red'}
                                                            ],
                                                            [
                                                                {'name': 'yellow'},
                                                                {'name': 'purple'},
                                                                {'name': 'green'}
                                                            ],
                                                            [
                                                                {'name': 'black'},
                                                                {'name': 'blue'},
                                                                {'name': 'red'}
                                                            ]
                                                        ]})

class TestGame(unittest.TestCase):

    def test_toJSON(self):
        test_board = [[Color("black"), Color("blue"), Color("red")],
                    [Color("yellow"), Color("purple"), Color("green")],
                    [Color("black"), Color("blue"), Color("red")]]

        self.assertEqual(Game(test_board).toJSON(), {'board': {
                                                            'size': 3,
                                                            'colors': ['red', 'blue', 'green', 'purple', 'yellow', 'black'],
                                                            'grid': [
                                                                [
                                                                    {'name': 'black'},
                                                                    {'name': 'blue'},
                                                                    {'name': 'red'}
                                                                ],
                                                                [
                                                                    {'name': 'yellow'},
                                                                    {'name': 'purple'},
                                                                    {'name': 'green'}
                                                                ],
                                                                [
                                                                    {'name': 'black'},
                                                                    {'name': 'blue'},
                                                                    {'name': 'red'}
                                                                ]
                                                            ]}
                                                        })

if __name__ == '__main__':
    unittest.main()