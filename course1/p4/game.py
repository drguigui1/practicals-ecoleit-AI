import pygame
from pygame.locals import *
from connect4 import ConnectFour
from ai import generate_move


def init_pygame():
    pygame.init()
    window = pygame.display.set_mode((900, 576), RESIZABLE)
    return window

def load_assets():
    assets = {
        "grid": pygame.image.load("assets/grid.png").convert_alpha(),
        "menu": pygame.image.load("assets/menu.png").convert_alpha(),
        "yellow_pawn": pygame.image.load("assets/yellow_pawn.png").convert_alpha(),
        "red_pawn": pygame.image.load("assets/red_pawn.png").convert_alpha(),
        "ai_wins": pygame.image.load("assets/ai_win.png").convert_alpha(),
        "play_wins": pygame.image.load("assets/win_player.png").convert_alpha()
    }
    return assets

def draw_initial_screen(window, assets):
    window.blit(assets["grid"], (0, 0))
    window.blit(assets["menu"], (673, 0))

def get_column_from_click(pos):
    if pos[0] < 96:
        return 0
    if pos[0]>100 and pos[0]<192:
        return 1
    if pos[0]>196 and pos[0]<288:
        return 2
    if pos[0]>292 and pos[0]<384:
        return 3
    if pos[0]>388 and pos[0]<480:
        return 4
    if pos[0]>484 and pos[0]<576:
        return 5
    if pos[0]>580 and pos[0]<672:
        return 6
    return None


def handle_move(game, window, assets, X_pawn, Y_pawn, col, is_player):
    line = game.fall_line(col)
    game.play(col, is_player)
    pawn = assets["yellow_pawn"] if is_player else assets["red_pawn"]
    window.blit(pawn, (X_pawn[col], Y_pawn[line]))

    if game.number_aligned_pawns(line, col) >= 4:
        win_img = assets["play_wins"] if is_player else assets["ai_wins"]
        window.blit(win_img, (673, 430))
        return True

    return False

def reset_game(window, assets):
    draw_initial_screen(window, assets)
    return ConnectFour()

def main_graphic():
    X_pawn = [9,105,201,297,393,489,585]
    Y_pawn = [488,392,296,200,104,8]

    window = init_pygame()
    assets = load_assets()
    draw_initial_screen(window, assets)
    game = ConnectFour()
    pygame.display.flip()
    continuing = True
    end_game = False

    while continuing:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if 707 < event.pos[0] < 837 and 300 < event.pos[1] < 410:
                    game = reset_game(window, assets)
                    end_game = False
                else:
                    if not end_game:
                        column = get_column_from_click(event.pos)
                        if column is not None and game.is_valid(column):
                            end_game = handle_move(game, window, assets, X_pawn, Y_pawn, column, True)
                            if end_game:
                                continue
                            pygame.display.flip()
                            col = generate_move(game)
                            end_game = handle_move(game, window, assets, X_pawn, Y_pawn, col, False)
            if event.type == QUIT:
                continuing = False
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main_graphic()
