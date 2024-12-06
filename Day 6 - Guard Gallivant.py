'''
# Part 1

floor = []
visited = []
cycles = 0
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
direction = 0

with open('data/day6.txt') as file:
    for line in file:
        floor.append(list(line.strip()))
        visited.append(list(line.strip()))

for i, line in enumerate(floor):
    for j, place in enumerate(line):
        if place == "^":
            x, y = j, i
            floor[y][x] = "."
            visited[y][x] = "."

while True:
    cy, cx = directions[direction]
    visited[y][x] = "X"
    y, x = y + cy, x + cx
    if y < 0 or y >= len(floor) or x < 0 or x >= len(floor):
        break
    elif floor[y][x] == "#":
        y, x = y - cy, x - cx
        direction = (direction + 1) % 4

count = 0

for line in visited:
    for char in line:
        if char == "X":
            count += 1

print(count)
'''

# Part 2

floor = []
visited = []
cycles = 0
original = 0
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
direction = 0

with open('data/day6.txt') as file:
    for line in file:
        floor.append(list(line.strip()))
        visited.append(list(line.strip()))

for i, line in enumerate(floor):
    for j, place in enumerate(line):
        if place == "^":
            x, y = j, i
            start = (j, i)
            direction = "up"
            floor[y][x] = "."
            visited[y][x] = "."

while True:
    original += 1
    if direction == "up":
        if y == 0:
            visited[y][x] = "X"
            break
        elif floor[y - 1][x] == ".":
            visited[y][x] = "X"
            y -= 1
        elif floor[y - 1][x] == "#":
            direction = "right"
    elif direction == "right":
        if x == len(floor[y]) - 1:
            visited[y][x] = "X"
            break
        elif floor[y][x + 1] == ".":
            visited[y][x] = "X"
            x += 1
        elif floor[y][x + 1] == "#":
            direction = "down"
    elif direction == "down":
        if y == len(floor) - 1:
            visited[y][x] = "X"
            break
        elif floor[y + 1][x] == ".":
            visited[y][x] = "X"
            y += 1
        elif floor[y + 1][x] == "#":
            direction = "left"
    elif direction == "left":
        if x == 0:
            visited[y][x] = "X"
            break
        elif floor[y][x - 1] == ".":
            visited[y][x] = "X"
            x -= 1
        elif floor[y][x - 1] == "#":
            direction = "up"

for k in range(len(visited)):
    for l in range(len(visited[k])):
        if visited[k][l] == "X":
            visited[k][l] = "."

found = 0

for i in range(len(floor)):
    for j in range(len(floor[i])):
        cycles = 0
        x, y = start
        direction = "up"
        if floor[i][j] == ".":
            floor[i][j] = "#"
            visited[i][j] = "#"
            while True and cycles < original * 10:
                cycles += 1
                if direction == "up":
                    if y == 0:
                        visited[y][x] = "U"
                        break
                    elif floor[y - 1][x] == ".":
                        visited[y][x] = "U"
                        y -= 1
                    elif floor[y - 1][x] == "#":
                        direction = "right"
                elif direction == "right":
                    if x == len(floor[y]) - 1:
                        visited[y][x] = "R"
                        break
                    elif floor[y][x + 1] == ".":
                        visited[y][x] = "R"
                        x += 1
                    elif floor[y][x + 1] == "#":
                        direction = "down"
                elif direction == "down":
                    if y == len(floor) - 1:
                        visited[y][x] = "D"
                        break
                    elif floor[y + 1][x] == ".":
                        visited[y][x] = "D"
                        y += 1
                    elif floor[y + 1][x] == "#":
                        direction = "left"
                elif direction == "left":
                    if x == 0:
                        visited[y][x] = "L"
                        break
                    elif floor[y][x - 1] == ".":
                        visited[y][x] = "L"
                        x -= 1
                    elif floor[y][x - 1] == "#":
                        direction = "up"
            if cycles >= original * 10:
                found += 1
            floor[i][j] = "."
            visited[i][j] = "."
            for k in range(len(visited)):
                for l in range(len(visited[k])):
                    if visited[k][l] != "#":
                        visited[k][l] = "."

print(found)