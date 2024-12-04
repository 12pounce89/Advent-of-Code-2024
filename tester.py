with open ("data/day4.txt", "r") as file:
    data = file.read().rstrip().split("\n")

def p1(data):
    info=["XMAS", "SAMX"]
    total=0
    for i in data:
        for j in range(len(i)-3):
            if i[j:j+4] in info:
                total+=1
    for i in range(len(data[0])):
        for j in range(len(data)-3):
            if data[j][i]+data[j+1][i]+data[j+2][i]+data[j+3][i] in info:
                total+=1
    for i in range(len(data)-3):
        for j in range(len(data[0])-3):
            if data[i][j]+data[i+1][j+1]+data[i+2][j+2]+data[i+3][j+3] in info:
                total+=1
    for i in range(len(data)-3):
        for j in range(len(data[0])-3):
            if data[i][j+3]+data[i+1][j+2]+data[i+2][j+1]+data[i+3][j] in info:
                total+=1
    return total

print(p1(data))

def p2(data):
    info=["MAS", "SAM"]
    total=0
    for i in range(len(data)-2):
        for j in range(len(data[0])-2):
            if data[i][j]+data[i+1][j+1]+data[i+2][j+2] in info and data[i][j+2]+data[i+1][j+1]+data[i+2][j] in info:
                total+=1
    return total

#print(p2(data))