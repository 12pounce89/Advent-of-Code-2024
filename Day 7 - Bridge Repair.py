'''
# Part 1

testValues = []
numbers = []

with open('data/day7.txt') as file:
    for line in file:
        brokenLine = line.strip().split(":")
        testValues.append(int(brokenLine[0].strip()))
        numbers.append(brokenLine[1].strip().split())

sum = 0

for lineNum, tester in enumerate(testValues):
    for i in range(2 ** (len(numbers[lineNum]) - 1)):
        binary = bin(i)[2:]
        for i in range(len(numbers[lineNum]) - 1 - len(binary)):
            binary = "0" + binary
        total = int(numbers[lineNum][0])
        for j in range(len(numbers[lineNum]) - 1):
            if total > tester:
                break
            if binary[j] == "0":
                total += int(numbers[lineNum][j + 1])
            elif binary[j] == "1":
                total *= int(numbers[lineNum][j + 1])
        if total == tester:
            sum += tester
            break

print(sum)
'''

# Part 2

testValues = []
numbers = []

with open('data/day7.txt') as file:
    for line in file:
        brokenLine = line.strip().split(":")
        testValues.append(int(brokenLine[0].strip()))
        numbers.append(brokenLine[1].strip().split())

sum = 0

def trin(x):
    if x == 0:
        return "0"
    result = ""
    while x > 0:
        result = str(x % 3) + result
        x //= 3
    return result

for lineNum, tester in enumerate(testValues):
    for i in range(3 ** (len(numbers[lineNum]) - 1)):
        trinary = trin(i)
        for i in range(len(numbers[lineNum]) - 1 - len(trinary)):
            trinary = "0" + trinary
        total = int(numbers[lineNum][0])
        for j in range(len(numbers[lineNum]) - 1):
            if total > tester:
                break
            if trinary[j] == "0":
                total += int(numbers[lineNum][j + 1])
            elif trinary[j] == "1":
                total *= int(numbers[lineNum][j + 1])
            elif trinary[j] == "2":
                total = int(str(total) + numbers[lineNum][j + 1])
        if total == tester:
            sum += tester
            break

print(sum)