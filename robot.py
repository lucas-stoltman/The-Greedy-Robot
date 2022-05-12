# Created by Lucas Stoltman
# Program 4
# April 29th, 2022
# CSS 340 A, Dimpsey
# Version: 1.0


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
    def find_direction(self, treasure: Point, x=_x, y=_x):
        # base case
        if x == treasure.get_x() and y == treasure.get_y():
            self._direction = "arrived"

        # same x = directly N/S
        if x == treasure.get_x():
            if y < treasure.get_y():
                self._direction = "north"
            elif y > treasure.get_y():
                self._direction = "south"

        # same y = directly E/W
        elif y == treasure.get_y():
            if x < treasure.get_x():
                self._direction = "east"
            elif x > treasure.get_x():
                self._direction = "west"

        elif x < treasure.get_x() and y < treasure.get_y():
            self._direction = "northeast"
        elif x < treasure.get_x() and y > treasure.get_y():
            self._direction = "southeast"
        elif x > treasure.get_x() and y < treasure.get_y():
            self._direction = "northwest"
        elif x > treasure.get_x() and y > treasure.get_y():
            self._direction = "southwest"

    def find_path(self, treasure: Point, x=_x, y=_x, path_string=""):

        # check direction
        self.find_direction(treasure, x, y)

        if self._direction == "arrived":
            self._num_paths += 1
            print(path_string)
            print(self._num_paths)
            return True

        # north case
        if self._direction == "north":
            if y < treasure.get_y():
                y += 1
                path_string += "N"
                self.find_path(treasure, x, y, path_string)
        # south case
        elif self._direction == "south":
            if y > treasure.get_y():
                y -= 1
                path_string += "S"
                self.find_path(treasure, x, y, path_string)
        # east case
        elif self._direction == "east":
            if x < treasure.get_x():
                x += 1
                path_string += "E"
                self.find_path(treasure, x, y, path_string)
        # west case
        elif self._direction == "west":
            if x > treasure.get_x():
                x -= 1
                path_string += "W"
                self.find_path(treasure, x, y, path_string)

        else:
            print("ERROR")
            return False

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
