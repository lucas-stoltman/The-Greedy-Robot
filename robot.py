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


class Robot:
    # variables
    _x = 0
    _y = 0
    _num_paths = 0

    # cardinal direction from robot -> treasure
    _direction = ""

    # constructor
    def __init__(self, x1: int = 0, y1: int = 0):
        self._x = x1
        self._y = y1

    # getters
    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_direction(self):
        return self._direction

    # methods
    def find_direction(self, point: Point):
        # base case
        if self._x == point.get_x() and self._y == point.get_y():
            self._direction = "beneath"

        # same x = directly N/S
        if self._x == point.get_x():
            if self._y < point.get_y():
                self._direction = "north"
            elif self._y > point.get_y():
                self._direction = "south"

        # same y = directly E/W
        elif self._y == point.get_y():
            if self._x < point.get_x():
                self._direction = "east"
            elif self._x > point.get_x():
                self._direction = "west"
        elif self._x < point.get_x() and self._y < point.get_y():
            self._direction = "northeast"
        elif self._x < point.get_x() and self._y > point.get_y():
            self._direction = "southeast"
        elif self._x > point.get_x() and self._y < point.get_y():
            self._direction = "northwest"
        elif self._x > point.get_x() and self._y > point.get_y():
            self._direction = "southwest"

    # overloads
    def __str__(self):
        return f"({self._x}, {self._y})"

    def __repr__(self):
        return "{self.__class__.__name__}({self._x}, " \
               "{self._y})".format(self=self)

    def __eq__(self, point: Point):
        if self._x == point.get_x() and self._y == point.get_y():
            return True
        else:
            return False
