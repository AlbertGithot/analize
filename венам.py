saper = [
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,-2],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,1],
    [0,0,0,0,0,0,0,0,0,0,0],
    [2,0,0,0,0,0,0,0,0,0,0],
]

for row in range(len(saper)):
    if 1 in saper[row]:
        lenstroki = len(saper[row])
        indexodnerki = saper[row].index(1)
        if indexodnerki > lenstroki:
            saper[row][indexodnerki + 1] = 1
            saper[row][indexodnerki] = 0

for row in range(len(saper)):
    print(saper[row])
