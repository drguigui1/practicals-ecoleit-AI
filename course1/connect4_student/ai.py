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
    if game.winning(is_player=True):
        return -100 * (42 - game.total_number_pawns())
    elif game.winning(is_player=False):
        return 100 * (42 - game.total_number_pawns())
    
    # Use heuristique table
    return 0


def minimax_move(game: ConnectFour, depth: int, is_player: bool) -> List[int]:
    '''
    Implement the minimax algorithm, use 'heuristic_leaf' function
    '''
    best = [-1, +inf] if is_player else [-1, -inf]

    if depth == 0 or game.end_game():
        return [-1, heuristic_leaf(game)]

    for col in game.available():
        game.play(col, is_player)
        score = minimax_move(game, depth-1, not is_player)
        game.cancel(col)
        score[0] = col

        if not is_player:
            if score[1] > best[1]:
                best = score
        elif is_player:
            if score[1] < best[1]:
                best = score

    return best


def heuristic(game: ConnectFour, is_player: bool) -> int:
    '''
    Implement the heuristic function for any position of the game

    In this function you can use the heuristic table
    '''
    if game.winning(is_player=True):
        return -100 * (42 - game.total_number_pawns())
    elif game.winning(is_player=False):
        return 100 * (42 - game.total_number_pawns())
    elif len(game.available()) == 0:
        return 0

    s1, s2 = 0, 0
    for i in range(game.nb_lines):
        for j in range(game.nb_cols):
            if game.grid[i][j] == 1: # is_player
                s1 += game.heuristic_table[i][j]
            if game.grid[i][j] == 2:
                s2 += game.heuristic_table[i][j]

    if is_player:
        return s2 - s1
    return s1 - s2


def minimax_move_with_heuristic_table(game: ConnectFour, depth: int, is_player: bool):
    '''
    Implement the minimax algorithm using the 'heuristic' function
    '''
    best = [-1, +inf] if is_player else [-1, -inf]

    if depth == 0 or game.end_game():
        return [-1, heuristic(game)]

    for col in game.available():
        game.play(col, is_player)
        score = minimax_move(game, depth-1, not is_player)
        game.cancel(col)
        score[0] = col

        if not is_player:
            if score[1] > best[1]:
                best = score
        elif is_player:
            if score[1] < best[1]:
                best = score

    return best



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
    return minimax_move(game, 4, False)[0]
    # return generate_random_move(game)
