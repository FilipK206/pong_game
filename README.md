# Pong Game

![pong_game](https://github.com/FilipK206/pong_game/assets/109867923/630f71e6-d94e-4dd9-ac22-ee9c02365a84)

This is a simple Pong game implemented in Python using the Pygame library.

## Description

Pong is a classic arcade game where players control paddles and try to hit a ball past their opponent's paddle. The game features a simple user interface and basic gameplay mechanics.

This repository contains the source code for a Python implementation of the Pong game. The game has been developed using the Pygame library. The primary file `main.py` contains the object-oriented version of the game code. The `pong.py` is the inital version of the game.

## Game Mechanics

The object-oriented version of the Pong game introduces several new mechanics:
- The game is organized into classes such as `Ball`, `Paddle`, and `Game` to improve code structure and maintainability.
- The `Ball` class manages the movement and collision of the ball, while the `Paddle` class handles the movement of the player and opponent paddles.
- Smooth movement of the opponent paddle has been implemented using interpolation, making the opponent's movements more natural and responsive.
- The game includes a main menu and result menu implemented as classes, allowing players to navigate through different game states seamlessly.

## Features

- Player vs. computer gameplay
- Score tracking
- Lives system
- Timer

![Welcome](https://github.com/FilipK206/pong_game/assets/109867923/53e985a8-207a-4495-8bb2-adebb622be5f)


## Usage

To play the game, simply run the `main.py` file using Python:

python main.py

## Controls

- Use the up and down arrow keys to control the player's paddle.
- The game starts when you click the mouse.

## Credits

This game was created by Filip Kozal.

