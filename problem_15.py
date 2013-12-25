# Starting in the top left corner of a 2x2 grid,
# and only being able to move to the right and down, 
# there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 20x20 grid?

# Use combinatorics:
# 40 choose 20

import math

def lattice_paths(grid_width):
    top = math.factorial(grid_width * 2)
    bottom = math.factorial(grid_width * 2 - grid_width) * math.factorial(grid_width)

    answer = top / bottom

    return answer

if __name__ == "__main__":
    print lattice_paths(20)