"""
--- Day 6: Probably a Fire Hazard ---
Because your neighbors keep defeating you in the holiday house decorating contest year after year, you've decided to deploy one million lights in a 1000x1000 grid.

Furthermore, because you've been especially nice this year, Santa has mailed you instructions on how to display the ideal lighting configuration.

Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on, turn off, or toggle various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The lights all start turned off.

To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions Santa sent you in order.

For example:

turn on 0,0 through 999,999 would turn on (or leave on) every light.
toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on, and turning on the ones that were off.
turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.
After following the instructions, how many lights are lit?
"""

# Represent lights as a 2d 1000x1000 array. 0 means that lights are off, 1 means they are on
grid = [[0 for i in range(1000)] for j in range(1000)]

file = open("input.txt")

# Parse each line to determine to turn on, off, or toggle lights
for line in file:
    words = line.split(" ")
    # Turn off and on
    if words[0] == 'turn':
        row_start = int(words[2].split(',')[0])
        row_end = int(words[4].split(',')[0])
        col_start = int(words[2].split(',')[1])
        col_end = int(words[4].split(',')[1].split('\\')[0])
        # Turn off lights by setting their grid value to 0
        if words[1] == 'off':
            for i in range(row_end - row_start + 1):
                i += row_start
                for j in range(col_end - col_start + 1):
                    j += col_start
                    grid[i][j] = 0
        # Turn on lights by setting their grid value to 1
        elif words[1] == 'on':
            for i in range(row_end - row_start + 1):
                i += row_start
                for j in range(col_end - col_start + 1):
                    j += col_start
                    grid[i][j] = 1
        else:
            print("Invalid word")
    # Toggle lights in grid
    elif words[0] == 'toggle':
        row_start = int(words[1].split(',')[0])
        row_end = int(words[3].split(',')[0])
        col_start = int(words[1].split(',')[1])
        col_end = int(words[3].split(',')[1].split('\\')[0])
        for i in range(row_end - row_start + 1):
            i += row_start
            for j in range(col_end - col_start + 1):
                j += col_start
                # Turn off lights if they are on
                if grid[i][j] == 1:
                    grid[i][j] = 0
                # Turn on lights if they are off
                else:
                    grid[i][j] = 1
    else:
        print("Invalid word")

file.close()

total_on = 0
for row in grid:
    for col in row:
        if col == 1:
            total_on += 1

print(total_on)