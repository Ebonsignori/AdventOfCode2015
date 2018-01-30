"""
--- Part Two ---
You just finish implementing your winning light pattern when you realize you mistranslated Santa's message from Ancient Nordic Elvish.

The light grid you bought actually has individual brightness controls; each light can have a brightness of zero or more. The lights all start at zero.

The phrase turn on actually means that you should increase the brightness of those lights by 1.

The phrase turn off actually means that you should decrease the brightness of those lights by 1, to a minimum of zero.

The phrase toggle actually means that you should increase the brightness of those lights by 2.

What is the total brightness of all lights combined after following Santa's instructions?

For example:

turn on 0,0 through 0,0 would increase the total brightness by 1.
toggle 0,0 through 999,999 would increase the total brightness by 2000000.
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
                    if grid[i][j] > 0:
                        grid[i][j] -= 1
        # Turn on lights by setting their grid value to 1
        elif words[1] == 'on':
            for i in range(row_end - row_start + 1):
                i += row_start
                for j in range(col_end - col_start + 1):
                    j += col_start
                    grid[i][j] += 1
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
                grid[i][j] += 2
    else:
        print("Invalid word")

file.close()

total_brightness = 0
for row in grid:
    for col in row:
        total_brightness += col

print(total_brightness)