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
    _path = ""
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
    def find_direction(self, treasure: Point):
        # base case
        if self._x == treasure.get_x() and self._y == treasure.get_y():
            self._direction = "beneath"

        # same x = directly N/S
        if self._x == treasure.get_x():
            if self._y < treasure.get_y():
                self._direction = "north"
            elif self._y > treasure.get_y():
                self._direction = "south"

        # same y = directly E/W
        elif self._y == treasure.get_y():
            if self._x < treasure.get_x():
                self._direction = "east"
            elif self._x > treasure.get_x():
                self._direction = "west"
        elif self._x < treasure.get_x() and self._y < treasure.get_y():
            self._direction = "northeast"
        elif self._x < treasure.get_x() and self._y > treasure.get_y():
            self._direction = "southeast"
        elif self._x > treasure.get_x() and self._y < treasure.get_y():
            self._direction = "northwest"
        elif self._x > treasure.get_x() and self._y > treasure.get_y():
            self._direction = "southwest"

    # TODO
    # print routes
    # update _num_paths
    # update _path
    def find_paths(self, treasure: Point):
        import random

        self.find_direction(treasure)
        # end case
        if self._direction == "beneath":
            return True
        elif self._direction == "north":
            self.N()
            self.find_paths(treasure)
        elif self._direction == "south":
            self.S()
            self.find_paths(treasure)
        elif self._direction == "east":
            self.E()
            self.find_paths(treasure)
        elif self._direction == "west":
            self.W()
            self.find_paths(treasure)
        elif self._direction == "northeast":
            num = random.randint(0, 1)
            if num == 0:
                self.N()
            else:
                self.E()
            self.find_paths(treasure)
        elif self._direction == "northwest":
            num = random.randint(0, 1)
            if num == 0:
                self.N()
            else:
                self.W()
            self.find_paths(treasure)
        elif self._direction == "southeast":
            num = random.randint(0, 1)
            if num == 0:
                self.S()
            else:
                self.E()
            self.find_paths(treasure)
        elif self._direction == "southwest":
            num = random.randint(0, 1)
            if num == 0:
                self.S()
            else:
                self.W()
            self.find_paths(treasure)
        else:
            print("Error")
            return False




    def print_path(self):
        return self._path

    # move North once
    def N(self):
        self._y += 1
        self._path += "N"
        return True

    # move South once
    def S(self):
        self._y -= 1
        self._path += "S"
        return True

    # move East once
    def E(self):
        self._x += 1
        self._path += "E"
        return True

    # move West once
    def W(self):
        self._x -= 1
        self._path += "W"
        return True

    # overloads
    def __str__(self):
        return f"({self._x}, {self._y})"

    def __repr__(self):
        return "{self.__class__.__name__}({self._x}, " \
               "{self._y})".format(self=self)

    def __eq__(self, treasure: Point):
        if self._x == treasure.get_x() and self._y == treasure.get_y():
            return True
        else:
            return False
