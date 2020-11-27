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
                                                        'colors': [
                                                            {'name': 'red', 'available': True},
                                                            {'name': 'blue', 'available': True},
                                                            {'name': 'green', 'available': True},
                                                            {'name': 'purple', 'available': True},
                                                            {'name': 'yellow', 'available': True},
                                                            {'name': 'black', 'available': True}
                                                            ],
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
                                                    'computer': {'player_num': 2, 'color': {'name': 'red'}, 'score': 1},
                                                    'board': {
                                                            'size': 3,
                                                            'colors': [
                                                            {'name': 'red', 'available': True},
                                                            {'name': 'blue', 'available': True},
                                                            {'name': 'green', 'available': True},
                                                            {'name': 'purple', 'available': True},
                                                            {'name': 'yellow', 'available': True},
                                                            {'name': 'black', 'available': True}
                                                            ],
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
        test_game.player_1.makeMove(test_game.board, Color('blue'))

        self.assertEqual(test_game.toJSON(), {'player_1': {'player_num': 1, 'color': {'name': 'blue'}, 'score': 2},
                                                'computer': {'player_num': 2, 'color': {'name': 'red'}, 'score': 1},
                                                'board': {
                                                        'size': 3,
                                                        'colors': [
                                                            {'name': 'red', 'available': True},
                                                            {'name': 'blue', 'available': True},
                                                            {'name': 'green', 'available': True},
                                                            {'name': 'purple', 'available': True},
                                                            {'name': 'yellow', 'available': True},
                                                            {'name': 'black', 'available': True}
                                                            ],
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
                                                            {'name': 'yellow', 'available': True},
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
        test_board = [[Tile("black", 1), Tile("blue", 0), Tile("red", 0)],
                    [Tile("yellow", 0), Tile("purple", 0), Tile("green", 0)],
                    [Tile("black", 0), Tile("blue", 0), Tile("red", 2)]]
        test_game = Game(test_board)

        self.assertEqual(test_game.computer.possibleMoves(test_game.board), {'green': 1, 'blue': 1})

    def test_makeThenFindPossible(self):
        test_board = [[Tile("black", 1), Tile("blue", 0), Tile("red", 0)],
                    [Tile("yellow", 0), Tile("purple", 0), Tile("green", 0)],
                    [Tile("black", 0), Tile("blue", 0), Tile("red", 2)]]
        test_game = Game(test_board)
        test_game.computer.makeMove(test_game.board, Color('blue'))

        self.assertEqual(test_game.computer.possibleMoves(test_game.board), {'black': 1, 'green': 1, 'purple': 1})
    
    def test_determineBest(self):
        test_board = [[Tile("black", 1), Tile("black", 1), Tile("yellow", 0)],
                    [Tile("yellow", 0), Tile("purple", 0), Tile("green", 0)],
                    [Tile("purple", 0), Tile("red", 2), Tile("red", 2)]]
        test_game = Game(test_board)

        self.assertEqual(test_game.computer.determineBestMove(test_game.board).toJSON(), {'name': 'purple'})
    
    def test_aiMoveMaking(self):
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
                                                            {'name': 'purple', 'available': True},
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