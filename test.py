from board import *

import unittest


class TestBoard(unittest.TestCase):

    def test_is_board_created_empty(self):
        board = Board()
        for x in range(6):
            for y in range(6):
                self.assertEqual(board[x][y], Pieces.Empty)

    def test_are_pieces_added_every_time(self):
        board = Board()
        for _ in range(36):
            pos = board.add_a_random_piece()
            self.assertNotEqual(board[pos[0]][pos[1]], Pieces.Empty)


class TestWinningList(unittest.TestCase):

    def test_is_winning_list(self):
        all_red = [Pieces.Red for _ in range(6)]
        all_blue = [Pieces.Blue for _ in range(6)]
        all_empty = [Pieces.Empty for _ in range(6)]

        self.assertTrue(is_winning_list(all_red))
        self.assertTrue(is_winning_list(all_blue))
        self.assertFalse(is_winning_list(all_empty))

    def test_empty_list(self):
        self.assertFalse(is_winning_list([]))

    def test_short_lists(self):
        for length in range(5):
            blue_list = [Pieces.Blue for _ in range(length)]
            red_list = [Pieces.Red for _ in range(length)]

            self.assertEqual(len(blue_list), length)
            self.assertEqual(len(red_list), length)

            self.assertFalse(is_winning_list(blue_list))
            self.assertFalse(is_winning_list(red_list))

    def test_broken_line(self):
        broken_red = [Pieces.Red for _ in range(6)]
        broken_red[3] = Pieces.Blue

        broken_blue = [Pieces.Blue for _ in range(6)]
        broken_blue[3] = Pieces.Red

        self.assertFalse(is_winning_list(broken_red))
        self.assertFalse(is_winning_list(broken_blue))


class TestGetDiagonals(unittest.TestCase):
    def setUp(self):
        self.board = []
        for x in range(6):
            self.board.append([x * 10 + y for y in range(6)])


    def test_get_diagonals(self):
        diagonals = get_diagonals_from_list(self.board, (0, 0))
        expect = [[0, 11, 22, 33, 44, 55], []]

        self.assertListEqual(diagonals, expect)

    def test_get_diagonals_2(self):
        diagonals = get_diagonals_from_list(self.board, (2, 4))
        expect = [[2, 13, 24, 35], [15, 24, 33, 42, 51]]

        self.assertListEqual(diagonals, expect)

    def test_get_diagonals_3(self):
        diagonals = get_diagonals_from_list(self.board, (3, 3))
        expect = [[0, 11, 22, 33, 44, 55], [15, 24, 33, 42, 51]]

        self.assertListEqual(diagonals, expect)

if __name__ == "__main__":
    unittest.main()
