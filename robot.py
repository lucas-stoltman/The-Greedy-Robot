# Created by Lucas Stoltman
# Program 4
# April 29th, 2022
# CSS 340 A, Dimpsey
# Version: 1.0
import sys


class Robot:
    rx = 0
    ry = 0
    tx = 0
    ty = 0
    _num_paths = 0

    # constructor
    def __init__(self, x1: int = 0, y1: int = 0, x2: int = 0, y2: int = 0):
        rx = x1
        ry = y1
        tx = x2
        ty = y2

    # base case
    # check for cardinal treasure = the quickest path
    # if x = a or y = b

    # decide where treasure is
    # if x > a, y > b


class Point:
    _x = 0
    _y = 0

    def __init__(self, x1, y1):
        _x = x1
        _y = y1

    def get_x(self):
        return _x

    def get_y(self):
        return _y
