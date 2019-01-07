# 2048-expectminimax
I created an adversarial search agent to play the 2048-puzzle game using the expectiminimax algorithm. A demo ofthe game is available here: gabrielecirulli.github.io/2048.

- GameManager.py​. This is the driver program that loads your Computer AI and Player AI andbegins a game where they compete with each other. See below on how to execute this program.

- Grid.py​. This module defines the Grid object, along with some useful operations:move()​, ​getAvailableCells()​, ​insertTile()​, and ​clone()​.

- BaseAI.py​. This is the base class for any AI component. All AIs inherit from this module, andimplement the ​getMove()​ function, which takes a Grid object as parameter and returns a move (there aredifferent "moves" for different AIs).

- ComputerAI.py​. This inherits from BaseAI.

- PlayerAI.py​. The PlayerAI class should inherit from BaseAI. ThegetMove()​ function to implement must return a number that indicates the player’s action. In particular, ​0stands for "Up", 1 stands for "Down", 2 stands for "Left", and 3 stands for "Right"​.

- BaseDisplayer.py​ and ​Displayer.py​. These print the grid.
