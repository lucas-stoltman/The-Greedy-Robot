# Created by Lucas Stoltman
# Program 4
# April 29th, 2022
# CSS 340 A, Dimpsey
# Version: 1.0

import sys

from robot import Robot
from robot import Point

# final input
# x1 = int(sys.argv[1])
# y1 = int(sys.argv[2])
# x2 = int(sys.argv[3])
# y2 = int(sys.argv[4])

x1 = 1
y1 = 1
x2 = 1
y2 = 1

# debugging arguments
print(f"Robot: ({x1},{y1})\n"
      f"Treasure: ({x2},{y2})")

treasure = Point(x2, y2)
rob = Robot(x1, y1)

# --- find_direction() ---
print("\n---\033[1m", "find_direction()", "\033[0m---", )
rob.find_direction(treasure)
print("The treasure is:", rob.get_direction())

