import unittest

from ..filler.models import (Color, Board, Game)

class TestColor(unittest.TestCase):

    def test_toJSON(self):
        self.assertEqual(Color("Red").toJSON(), {'name': 'Red', 'count': 0})

class TestBoard(unittest.TestCase):

    def test_toJSON(self):
        test_board = [[Color("black"), Color("blue"), Color("red")],
                    [Color("yellow"), Color("purple"), Color("green")],
                    [Color("black"), Color("blue"), Color("red")]]

        self.assertEqual(Board(3, test_board).toJSON(), {'size': 3,
                                                        'colors': ['red', 'blue', 'green', 'purple', 'yellow', 'black'],
                                                        'grid': [
                                                            [
                                                                {'name': 'black', 'count': 0},
                                                                {'name': 'blue', 'count': 0},
                                                                {'name': 'red', 'count': 0}
                                                            ],
                                                            [
                                                                {'name': 'yellow', 'count': 0},
                                                                {'name': 'purple', 'count': 0},
                                                                {'name': 'green', 'count': 0}
                                                            ],
                                                            [
                                                                {'name': 'black', 'count': 0},
                                                                {'name': 'blue', 'count': 0},
                                                                {'name': 'red', 'count': 0}
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
                                                                    {'name': 'black', 'count': 0},
                                                                    {'name': 'blue', 'count': 0},
                                                                    {'name': 'red', 'count': 0}
                                                                ],
                                                                [
                                                                    {'name': 'yellow', 'count': 0},
                                                                    {'name': 'purple', 'count': 0},
                                                                    {'name': 'green', 'count': 0}
                                                                ],
                                                                [
                                                                    {'name': 'black', 'count': 0},
                                                                    {'name': 'blue', 'count': 0},
                                                                    {'name': 'red', 'count': 0}
                                                                ]
                                                            ]}
                                                        })

if __name__ == '__main__':
    unittest.main()