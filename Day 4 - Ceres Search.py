# Part 1

grid = []
count = 0

with open('data/tester.txt') as file:
    for line in file:
        letters = list(line)
        grid.append(letters)

newGrid = [['.' for i in range(len(grid[0]))] for i in range(len(grid))]

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 'X':
            if ((j + 3) < len(grid[i])):
                if grid[i][j + 1] == 'M' and grid[i][j + 2] == 'A' and grid[i][j + 3] == 'S':
                    count += 1
                    newGrid[i][j] = 'X'
                    newGrid[i][j + 1] = 'M'
                    newGrid[i][j + 2] = 'A'
                    newGrid[i][j + 3] = 'S'
            if ((j + 3) < len(grid[i]) and (i + 3) < len(grid)):
                if grid[i + 1][j + 1] == 'M' and grid[i + 2][j + 2] == 'A' and grid[i + 3][j + 3] == 'S':
                    count += 1
                    newGrid[i][j] = 'X'
                    newGrid[i + 1][j + 1] = 'M'
                    newGrid[i + 2][j + 2] = 'A'
                    newGrid[i + 3][j + 3] = 'S'
            if ((i + 3) < len(grid)):
                if grid[i + 1][j] == 'M' and grid[i + 2][j] == 'A' and grid[i + 3][j] == 'S':
                    count += 1
                    newGrid[i][j] = 'X'
                    newGrid[i + 1][j] = 'M'
                    newGrid[i + 2][j] = 'A'
                    newGrid[i + 3][j] = 'S'
            if ((j - 3) > 0 and (i + 3) < len(grid)):
                if grid[i + 1][j - 1] == 'M' and grid[i + 2][j - 2] == 'A' and grid[i + 3][j - 3] == 'S':
                    count += 1
                    newGrid[i][j] = 'X'
                    newGrid[i + 1][j - 1] = 'M'
                    newGrid[i + 2][j - 2] = 'A'
                    newGrid[i + 3][j - 3] = 'S'
            if ((j - 3) > 0):
                if grid[i][j - 1] == 'M' and grid[i][j - 2] == 'A' and grid[i][j - 3] == 'S':
                    count += 1
                    newGrid[i][j] = 'X'
                    newGrid[i][j - 1] = 'M'
                    newGrid[i][j - 2] = 'A'
                    newGrid[i][j - 3] = 'S'
            if ((j - 3) > 0 and (i - 3) > 0):
                if grid[i - 1][j - 1] == 'M' and grid[i - 2][j - 2] == 'A' and grid[i - 3][j - 3] == 'S':
                    count += 1
                    newGrid[i][j] = 'X'
                    newGrid[i - 1][j - 1] = 'M'
                    newGrid[i - 2][j - 2] = 'A'
                    newGrid[i - 3][j - 3] = 'S'
            if ((i - 3) > 0):
                if grid[i - 1][j] == 'M' and grid[i - 2][j] == 'A' and grid[i - 3][j] == 'S':
                    count += 1
                    newGrid[i][j] = 'X'
                    newGrid[i - 1][j] = 'M'
                    newGrid[i - 2][j] = 'A'
                    newGrid[i - 3][j] = 'S'
            if ((j + 3) < len(grid[i]) and (i - 3) > 0):
                if grid[i - 1][j + 1] == 'M' and grid[i - 2][j + 2] == 'A' and grid[i - 3][j + 3] == 'S':
                    count += 1
                    newGrid[i][j] = 'X'
                    newGrid[i - 1][j + 1] = 'M'
                    newGrid[i - 2][j + 2] = 'A'
                    newGrid[i - 3][j + 3] = 'S'



print(count)
for item in newGrid:
    for char in item:
        print(char, end='')
    print()