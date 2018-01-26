"""
--- Day 3: Perfectly Spherical Houses in a Vacuum ---
Santa is delivering presents to an infinite two-dimensional grid of houses.

He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next. Moves are always exactly one house to the north (^), south (v), east (>), or west (<). After each move, he delivers another present to the house at his new location.

However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa ends up visiting some houses more than once. How many houses receive at least one present?

For example:

> delivers presents to 2 houses: one at the starting location, and one to the east.
^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.
"""


class Grid:
    def __init__(self):
        # Initialize map of houses as a 3x3 grid.
        self.grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        # Track Santa's location with santa_row and column indexes. He begins at 1,1 (Middle of 3x3 square grid)
        self.row = 1
        self.col = 1

        # Make sure Santa delivers at his starting location
        self.grid[self.row][self.col] += 1

    def up(self):
        self.row += 1
        # Update grid size to accommodate for new house
        if self.row > len(self.grid) - 1:
            # Insert a santa_row at end of grid and fill it with empty houses
            self.grid.append([0 for col in self.grid[0]])
        # Update house with a delivery from santa
        self.grid[self.row][self.col] += 1

    def down(self):
        if self.row <= 0:
            # Update grid size to accommodate for new house
            # Insert a santa_row at beginning of grid and fill it with empty houses
            self.grid.insert(0, [0 for col in self.grid[1]])
        else:
            self.row -= 1

        # Update house with a delivery from santa
        self.grid[self.row][self.col] += 1

    def right(self):
        self.col += 1
        # Update grid size to accommodate for new house
        if self.col > len(self.grid[0]) - 1:
            # Insert a santa_col at end of each santa_row in the grid
            for row in self.grid:
                row.append(0)
        # Update house with a delivery from santa
        self.grid[self.row][self.col] += 1

    def left(self):
        if self.col <= 0:
            # Update grid size to accommodate for new house
            # Insert a santa_col at beginning of each santa_row in the grid
            for row in self.grid:
                row.insert(0, 0)
        else:
            self.col -= 1

        # Update house with a delivery from santa
        self.grid[self.row][self.col] += 1


grid = Grid()


# Get problem input from input.txt file
file = open("input.txt", 'r')

# Iterate through directions from elf (characters) and update santa's change in position
for line in file:
    for ch in line:
        # Increment each house that santa visits via elf directions
        if ch is '^':
            # Move up
            grid.up()
        elif ch is 'v':
            # Move down
            grid.down()
        elif ch is '<':
            # Move left
            grid.left()
        elif ch is '>':
            # Move right
            grid.right()
        else:
            print("Invalid direction")

# Close file
file.close()

total_houses = 0
for row in grid.grid:
    for col in row:
        if col >= 1:
            total_houses += 1

print("Total houses visited by Santa = " + str(total_houses))
