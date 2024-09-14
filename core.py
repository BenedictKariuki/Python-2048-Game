"""
    Author: Benedict Kariuki
    Date: September 14, 2024
    Version: 1.0
    Description: This program implements the 2048 Game developed by Gabriele Cirulli in March 2014 using Python.
"""
import random

from abc import ABC, abstractmethod
from .config import num_cols, num_rows


class GameInterface(ABC):
    @abstractmethod
    def move_right(self):
        pass

    @abstractmethod
    def move_left(self):
        pass

    @abstractmethod
    def move_up(self):
        pass

    @abstractmethod
    def move_down(self):
        pass


class Game(GameInterface):
    grid = []

    @classmethod
    def get_state(cls):
        # loop through the grid and if any cell contains 2048, we won
        for row in range(num_rows):
            for col in range(num_cols):
                if cls.grid[row][col] == 2048:
                    return "WON"
        # if after a move, an empty cell was created, game is not over
        for row in range(num_rows):
            for col in range(num_cols):
                if cls.grid[row][col] == 0:
                    return "GAME NOT OVER"

        # if there are two tiles that can be merged
        for row in range(num_rows - 1):
            for col in range(num_cols - 1):
                if cls.grid[row][col] == cls.grid[row][col + 1] or cls.grid[row][col] == cls.grid[row + 1][col]:
                    return "GAME NOT OVER"
        # checking the last row for tiles that can be merged
        for j in range(3):
            if cls.grid[3][j] == cls.grid[3][j + 1]:
                return "GAME NOT OVER"

        # checking the last column for tiles that can be merged
        for i in range(3):
            if cls.grid[i][3] == cls.grid[i + 1][3]:
                return "GAME NOT OVER"
        return "LOST"

    # for up and down moves, you need to transpose first
    @classmethod
    def transpose(cls):
        new_grid = []
        for row in range(num_rows):
            new_grid.append([])
            for col in range(num_cols):
                new_grid[row].append(cls.grid[col][row])
        return new_grid

    # for right moves, just reverse, move left, then reverse back
    @classmethod
    def reverse(cls):
        new_grid = []
        for row in range(num_rows):
            new_grid.append(cls.grid[row][::-1])
        return new_grid

    @classmethod
    def merge(cls):
        for row in range(num_rows):
            for col in range(num_cols - 1):
                # compare current cell and the next, if they are non-zero and contain same number
                if cls.grid[row][col] == cls.grid[row][col + 1] and cls.grid[row][col] != 0:
                    cls.grid[row][col] = cls.grid[row][col] * 2
                    cls.grid[row][col + 1] = 0
        return cls.grid

    @classmethod
    def compress(cls):
        # when compressing, you need move all non-zero elements to the left and fill the rest with zeros
        new_grid = [[0] * 4 for i in range(num_cols)]
        # iterate the grid row by row
        # we have to keep track of the current position of the new grid so that we insert elements there
        for row in range(num_rows):
            # keep track of the current position in the row (i.e. the column in the current row)
            pos = 0
            for col in range(num_cols):
                if cls.grid[row][col] != 0:
                    new_grid[row][pos] = cls.grid[row][col]
                    pos += 1
        return new_grid

    @classmethod
    def move_right(cls):
        # to move right, there are three steps:- reverse grid, move left, reverse back
        # reversing
        cls.grid = cls.reverse()
        # move left
        cls.move_left()
        # reverse back
        cls.grid = cls.reverse()

    @classmethod
    def move_up(cls):
        # to move up, three steps:- transpose grid, move left, then transpose back
        # transpose grid
        cls.grid = cls.transpose()
        # move left
        cls.move_left()
        # transpose back
        cls.grid = cls.transpose()

    @classmethod
    def move_left(cls):
        # move first
        cls.grid = cls.compress()
        # then merge
        cls.grid = cls.merge()
        # the merging operation may create empty cells, so move(compress) again
        cls.grid = cls.compress()

    @classmethod
    def move_down(cls):
        # to move right, three steps:- transpose grid, move right, transpose back
        # transpose
        cls.grid = cls.transpose()
        # move right
        cls.move_right()
        # transpose back
        cls.grid = cls.transpose()

    @classmethod
    def arrange(cls):
        for row in range(len(cls.grid)):
            print(str(cls.grid[row]))

    @classmethod
    def add_new_2(cls):
        # two random positions first time
        row = random.randint(0, 3)
        col = random.randint(0, 3)

        # keeping generating random nos until we find an empty spot
        while cls.grid[row][col] != 0:
            row = random.randint(0, 3)
            col = random.randint(0, 3)

        cls.grid[row][col] = 2
