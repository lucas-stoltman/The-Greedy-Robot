# Created by Lucas Stoltman
# Program 4
# April 29th, 2022
# CSS 340 A, Dimpsey
# Version: 1.0
import sys


class Robot:
    # robot x
    rx = 0
    # robot y
    ry = 0

    # treasure x
    tx = 0
    # treasure y
    ty = 0

    _num_paths = 0

    # constructor
    def __init__(self, x1: int = 0, y1: int = 0, x2: int = 0, y2: int = 0):
        rx = x1
        ry = y1
        tx = x2
        ty = y2

    # base case
    # TODO check for cardinal treasure = the quickest path
    # def check_cardinal(self):
    #     if rx = tx or ry = ty:

    # TODO decide where treasure is
    # if x > a, y > b

    # TODO finish print
    def __str__(self):
        return f"{rx}, {ry}"

    def __repr__(self):
        return f"{rx}, {ry}, {tx}, {ty}"


class Point:
    _x = 0
    _y = 0

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    # TODO __str__
    # TODO __repr__
    # TODO __eq__
