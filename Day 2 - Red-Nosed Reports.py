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

# with open('data/day2.txt') as file:
#     for report in file:
#         levels = report.split()
#         running = True
#         removed = False
#         if int(levels[0]) > int(levels[1]):
#             pos = 0
#             while (pos < len(levels) - 1) and running:
#                 if ((int(levels[pos]) - int(levels[pos + 1])) > 3 or (int(levels[pos]) - int(levels[pos + 1])) < 1):
#                     if not removed and (pos < len(levels) - 2):
#                         if ((int(levels[pos]) - int(levels[pos + 2])) > 3 or (int(levels[pos]) - int(levels[pos + 2])) < 1):
#                             pos += 1
#                             removed = True
#                         else:
#                             running = False
#                 pos += 1
#             if pos >= int(len(levels)) - 2 and running:
#                 safe += 1
#         elif int(levels[0]) < int(levels[1]):
#             pos = 0
#             while (pos < len(levels) - 1) and running:
#                 if ((int(levels[pos]) - int(levels[pos + 1])) < -3 or (int(levels[pos]) - int(levels[pos + 1])) > -1):
#                     if not removed and (pos < len(levels) - 2):
#                         if ((int(levels[pos]) - int(levels[pos + 2])) < -3 or (int(levels[pos]) - int(levels[pos + 2])) > -1):
#                             pos += 1
#                             removed = True
#                         else:
#                             running = False
#                 pos += 1
#             if pos >= int(len(levels)) - 2 and running:
#                 safe += 1

safe = 0

def increasing_comparator(a, b):
    if ((a - b) < -3 or (a - b) > -1):
        return True
    return False

def decreasing_comparator(a, b):
    if ((a - b) > 3 or (a - b) < 1):
        return True
    return False

def checkIfSafe(levels, comparator):
    running = True
    pos = 0
    while (pos < len(levels) - 1) and running:
        if (comparator(int(levels[pos]), int(levels[pos + 1]))):
            running = False
        pos += 1
    if pos >= int(len(levels)) - 2 and running:
        return True
    else:
        return False


with open('data/day2.txt') as file:
    for report in file:
        levels = report.split()
        levelsTuple = tuple(levels)
        running = True
        if int(levels[0]) > int(levels[1]):
            test = checkIfSafe(levels, increasing_comparator)
        elif int(levels[0]) < int(levels[1]):
            test = checkIfSafe(levels, decreasing_comparator)
        if test:
            safe += 1
        else:
            for i in range(len(levels)):
                tester = list(levelsTuple)
                del tester[i]
            if int(tester[0]) > int(tester[1]):
                test = checkIfSafe(tester, increasing_comparator)
            elif int(tester[0]) < int(tester[1]):
                test = checkIfSafe(tester, decreasing_comparator)
            if test:
                safe += 1

print(safe)