# Copyright (c) Hoshmand. All rights reserved.
# 
# https://twitter.com/hoshmandctf
# https://github.com/hoshmandctf

def lattice_paths(grid_size):
    # Create a grid to store the number of paths to each point
    grid = [[0] * (grid_size + 1) for _ in range(grid_size + 1)]

    # Initialize the boundary values
    for i in range(grid_size + 1):
        grid[i][grid_size] = 1
        grid[grid_size][i] = 1

    # Fill in the grid using dynamic programming
    for i in range(grid_size - 1, -1, -1):
        for j in range(grid_size - 1, -1, -1):
            grid[i][j] = grid[i + 1][j] + grid[i][j + 1]

    # Return the number of paths to the top left corner
    return grid[0][0]

# Set the grid size to 20x20
grid_size = 20

# Call the function to find the number of lattice paths
result = lattice_paths(grid_size)
print("The number of lattice paths in a", grid_size, "x", grid_size, "grid is:", result)
