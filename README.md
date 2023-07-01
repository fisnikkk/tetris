# Tetris Game

This is a simple implementation of the classic game Tetris using the Pygame library. The game features falling blocks that the player must manipulate to form complete lines and score points.

## Prerequisites

To run this code, you need to have Pygame installed. You can install it using pip:

pip install pygame

## Usage

To start the game, simply run the code. The game window will open, and you can use the following controls:

- Left arrow key: Move the current piece to the left.
- Right arrow key: Move the current piece to the right.
- Down arrow key: Move the current piece down faster.
- Spacebar: Rotate the current piece.

The goal of the game is to fill complete lines with blocks. When a line is filled, it clears, and the player earns points. The game ends when the blocks reach the top of the screen.

## Code Structure

The code is organized as follows:

- Pygame initialization and game window setup.
- Game board setup and utility functions for checking collision, adding pieces to the board, and clearing lines.
- Piece class representing the falling blocks and their movement and rotation.
- Function for generating new pieces.
- Game loop handling user input, updating the game state, and rendering the game window.
- Functions for drawing the game board and pieces, and checking for game over.

## Customization

You can customize the game by modifying the following variables:

- `WINDOW_WIDTH` and `WINDOW_HEIGHT`: Width and height of the game window.
- `BLOCK_SIZE`: Size of each block in pixels.
- `BOARD_WIDTH` and `BOARD_HEIGHT`: Width and height of the game board in number of blocks.
- `shapes`: List of different block shapes.
- `colors`: List of colors corresponding to each block shape.
- `update_score`: Function to determine the score based on the number of cleared lines.
- Frame rate: You can adjust the frame rate by changing the argument passed to `clock.tick()`.

## Acknowledgements

This code is inspired by the classic game Tetris and the Pygame library.
