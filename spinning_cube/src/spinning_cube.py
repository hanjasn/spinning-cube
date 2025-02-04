import time
import sys
import os
import math


# TODO:
# https://math.libretexts.org/Bookshelves/Applied_Mathematics/Mathematics_for_Game_Developers_%28Burzynski%29/04%3A_Matrices/4.06%3A_Rotation_Matrices_in_3-Dimensions
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

def calculate_rotation_x(vector: tuple[float,float,float], rotation: float) -> tuple[float,float,float]:
    sine: float = math.sin(rotation)
    cosine: float = math.cos(rotation)
    x: float = vector[0]
    y: float = cosine*vector[1] - sine*vector[2]
    z: float = sine*vector[1] + cosine*vector[2]
    return (x,y,z)

def calculate_rotation_y(vector: tuple[float,float,float], rotation: float) -> tuple[float,float,float]:
    sine: float = math.sin(rotation)
    cosine: float = math.cos(rotation)
    x: float = cosine*vector[0] + sine*vector[2]
    y: float = vector[1]
    z: float = -sine*vector[0] + cosine*vector[2]
    return (x,y,z)

def calculate_rotation_z(vector: tuple[float,float,float], rotation: float) -> tuple[float,float,float]:
    sine: float = math.sin(rotation)
    cosine: float = math.cos(rotation)
    x: float = cosine*vector[0] - sine*vector[1]
    y: float = sine*vector[0] + cosine*vector[1]
    z: float = vector[2]
    return (x,y,z)

def calculate_rotation(vector: tuple[float,float,float], rotation: float) -> tuple[float,float,float]:
    return calculate_rotation_z(calculate_rotation_y(calculate_rotation_x(vector, rotation), rotation), rotation)

def draw_cube_vector_rotated(vector: tuple[float,float,float], rotation: float) -> None:
    rotated_vector: tuple[float,float,float] = calculate_rotation(vector, rotation)
    # TODO:

def draw_cube(length: int, rotation: float) -> None:
    # TODO: nested for loop across entire canvas with (x,y) coordinates
    pass

def main():
    pass

if __name__ == "__main__":
    main()
