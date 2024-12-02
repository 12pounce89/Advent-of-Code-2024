# Part 1
'''
safe = 0

with open('data/day2.txt') as file:
    for report in file:
        levels = report.split()
        running = True
        if int(levels[0]) > int(levels[1]):
            pos = 0
            while (pos < len(levels) - 1) and running:
                if ((int(levels[pos]) - int(levels[pos + 1])) > 3 or (int(levels[pos]) - int(levels[pos + 1])) < 1):
                    running = False
                pos += 1
            if pos >= int(len(levels)) - 2 and running:
                safe += 1
        elif int(levels[0]) < int(levels[1]):
            pos = 0
            while (pos < len(levels) - 1) and running:
                if ((int(levels[pos]) - int(levels[pos + 1])) < -3 or (int(levels[pos]) - int(levels[pos + 1])) > -1):
                    running = False
                pos += 1
            if pos >= int(len(levels)) - 2 and running:
                safe += 1

print(safe)
'''

# Part 2

safe = 0

with open('data/day2.txt') as file:
    for report in file:
        levels = report.split()
        running = True
        if int(levels[0]) > int(levels[1]):
            pos = 0
            while (pos < len(levels) - 1) and running:
                diff = int(levels[pos]) - int(levels[pos + 1])
                if (diff > 3 or diff < 1):
                    for i in range(len(levels)):
                        newPos = 0
                        newRunning = True
                        newLevels = levels[:i] + levels[i + 1:]
                        if int(newLevels[0]) > int(newLevels[1]):
                            while (newPos < len(newLevels) - 1) and newRunning:
                                diff = int(newLevels[newPos]) - int(newLevels[newPos + 1])
                                if (diff > 3 or diff < 1):
                                    newRunning = False
                                newPos += 1
                            if newPos >= int(len(newLevels)) - 2 and newRunning:
                                safe += 1
                                break
                        elif int(newLevels[0]) < int(newLevels[1]):
                            while (newPos < len(newLevels) - 1) and newRunning:
                                diff = int(newLevels[newPos]) - int(newLevels[newPos + 1])
                                if (diff < -3 or diff > -1):
                                    newRunning = False
                                newPos += 1
                            if newPos >= int(len(newLevels)) - 2 and newRunning:
                                safe += 1
                                break
                    running = False
                pos += 1
            if pos >= int(len(levels)) - 2 and running:
                safe += 1
        elif int(levels[0]) < int(levels[1]):
            pos = 0
            while (pos < len(levels) - 1) and running:
                diff = int(levels[pos]) - int(levels[pos + 1])
                if (diff < -3 or diff > -1):
                    for i in range(len(levels)):
                        newPos = 0
                        newRunning = True
                        newLevels = levels[:i] + levels[i + 1:]
                        if int(newLevels[0]) > int(newLevels[1]):
                            while (newPos < len(newLevels) - 1) and newRunning:
                                diff = int(newLevels[newPos]) - int(newLevels[newPos + 1])
                                if (diff > 3 or diff < 1):
                                    newRunning = False
                                newPos += 1
                            if newPos >= int(len(newLevels)) - 2 and newRunning:
                                safe += 1
                                break
                        elif int(newLevels[0]) < int(newLevels[1]):
                            while (newPos < len(newLevels) - 1) and newRunning:
                                diff = int(newLevels[newPos]) - int(newLevels[newPos + 1])
                                if (diff < -3 or diff > -1):
                                    newRunning = False
                                newPos += 1
                            if newPos >= int(len(newLevels)) - 2 and newRunning:
                                safe += 1
                                break
                    running = False
                pos += 1
            if pos >= int(len(levels)) - 2 and running:
                safe += 1
        elif(levels[0] == levels[1]):
            newLevels = levels[1:]
            pos = 0
            if (int(newLevels[0]) > int(newLevels[1])):
                while (pos < len(newLevels) - 1) and running:
                    diff = int(newLevels[pos]) - int(newLevels[pos + 1])
                    if (diff > 3 or diff < 1):
                        running = False
                    pos += 1
                if pos >= int(len(levels)) - 2 and running:
                    safe += 1
            if (int(newLevels[0]) < int(newLevels[1])):
                while (pos < len(newLevels) - 1) and running:
                    diff = int(newLevels[pos]) - int(newLevels[pos + 1])
                    if (diff < -3 or diff > -1):
                        running = False
                    pos += 1
                if pos >= int(len(levels)) - 2 and running:
                    safe += 1


print(safe)