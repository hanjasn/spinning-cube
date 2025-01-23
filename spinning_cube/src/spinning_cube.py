import time
import sys
import os
import math


# TODO:
# - eight points of the cube and their position in 3D space
# - adjacency list to represent the points and edges of the cube
# - function: draw sides of cube with point and edge data and return as string
#     - add a transparency effect
#         - directly visible edges are dark-colored
#         - edges visible through cube are light-colored
#         - sides are a shade between the shades of the edges
#
# A physical representation of a cube that represents its position and orientation in 3D space. Printing the cube returns an ASCII drawing of the cube.
class Cube:
    def __init__(self) -> None:
        self.adj_list: dict = {} # TODO:

    def __repr__(self) -> str:
        return ""


# TODO:
# Spinning
# - the cube will follow a point (follow_point) on the xy-plane on the display as its spinning direction
#     - e.g. (0,0) the cube is stationary, (1,0) the cube spins rightwards, (0,-1) the cube spins downwards, etc.
# - the cube will spin along the xz-plane and yz-plane relative to the point's location on the xy-plane
# - spin velocity = degrees/sec which is a function of the point's distance
#     - the spin velocity and frame time can be used to draw the next frame of the cube
# - function: calculate next position of cube
# - make the point move in a circle so that the for a more interesting spin effect
# TODO:
# Animate ASCII Spinning Cube
# - while loop
#     - calculate next position in spin
#     - clear screen
#     - print cube in new position
#     - pause by duration relative to framerate
class SpinningCube:
    # Specifies the wait time in time.sleep(FRAME_TIME)
    FRAME_TIME: float = 1/25

    def __init__(self, follow_point: tuple[float,float]=(0,1), cube: Cube=Cube()) -> None:
        self.cube: Cube = cube
        if follow_point[0] < -1 or follow_point[0] > 1  or follow_point[1] < -1 or follow_point[1] > 1:
            raise ValueError("Point must be within range of (-1,-1) and (1,1)")
        # Follow point values are float values that range from -1 to 1 relative to its location on the xy-plane
        self.follow_point: tuple[float,float] = follow_point

    def animate_cube(self) -> None:
        pass
        # while True:
        #     os.system('cls')
        #     for _ in range(10):
        #         sys.stdout.write("11111111111111111111111\n")
        #     time.sleep(0.04)

    # Multiplies x and y values instead of using power operator for efficiency
    def calculate_follow_point_distance(self) -> float:
        return math.sqrt(self.follow_point[0]*self.follow_point[0] + self.follow_point[1]*self.follow_point[1])

def main():
    spinning_cube: SpinningCube = SpinningCube((0,0))
    spinning_cube.animate_cube()

if __name__ == "__main__":
    main()
