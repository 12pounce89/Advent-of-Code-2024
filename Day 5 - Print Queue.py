'''
# Part 1

rules = []
queues = []

with open('data/day5.txt') as file:
    for line in file:
        if line == "" or line == "\n":
            pass
        elif line[2] == "|":
            rules.append(line.strip().split('|'))
        elif line[2] == ',':
            listed = line.strip().split(',')
            myDict = dict()
            for i, item in enumerate(listed):
                myDict[item] = i
            queues .append(myDict)

passed = True
sum = 0

for queue in queues:
    passed = True
    for item in rules:
        if item[0] in queue and item[1] in queue:
            if queue[item[0]] > queue[item[1]]:
                passed = False
                break
    if passed:
        for key in queue:
            if queue[key] == len(queue) // 2:
                sum += int(key)

print(sum)
'''

# Part 2

rules = []
queues = []

with open('data/day5.txt') as file:
    for line in file:
        if line == "" or line == "\n":
            pass
        elif line[2] == "|":
            rules.append(line.strip().split('|'))
        elif line[2] == ',':
            listed = line.strip().split(',')
            myDict = dict()
            for i, item in enumerate(listed):
                myDict[item] = i
            queues.append(myDict)

passed = True
sum = 0
failed = True
failedQueues = []

for queue in queues:
    passed = True
    for item in rules:
        if item[0] in queue and item[1] in queue:
            if queue[item[0]] > queue[item[1]]:
                passed = False
                while True:
                    if not failed:
                        failed = True
                        break
                    failed = False
                    for item2 in rules:
                        if item2[0] in queue and item2[1] in queue:
                            if queue[item2[0]] > queue[item2[1]]:
                                temp = queue[item2[0]]
                                queue[item2[0]] = queue[item2[1]]
                                queue[item2[1]] = temp
                                failed = True
                break
    if not passed:
        failedQueues.append(queue)
        for key in queue:
            if queue[key] == len(queue) // 2:
                sum += int(key)

print(sum)