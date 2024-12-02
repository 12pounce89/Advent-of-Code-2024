InputList = []
with open("data/day2.txt", "r") as data:
    for t in data:
        Line = t.strip()
        Line = tuple(map(int, Line.split()))
        InputList.append(Line)

def CheckIfSafe(InTuple):
    Increase = None
    for n in range(len(InTuple)-1):
        a, b = InTuple[n], InTuple[n+1]
        Diff = b - a
        if Diff == 0 or abs(Diff) > 3:
            return False
        elif Diff > 0 and Increase == None:
            Increase = True
        elif Diff < 0 and Increase == None:
            Increase = False
        elif (Diff > 0 and not(Increase)) or (Diff < 0 and Increase):
            return False
    return True

Part1Answer = 0
Part2Answer = 0
for o in InputList:
    if CheckIfSafe(o):
        Part1Answer += 1
        Part2Answer += 1
        continue

    for n in range(len(o)):
        NewList = list(o)
        del NewList[n]
        NewTuple = tuple(NewList)
        if CheckIfSafe(NewTuple):
            Part2Answer += 1
            break

print(f"{Part1Answer = }")
print(f"{Part2Answer = }")