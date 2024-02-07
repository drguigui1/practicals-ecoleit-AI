import random
from math import inf
from typing import List

from connect4 import ConnectFour


# Available functions / attributes in ConnectFour
# game.available(): List all the available columns
# game.winning(is_player): Check if the player or the ai has won the game
# game.play(col, is_player): Play a move (put a pawn on the specified column)
# game.cancel(col): Cancel the last move on the specified column
# game.total_number_pawns(): Number of pawn in the game (maximum is 42)
# game.nb_rows / game.nb_lines / game.grid (1 in the grid is for the player while 2 in the grid is for the ai, 0 is for empty cell)
# game.heuristic_table: Table that can use as weight in your heuristic function (to evaluate state of the board)


def generate_random_move(game: ConnectFour):
    available_cols = game.available()
    idx = random.randint(0, len(available_cols)-1)
    return available_cols[idx]


def naive_move(game: ConnectFour):
    '''
    If you can win, put the pawn
    If your opponant can win, put the pawn to block
    Otherwise play random

    No need recursive call in this function
    '''
    # FIXME
    pass


def heuristic_leaf(game: ConnectFour) -> int:
    '''
    Implement the heuristic function for the minimax algorithm but only in the case of a leaf

    In Connect4 the leaf mean someone has won the game
    Implement the heuristic function to make your algorithm minize the distance between the current state of the board of the winning position
    '''
    # FIXME
    pass


def minimax_move(game: ConnectFour, depth: int, is_player: bool) -> List[int]:
    '''
    Implement the minimax algorithm, use 'heuristic_leaf' function
    '''
    # FIXME
    pass


def heuristic(game: ConnectFour, is_player: bool) -> int:
    '''
    Implement the heuristic function for any position of the game

    In this function you can use the heuristic table
    '''
    # FIXME
    pass


def minimax_move_with_heuristic_table(game: ConnectFour, depth: int, is_player: bool):
    '''
    Implement the minimax algorithm using the 'heuristic' function
    '''
    # FIXME
    pass


def alpha_beta_move(game: ConnectFour):
    '''
    Implement the Alpha beta algorithm
    '''
    # FIXME
    pass


def generate_move(game: ConnectFour) -> int:
    '''
    Generate the idx of the column to get at each step of the game
    idx must be in: [1, 7]
    '''
    # Replace by the functions you want to call
    return generate_random_move(game)
