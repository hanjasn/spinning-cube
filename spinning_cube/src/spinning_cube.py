import time
import sys
import os
import math

'''
Design
- model x,y,z axes for a shape object w/ a center point (0,0)
- draw the sides relative to the axes
- add a transparency effect
    - directly visible edges are dark
    - edges visible through sides are light
    - sides are a shade between the shades of the edges
- function: calculate next position of cube
- function: draw cube and return as string

Spinning
- the cube will follow a point (follow_point) on the xy-plane on the display as its spinning direction
    - e.g. (0,0) the cube is stationary, (1,0) the cube spins rightwards, (0,-1) the cube spins downwards, etc.
- the cube will spin along the xz-plane and yz-plane relative to the point's location on the xy-plane
- spin velocity = degrees/sec which is a function of the point's distance
    - the spin velocity and frame time can be used to draw the next frame of the cube
- make the point move in a circle so that the final spin varies

Animate ASCII Spinning Cube
- while loop
    - calculate next position in spin
    - clear screen
    - print cube in new position
    - pause by duration relative to framerate
'''

class SpinningCube:
    # Specifies the wait time in time.sleep(FRAME_TIME)
    FRAME_TIME: float = 1/25

    def __init__(self, follow_point: tuple[float,float]=(0,-1)) -> None:
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
    def _calculate_follow_point_distance(self) -> float:
        return math.sqrt(self.follow_point[0]*self.follow_point[0] + self.follow_point[1]*self.follow_point[1])

def main():
    spinning_cube: SpinningCube = SpinningCube((0,0))
    spinning_cube.animate_cube()

if __name__ == "__main__":
    main()
