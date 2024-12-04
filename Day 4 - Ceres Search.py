'''
# Part 1

grid = []
count = 0

with open('data/day4.txt') as file:
    for line in file:
        letters = list(line)
        grid.append(letters)

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 'X':
            if ((j + 3) < len(grid[i])):
                if grid[i][j + 1] == 'M' and grid[i][j + 2] == 'A' and grid[i][j + 3] == 'S':
                    count += 1
            if ((j + 3) < len(grid[i]) and (i + 3) < len(grid)):
                if grid[i + 1][j + 1] == 'M' and grid[i + 2][j + 2] == 'A' and grid[i + 3][j + 3] == 'S':
                    count += 1
            if ((i + 3) < len(grid)):
                if grid[i + 1][j] == 'M' and grid[i + 2][j] == 'A' and grid[i + 3][j] == 'S':
                    count += 1
            if ((j - 3) >= 0 and (i + 3) < len(grid)):
                if grid[i + 1][j - 1] == 'M' and grid[i + 2][j - 2] == 'A' and grid[i + 3][j - 3] == 'S':
                    count += 1
            if ((j - 3) >= 0):
                if grid[i][j - 1] == 'M' and grid[i][j - 2] == 'A' and grid[i][j - 3] == 'S':
                    count += 1
            if ((j - 3) >= 0 and (i - 3) >= 0):
                if grid[i - 1][j - 1] == 'M' and grid[i - 2][j - 2] == 'A' and grid[i - 3][j - 3] == 'S':
                    count += 1
            if ((i - 3) >= 0):
                if grid[i - 1][j] == 'M' and grid[i - 2][j] == 'A' and grid[i - 3][j] == 'S':
                    count += 1
            if ((j + 3) < len(grid[i]) and (i - 3) >= 0):
                if grid[i - 1][j + 1] == 'M' and grid[i - 2][j + 2] == 'A' and grid[i - 3][j + 3] == 'S':
                    count += 1



print(count)
# for item in newGrid:
#     for char in item:
#         print(char, end='')
#     print()
'''

# Part 2

grid = []
count = 0

with open('data/day4.txt') as file:
    for line in file:
        letters = list(line)
        grid.append(letters)


for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 'M':
            if j + 2 < len(grid[i]) and i + 2 < len(grid):
                if (grid[i][j + 2] == 'M' and grid[i + 1][j + 1] == 'A' and grid[i + 2][j] == 'S' and grid[i + 2][j + 2] == 'S'):
                    count += 1
                elif (grid[i + 2][j] == 'M' and grid[i + 1][j + 1] == 'A' and grid[i][j + 2] == 'S' and grid[i + 2][j + 2] == 'S'):
                    count += 1
            if i - 2 >= 0 and j + 2 < len(grid[i]):
                if (grid[i][j + 2] == 'M' and grid[i - 1][j + 1] == 'A' and grid[i - 2][j] == 'S' and grid[i - 2][j + 2] == 'S'):
                    count += 1
            if i + 2 < len(grid) and j - 2 >= 0:
                if (grid[i + 2][j] == 'M' and grid[i + 1][j - 1] == 'A' and grid[i][j - 2] == 'S' and grid[i + 2][j - 2] == 'S'):
                    count += 1


print(count)