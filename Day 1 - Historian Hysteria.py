'''
# Part 1

def increasing_comparator(a, b):
    if (a < b):
        return True
    return False

def decreasing_comparator(a, b):
    if (a >= b):
        return True
    return False

def bubble_sort(a_list, comparator=increasing_comparator):
    running = True
    while running:
        running = False
        for i in range(len(a_list) - 1):
            if (comparator(a_list[i + 1], a_list[i])):
                running = True
                temp = a_list[i]
                a_list[i] = a_list[i + 1]
                a_list[i + 1] = temp
    return a_list

first = []
second = []

with open('data/day1.txt') as file:
    for line in file:
        first.append(line.split()[0])
        second.append(line.split()[1])

first = bubble_sort(first)
second = bubble_sort(second)

sum = 0

for i in range(len(first)):
    sum += abs(int(first[i]) - int(second[i]))

print(sum)
'''

# Part 2

def increasing_comparator(a, b):
    if (a < b):
        return True
    return False

def decreasing_comparator(a, b):
    if (a >= b):
        return True
    return False

def bubble_sort(a_list, comparator=increasing_comparator):
    running = True
    while running:
        running = False
        for i in range(len(a_list) - 1):
            if (comparator(a_list[i + 1], a_list[i])):
                running = True
                temp = a_list[i]
                a_list[i] = a_list[i + 1]
                a_list[i + 1] = temp
    return a_list

first = []
second = []

with open('data/day1.txt') as file:
    for line in file:
        first.append(line.split()[0])
        second.append(line.split()[1])

first = bubble_sort(first)
second = bubble_sort(second)

score = 0

for item in first:
    count = 0
    for item2 in second:
        if (int(item) == int(item2)):
            count += 1
    score += int(item) * count

print(score)