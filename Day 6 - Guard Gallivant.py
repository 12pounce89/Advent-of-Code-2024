'''
# Part 1

floor = []
visited = []
cycles = 0

with open('data/day6.txt') as file:
    for line in file:
        floor.append(list(line.strip()))
        visited.append(list(line.strip()))

for i, line in enumerate(floor):
    for j, place in enumerate(line):
        if place == "^":
            x, y = j, i
            direction = "up"
            floor[y][x] = "."
            visited[y][x] = "."

while True:
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
newObstructions = set()
last = "U"

with open('data/day6.txt') as file:
    for line in file:
        floor.append(list(line.strip()))
        visited.append(list(line.strip()))

for i, line in enumerate(floor):
    for j, place in enumerate(line):
        if place == "^":
            x, y = j, i
            direction = "up"
            floor[y][x] = "."
            visited[y][x] = "."

while True:
    if direction == "up":
        if y == 0:
            visited[y][x] = "U"
            break
        elif floor[y - 1][x] == ".":
            if visited[y][x] == "R":
                newObstructions.add(str(y - 1) + str(x))
            for i in range(x + 1, len(floor[y])):
                if visited[y][i] == "#":
                    break
                elif visited[y][i] == "R":
                    newObstructions.add(str(y - 1) + str(x))
                    break
                elif visited[y][i] == "U":
                    if visited[y - 1][i] == "#":
                        newObstructions.add(str(y - 1) + str(x))
                        break
            visited[y][x] = last
            last = "U"
            y -= 1
        elif floor[y - 1][x] == "#":
            direction = "right"
    elif direction == "right":
        if x == len(floor[y]) - 1:
            visited[y][x] = "R"
            break
        elif floor[y][x + 1] == ".":
            if visited[y][x] == "D":
                newObstructions.add(str(y) + str(x + 1))
            for i in range(y + 1, len(floor)):
                if visited[i][x] == "#":
                    break
                elif visited[i][x] == "D":
                    newObstructions.add(str(y) + str(x + 1))
                    break
                elif visited[i][x] == "R":
                    if visited[i][x + 1] == "#":
                        newObstructions.add(str(y) + str(x + 1))
                        break
            visited[y][x] = last
            last = "R"
            x += 1
        elif floor[y][x + 1] == "#":
            direction = "down"
    elif direction == "down":
        if y == len(floor) - 1:
            visited[y][x] = "D"
            break
        elif floor[y + 1][x] == ".":
            if visited[y][x] == "L":
                newObstructions.add(str(y + 1) + str(x))
            for i in range(x - 1, -1, -1):
                if visited[y][i] == "#":
                    break
                elif visited[y][i] == "L":
                    newObstructions.add(str(y + 1) + str(x))
                    break
                elif visited[y][i] == "D":
                    if visited[y + 1][i] == "#":
                        newObstructions.add(str(y + 1) + str(x))
                        break
            visited[y][x] = last
            last = "D"
            y += 1
        elif floor[y + 1][x] == "#":
            direction = "left"
    elif direction == "left":
        if x == 0:
            visited[y][x] = "L"
            break
        elif floor[y][x - 1] == ".":
            if visited[y][x] == "U":
                newObstructions.add(str(y) + str(x - 1))
            for i in range(y - 1, -1, -1):
                if visited[i][x] == "#":
                    break
                elif visited[i][x] == "U":
                    newObstructions.add(str(y) + str(x - 1))
                    break
                elif visited[i][x] == "L":
                    if visited[i][x - 1] == "#":
                        newObstructions.add(str(y) + str(x - 1))
                        break
            visited[y][x] = last
            last = "L"
            x -= 1
        elif floor[y][x - 1] == "#":
            direction = "up"

print(len(newObstructions))