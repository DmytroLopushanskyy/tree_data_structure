"""
Module for Board class.
"""
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
        self.human_player = None
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

    def build_solutions_tree(self, test_board, index, mark):
        """
        Builds solution tree for finding the best next move.
        """
        test_board = Board(copy.deepcopy(test_board.board))

        if mark:
            symbol = self.automated_player
        else:
            symbol = self.human_player
        mark = not mark
        test_board.place(index, symbol)

        free_places = test_board.get_free_places()

        status = test_board.check_status()
        if status[1] == self.human_player:
            # multiply by coefficient to make the speed of reaching
            # the lost game more valuable
            return -1 * (len(free_places) ** 10 + 1)
        if status[1] == self.automated_player:
            return 1 * (len(free_places) ** 10 + 1)

        if len(free_places) == 1:
            return self.build_solutions_tree(test_board, free_places[0], mark)
        if len(free_places) == 0:
            return 0

        result = 0
        for ind in free_places:
            result += self.build_solutions_tree(test_board, ind, mark)
        return result

    def take_turn(self):
        """
        Compute next turn to win the game
        """
        self.solutions_tree = LinkedBinaryTree(Node(self))
        indexes = self.get_free_places()
        result = []

        for ind in indexes:
            result.append(self.build_solutions_tree(self, ind, True))

        best_choice = indexes[result.index(max(result))]
        self.place(best_choice, self.automated_player)

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

    def is_full(self):
        """
        Check if board is full
        """
        if len(self.get_free_places()) == 0:
            return True
        return False

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
