import time
import sys
import os
import math


# TODO:
# https://math.libretexts.org/Bookshelves/Applied_Mathematics/Mathematics_for_Game_Developers_(Burzynski)/04%3A_Matrices/4.06%3A_Rotation_Matrices_in_3-Dimensions
# function(3): given a vector and a rotation, calculate each of x,y,z with a rotation applied using a rotation matrix
# function: given a vector on the surface of a cube and a rotation, calculate the rotated vector and draw a character at the vector's location
# function: given the cube's dimensions and a rotation, draw the cube
# TODO:
# Animate ASCII Spinning Cube
# - while loop
#     - calculate next position in spin
#     - clear screen
#     - print cube in new position
#     - pause by duration relative to framerate
FRAME_TIME: float = 1/25

def calculate_rotation_x(vector: tuple[int,int,int], rotation: float) -> int:
    pass

def calculate_rotation_y(vector: tuple[int,int,int], rotation: float) -> int:
    pass

def calculate_rotation_z(vector: tuple[int,int,int], rotation: float) -> int:
    pass

def calculate_rotation(vector: tuple[int,int,int], rotation: float) -> tuple[int,int,int]:
    return (calculate_rotation_x(vector,rotation),
            calculate_rotation_y(vector,rotation),
            calculate_rotation_z(vector,rotation))

def draw_cube_vector_rotated(vector: tuple[int,int,int], rotation: float) -> None:
    rotated_vector: tuple[int,int,int] = calculate_rotation(vector, rotation)
    # TODO:

def draw_cube(length: int, rotation: float) -> None:
    # TODO: nested for loop across entire canvas with (x,y) coordinates
    pass

def main():
    pass

if __name__ == "__main__":
    main()
