from typing import List

class ConnectFour:
    def __init__(self):
        self.title = "Connect4"
        self.nb_lines = 6
        self.nb_cols = 7
        self.color_symbol = ("_", "X", "O")
        self.heuristic_table = [ \
            [3, 4, 5, 7, 5, 4, 3], \
            [4, 6, 8, 10, 8, 6, 4], \
            [5, 8, 11, 13, 11, 8, 5], \
            [5, 8, 11, 13, 11, 8, 5], \
            [4, 6, 8, 10, 8, 6, 4], \
            [3, 4, 5, 7, 5, 4, 3] \
        ]

        self.grid = []
        for _ in range(self.nb_lines):
             self.grid.append(self.nb_cols * [0])

    def display(self):
        for row in self.grid:
            print(row)
        print("---------")

    def is_valid(self, col: int) -> int:
        '''
        Check if a move is valid or not
        '''
        if col < 0 or col >= self.nb_cols:
            return False
        # Check if we can put a pawn on the cell
        return self.grid[self.nb_lines-1][col] == 0

    def available(self) -> List[int]:
        '''
        List all the available columns to play
        '''
        l = []
        for row in range(self.nb_lines):
            if self.is_valid(row):
                l.append(row)
        return l

    def fall_line(self, col: int) -> int:
        '''
        Get the associated available line for a specific move in column 'col'
        '''
        line = 0
        while line < self.nb_lines-1 and self.grid[line][col] != 0:
            line += 1
        return line

    def drop(self, col: int, color: int):
        '''
        Update the value of a specific cell (from the input column)
        '''
        self.grid[self.fall_line(col)][col] = color

    def play(self, col: int, is_player: bool):
        '''
        Make a move
        '''
        # Put 1 in the grid if it is player turn otherwise put 0
        self.drop(col, 1 if is_player else 2)

    def symbol_move(self, color: int) -> str:
        '''
        Return symbole associated to the payer (or _ if no pawn)
        '''
        return self.color_symbol[color]

    def number_pawns_direction(self, inLine: int, inCol: int, inDirX: int, inDirY: int) -> int:
        '''
        Compute the number of pawns in a specific direction
        '''
        color = self.grid[inLine][inCol]
        numberPawns = 1

        line = inLine + inDirY
        col = inCol + inDirX
        while line < self.nb_lines and col < self.nb_cols and self.grid[line][col] == color:
            numberPawns += 1
            line = line + inDirY
            col = col + inDirX

        line = inLine - inDirY
        col = inCol - inDirX
        while line < self.nb_lines and col < self.nb_cols and self.grid[line][col] == color:
            numberPawns += 1
            line = line - inDirY
            col = col - inDirX

        return numberPawns

    def number_aligned_pawns(self, inLine: int, inRow: int):
        '''
        Compute for a specific position, the number of aligned pawns
        '''
        numberPawns = 1
        if self.grid[inLine][inRow] != 0:
            # test dans toutes les directions
            numberPawns = max(numberPawns, self.number_pawns_direction(inLine, inRow, 1, 1))
            numberPawns = max(numberPawns, self.number_pawns_direction(inLine, inRow, 1, 0))
            numberPawns = max(numberPawns, self.number_pawns_direction(inLine, inRow, 1, -1))
            numberPawns = max(numberPawns, self.number_pawns_direction(inLine, inRow, 0, 1))
        return numberPawns

    def is_player(self):
        '''
        Tell if its the human turn to play
        '''
        j1, j2 = 0, 0
        for i in range(self.nb_lines):
            for j in range(self.nb_cols):
                if self.grid[i][j] == 1:
                    j1 += 1
                if self.grid[i][j] == 2:
                    j2 += 1
        return j1 == j2

    def winning(self, is_player: bool) -> bool:
        '''
        Check if a player has won the game
        '''
        a = 0
        color = 1 if is_player else 2
        for i in range(self.nb_lines):
            for j in range(self.nb_cols):
                if self.grid[i][j] == color:
                    a = max(a, self.number_aligned_pawns(i, j))

        return a >= 4

    def end_game(self) -> bool:
        '''
        Tell of the game is finished or not
        '''
        if len(self.available()) == 0:
            return True
        return self.winning(self.is_player())

    def cancel(self, col: int):
        '''
        Cancel previous move on a specific column
        '''
        rank = 0
        while rank <  self.nb_lines and self.grid[rank][col] != 0:
            rank += 1
        rank = rank - 1
        self.grid[rank][col] = 0

    def total_number_pawns(self) -> int:
        '''
        Compute the total number of pawn
        '''
        n = 0
        for i in range(self.nb_lines):
            for j in range(self.nb_cols):
                if self.grid[i][j] != 0:
                    n += 1
        return n
