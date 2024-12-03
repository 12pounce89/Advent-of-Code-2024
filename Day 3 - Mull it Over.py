'''
# Part 1

import re

correct = []
sum = 0

with open('data/day3.txt') as file:
    for line in file:
        correct += re.findall("mul\(\d+,\d+\)", line)

for item in correct:
    broken = item.split(',')
    first = broken[0].split('(')
    second = broken[1].split(')')
    mult = int(first[1]) * int(second[0])
    sum += mult

print(sum)
'''

# Part 2

import re

correct = []
sum = 0
on = True

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

print(sum)