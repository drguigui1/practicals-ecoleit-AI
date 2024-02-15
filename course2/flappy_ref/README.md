# TP Genetic Algorithm for Flappy Bird Game

In this TP we are going to implement Genetic Algorithms to play Flappy Bird game.

## Important

Project structure:

- `main.py`: Entrypoint of the projet (containing the code to launch the game with or without GA models)

- `game_manager.py`: Main part of the project with all the functions to run the game

- `utils.py`: Containing utils functions

- `brain.py`: This is the file you need to modify to implement the GA algorithms

- `bird.py`: This file contains the implementation of each bird, you also have to modify few things in this file. In this file you have to implement the replication / mutation functions.

## Steps

This TP is mainly divided into 2 parts:

- Implement a Neural Network genetic algorithm

- Implement a Tree based genetic algorithm


### Neural Network GA

Implement a simple neural network genetic algorithm in the file `brain.py` and implement the mutation / replication in the file `bird.py`


### Tree based GA

Implement a simple Tree based model. Generate the trees randomly with a spécified depth.
Each path of the tree must be a decision: jump or not.
Each node of the tree is made based on specific conditions that you can apply on the input.
For instance:

                   x_dist_obstacle < 10
                    /               \
         y_dist_obstacle < 5   y_dist_obstacle >= 10
            /           \            /         \
          Jump        No jump     Jump       No jump
            