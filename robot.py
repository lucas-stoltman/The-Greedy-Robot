# Created by Lucas Stoltman
# Program 4
# April 29th, 2022
# CSS 340 A, Dimpsey
# Version: 1.0
import sys


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


class Robot:
    # robot x
    _rx = 0
    # robot y
    _ry = 0

    # cardinal direction treasure is from robot
    _direction = ""
    _num_paths = 0

    # constructor
    def __init__(self, x1: int = 0, y1: int = 0):
        self._rx = x1
        self._ry = y1

    # base case
    # TODO check for cardinal treasure = the quickest path
    # def check_cardinal(self):
    #     if rx = tx or ry = ty:

    def get_direction(self):
        return self._direction

    # TODO decide where treasure is
    def find_direction(self, point: Point):
        # same x = N/S
        if self._rx == point.get_x():
            self._direction = "north/south"
        # same y = E/W
        elif self._ry == point.get_y():
            self._direction = "east/west"
        elif self._rx < point.get_x() and self._ry < point.get_y():
            self._direction = "northeast"
        elif self._rx < point.get_x() and self._ry > point.get_y():
            self._direction = "southeast"
        elif self._rx > point.get_x() and self._ry < point.get_y():
            self._direction = "northwest"
        elif self._rx > point.get_x() and self._ry > point.get_y():
            self._direction = "southwest"

    # TODO finish print
    def __str__(self):
        return f"{self._rx}, {self._ry}"

    def __repr__(self):
        return f"{self._rx}, {self._ry}, {self._tx}, {self._ty}"
