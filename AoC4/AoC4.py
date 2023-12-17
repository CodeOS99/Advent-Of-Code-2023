Totalpoints = 0
totNums = 0
allBoth = []
def pointize(atHand, winning, name):
    points1 = 0.5
    num = 0
    ticketsGotten  = []
    for each in atHand:
        if each in winning:
            points1 *= 2
            num+=1
    if points1 != 0.5:
        for each in range(int(num)):
            ticketsGotten.append(name+int(each))
    return ticketsGotten

def startProc(line):
    nums = 0
    name = int(line.split(":")[0][5:])
    print(name)
    both = line.split(":")[1].split("|")
    #           To INT                ( ALL THE CASES )
    winning = [int(each) for each in both[0].strip().split()]
    #           To INT                ( ALL THE CASES )
    atHand = [int(each) for each in both[1].strip().split()]
    ticketsGot = pointize(atHand, winning, name)
    print(ticketsGot)
    for each in ticketsGot:
        numToAdd = startProc(allBoth[each])
        nums+=1+numToAdd
    return nums
with open('AoC4.txt', 'r') as f:

    lines = f.readlines()
    allBoth = [line for line in lines]
    for line in lines:
        print("___________________________________________________________--------------------")
        gotNums = startProc(line)
        totNums+=1 + gotNums
    print(int(totNums)+len(allBoth))
    print(len(allBoth))

