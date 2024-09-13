# 2048 Game in Python

This project is a Python implementation of the classic 2048 game. The objective of the game is to slide numbered tiles on a grid and combine them to create a tile with the number 2048. This version supports the basic game mechanics like moving tiles in different directions, merging identical tiles, and adding new tiles after every move.

## Features

- **Move Tiles**: You can move tiles up, down, left, or right.
- **Merge Tiles**: Identical tiles merge when moved into each other, doubling their value.
- **Game State Check**: The game checks if you’ve won by reaching 2048, lost by having no more moves, or if the game is still ongoing.
- **Random Tile Generation**: After each move, a new tile with the value 2 is randomly generated in an empty spot on the grid.

## Class Breakdown

### `GameInterface`
An abstract base class (ABC) defining the following abstract methods for movement:
- `move_right()`
- `move_left()`
- `move_up()`
- `move_down()`

### `Game`
The main game logic is implemented in this class. It includes several key methods:
- `get_state()`: Determines whether the player has won, lost, or the game is still ongoing.
- `transpose()`: Transposes the game grid, useful for moving tiles vertically.
- `reverse()`: Reverses the grid for implementing moves in the opposite direction.
- `merge()`: Merges adjacent tiles with the same value.
- `compress()`: Moves all non-zero tiles to the left and fills the rest with zeros.
- `move_right()`, `move_left()`, `move_up()`, `move_down()`: Implements the game’s directional moves by combining compression, merging, and reversing logic.
- `arrange()`: Prints the current grid arrangement.
- `add_new_2()`: Adds a new tile with value 2 at a random empty spot after each move.

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/2048-game.git
   cd 2048-game
