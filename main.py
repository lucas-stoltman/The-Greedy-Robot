# Created by Lucas Stoltman
# Program 4
# April 29th, 2022
# CSS 340 A, Dimpsey
# Version: 1.0

import sys

from robot import Robot
from robot import Point

x1 = int(sys.argv[1])
y1 = int(sys.argv[2])
x2 = int(sys.argv[3])
y2 = int(sys.argv[4])

# x1 = 0
# y1 = 0
# x2 = 2
# y2 = 2

# debugging arguments
# print(f"Robot: ({x1},{y1})\n"
#       f"Treasure: ({x2},{y2})")

rob = Robot(x1, y1)
treasure = Point(x2, y2)

rob.find_direction(treasure)
rob.find_path(treasure, x1, y1)
rob.get_num_paths()
