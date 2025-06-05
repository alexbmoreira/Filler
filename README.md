# Filler

A filler game played against a computer.

## How to play

The goal is to fill as much of the board as you can.

You and the computer will each start with one square in the top left and bottom right corners, respectively.

Choose a color on the bottom to make your move.

After each choice, your square will join each of the adjacent squares that match your color. In other words, if your color is red, and you chooses blue, your cluster of squares will turn blue, and the number of blue squares adjacent to you will be added to your score.

![](https://i.ibb.co/rtKw4Jz/filler.gif)

The highest score after the board has been filled wins!

## Running the Flask server

Build and run with docker

```shell
docker compose up -d --build
```

Access the server at `localhost:5500`.

## Testing

```shell
docker compose exec filler python -m filler.tests.test_models
```
