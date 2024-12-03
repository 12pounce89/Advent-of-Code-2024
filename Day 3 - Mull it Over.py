# Part 1

import re

correct = []
sum = 0
on = True
testSum = 0

with open('data/day3.txt') as file:
    for line in file:
        correct += re.findall("mul\(\d+,\d+\)|do\(\)|don't\(\)", line)

for item in correct:
    if item == "do()":
        on = True
    elif item == "don't()":
        on = False
    elif on:
        broken = item.split(',')
        first = broken[0].split('(')
        second = broken[1].split(')')
        mult = int(first[1]) * int(second[0])
        sum += mult
    elif not on:
        broken = item.split(',')
        first = broken[0].split('(')
        second = broken[1].split(')')
        mult = int(first[1]) * int(second[0])
        testSum += mult

print(sum)
print(testSum)