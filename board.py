from enum import Enum
from random import randrange, choice


def get_first_pos(keys, items):
    if not isinstance(keys, list):
        keys = [keys]

    positions = []
    for item in keys:
        try:
            pos = items.index(item)
            positions.append(pos)
        except ValueError:
            positions.append(None)
    return positions


def is_winning_list(list: list) -> bool:
    """check if the passed list has 5 pieces in row"""

    if len(list) < 5:
        return False

    # Check if red has won this list
    num_reds = list.count(Pieces.Red)

    if num_reds == len(list):
        return True

    if num_reds >= 5:
        non_red_pos = get_first_pos([Pieces.Blue, Pieces.Empty], list)
        if non_red_pos in [0, 6]:
            print("red win")
            return True

    # Check if blue has won this list
    num_blues = list.count(Pieces.Blue)

    if num_blues == len(list):
        return True

    if num_blues >= 5:
        non_blue_pos = get_first_pos([Pieces.Red, Pieces.Empty], list)
        if non_blue_pos in [0, 6]:
            print("blue win")
            return True

    return False


def get_diagonals_from_list(target_list, pos: tuple):
    diagonals = [[], []]
    pos_start = None
    if pos[0] > pos[1]:
        pos_start = [pos[0] - pos[1], 0]
    else:
        pos_start = [0, pos[1] - pos[0]]

    neg_start = [0, pos[0] + pos[1]]
    if neg_start[1] > 5:
        diff = neg_start[1] - 5
        neg_start[1] -= diff
        neg_start[0] = diff

    # print("pos", pos)
    # print("pos_start", pos_start)
    # print("neg_start", neg_start)

    pos_coords = zip(range(pos_start[0], 6), range(pos_start[1], 6))
    neg_coords = zip(range(neg_start[0], 6), range(neg_start[1], 0, -1))

    # print("pos_coords", list(pos_coords))
    # print("neg_coords", list(neg_coords))

    for coord in pos_coords:
        diagonals[0].append(target_list[coord[0]][coord[1]])

    for coord in neg_coords:
        diagonals[1].append(target_list[coord[0]][coord[1]])

    return diagonals


class Board:

    def __init__(self):
        self.board = []
        self.added_coords = []  # done to check randrange thing
        for _ in range(6):
            self.board.append([Pieces.Empty for y in range(6)])

    def __str__(self):
        output = " 012345\n"
        for index, row in enumerate(self.board):
            output += str(index)
            for item in row:
                if item is Pieces.Empty:
                    output += "\033[95m."
                elif item is Pieces.Red:
                    output += "\033[94mX"
                elif item is Pieces.Blue:
                    output += "\033[91mO"
            output += "\n"
        return output

    def __getitem__(self, index):
        return self.board[index]

    def __setitem__(self, index, value):
        self.board[index] = value

    def add_a_random_piece(self):
        piece = choice([Pieces.Blue, Pieces.Red])
        return self.add_a_piece(piece)

    def add_a_piece(self, piece) -> tuple:
        while True:  # Loop until piece is added in empty place
            x = randrange(0, len(self.board))
            y = randrange(0, len(self.board[0]))

            if self.board[x][y] is Pieces.Empty:
                self.added_coords.append((x, y))
                self.board[x][y] = piece
                return (x, y)

    def has_move_won(self, pos):
        """ check if the previous move won the game"""
        x = pos[0]
        y = pos[1]

        vertical = self.board[x]
        horizontal = []
        for column in self.board:
            horizontal.append(column[y])

        diagonals = get_diagonals_from_list(self, pos)

        return(is_winning_list(vertical)
               or is_winning_list(horizontal))


class Pieces(Enum):
    Red = 1
    Blue = 2
    Empty = 3
