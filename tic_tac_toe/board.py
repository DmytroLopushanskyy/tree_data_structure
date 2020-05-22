"""
Module for Board class.
"""
import random
import copy
from btree import LinkedBinaryTree
from btnode import Node


class Board:
    """
    Represents 3x3 board for tic-tac-toe game.
    """
    def __init__(self, board=None):
        """
        Game board representation.
        """
        if not board:
            board = [[None, None, None],
                     [None, None, None],
                     [None, None, None]]
        self.board = board
        self.first_player = "⭕"
        self.second_player = "❌"
        self.automated_player = None
        self.solutions_tree = None

    def place(self, index, symbol):
        """
        Places the given symbol onto the board. Raises OccupiedError
        if place is occupied or IndexError if index is not within 1-9 range.
        """
        board = self.board

        index -= 1
        if not 0 <= index <= 8:
            raise IndexError("Index not in range 1-9")
        if board[index // 3][index % 3] is not None:
            raise OccupiedError("Place is already occupied")

        board[index // 3][index % 3] = symbol

    def check_status(self):
        """
        Checks board status, whether there is a win or draw.
        Returns tuple of status and additional info. e.g.
        ('finished', 'o') - o has won
        ('finished', 'draw') or ('in progress', '')
        :return: (bool, str)
        """
        # check horizontal
        for row in self.board:
            if row[0] == row[1] == row[2] and row[0] is not None:
                return 'finished', row[0]

        # check vertical
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col]:
                if self.board[0][col] is not None:
                    return 'finished', self.board[0][col]

        # check diagonal
        if self.board[0][0] == self.board[1][1] == self.board[2][2]:
            if self.board[0][0] is not None:
                return 'finished', self.board[0][0]

        if self.board[0][2] == self.board[1][1] == self.board[2][0]:
            if self.board[0][2] is not None:
                return 'finished', self.board[0][2]

        return 'in progress', ''

    def build_solutions_tree(self, test_board, index, mark, side):
        """
        Builds a binary tree to find the best next move.
        """
        test_board = Board(copy.deepcopy(test_board.board))

        if mark:
            symbol = self.second_player
        else:
            symbol = self.first_player
        mark = not mark
        test_board.place(index, symbol)
        node = Node(test_board)

        if side == "left":
            self.solutions_tree.insert_left(node)
        else:
            self.solutions_tree.insert_right(node)

        free_places = test_board.get_free_places()

        if len(free_places) == 1:
            return self.build_solutions_tree(test_board, free_places[0], mark, "left")
        if len(free_places) == 0:
            status = test_board.check_status()
            if status[1] == self.first_player:
                return -1
            if status[1] == self.second_player:
                return 1
            return 0

        index_1, index_2 = random.sample(free_places, 2)

        result = 0
        result += self.build_solutions_tree(test_board, index_1, mark, "left")
        result += self.build_solutions_tree(test_board, index_2, mark, "right")
        return result

    def take_turn(self):
        """
        Compute next turn to win the game
        """
        self.solutions_tree = LinkedBinaryTree(Node(self))
        index_1, index_2 = random.sample(self.get_free_places(), 2)

        res_1 = self.build_solutions_tree(self, index_1, self.second_player, "left")
        res_2 = self.build_solutions_tree(self, index_2, self.second_player, "right")

        if res_1 >= res_2:
            self.place(index_1, self.second_player)
        else:
            self.place(index_2, self.second_player)

    def get_free_places(self):
        """
        Returns unoccupied places of the board.
        :return: list
        """
        unoccupied = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] is None:
                    unoccupied.append(i * 3 + j + 1)
        return unoccupied

    def __str__(self):
        """
        String board representation.
        """
        result = ""
        for i in range(3):
            for j in range(3):
                if self.board[i][j]:
                    result += str(self.board[i][j])
                else:
                    result += "  "
                if j != 2:
                    result += " | "
            result += "\n"
        return result


class OccupiedError(Exception):
    """
    Exception indicates that the place is already occupied.
    """
