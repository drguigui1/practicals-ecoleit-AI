#
# Entrypoint
#

import sys

from game_manager import GameManager


def main():
    with_ai = False
    if len(sys.argv) > 1 and sys.argv[1] == "ai":
        with_ai = True

    manager = GameManager(board_width=500, board_height=766)
    manager.setup_board()

    if not with_ai:
        # Game with manual play
        manager.game_loop_manual()
    else:
        # Game with AI birds
        # You can change the number of birds here
        # FIXME
        birds = manager.initialize_ai_birds(nb_birds=30)
        manager.game_loop_with_ai(nb_it=1000, birds=birds)


if __name__ == "__main__":
    main()
