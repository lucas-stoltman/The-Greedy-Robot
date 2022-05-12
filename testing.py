# Created by Lucas Stoltman
# Program 4
# April 29th, 2022
# CSS 340 A, Dimpsey
# Version: 1.0

import sys

from robot import Robot
from robot import Point
# TODO remove random
import random

# final input
# x1 = int(sys.argv[1])
# y1 = int(sys.argv[2])
# x2 = int(sys.argv[3])
# y2 = int(sys.argv[4])

x1 = 0
y1 = 0
x2 = random.randint(-5, 5)
y2 = random.randint(-5, 5)

# debugging arguments
print(f"Robot: ({x1},{y1})\n"
      f"Treasure: ({x2},{y2})")

rob = Robot(x1, y1)
treasure = Point(x2, y2)

# --- find_direction() ---
# print("\n---\033[1m", "find_direction()", "\033[0m---", )
# rob.find_direction(treasure)
# print("The treasure is:", rob.get_direction())
#
#
# --- find_paths() ---
print("\n---\033[1m", "find_paths()", "\033[0m---", )
rob.find_path(treasure)
rob.print_paths()


# # --- Movement Testing ---
# print("\n---\033[1m", "Movement Testing", "\033[0m---", )
# print("Origin: ", rob)
# rob.N()
# print("\t N: ", rob)
# rob.S()
# print("\t S: ", rob)
# rob.E()
# print("\t E: ", rob)
# rob.W()
# print("\t W: ", rob)
#
# # print("\n\n-----------------")
# print("\n\n---\033[1m", "overloads", "\033[0m---", )
# print("-----------------")
# # --- __str__() ---
# print("\n__str__()")
# print(rob)
#
# # --- __repr__() ---
# print("\n__repr__()")
# print(repr(rob))
#
# # --- __eq__() ---
# print("\n__eq__()")
# print("rob == treasure:", rob == treasure)
