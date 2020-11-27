# Filler

A filler game played against a computer.

## How to play

The goal is to fill as much of the board as you can.

You and the computer will wach start with one square in the top left and bottom right corners, respectively.

Choose a color on the bottom to make your move.

After each choice, your square will join each of the adjacent squares that match your color. In other words, if your color is red, and you chooses blue, your cluster of squares will turn blue, and the number of blue squares adjacent to you will be added to your score.

The highest score after the board has been filled wins!

## Running the Flask server

Use a virtual environment and pip install dependencies:

```shell
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

Within the virtual environment, run the server:
```shell
export FLASK_APP=run.py
export FLASK_ENV=development
flask run
```

## Testing

```shell
python3 -m filler.tests.test_models
```
