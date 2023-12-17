possibles = []
with open('AoC6.txt', 'r') as f:
    lines = f.readlines()
    timesP1 = [int(each) for each in lines[0].removesuffix("\n").split()[1:]]
    distsP1 = [int(each) for each in lines[1].removesuffix("\n").split()[1:]]
    times: int = ""
    dists: int = ""
    for each in timesP1:
        times += str(each)
    for each in distsP1:
        dists += str(each)
    times = int(times)
    dists = int(dists)
    possibles.append([])
    time, dist = times, dists
    for timeHeld in range(1, time):
        remTime = time - timeHeld
        distTraveled = remTime * timeHeld
        if distTraveled > int(dist):
            possibles[-1].append(timeHeld)
toPrint = 1
for each in possibles:
    toPrint *= len(each)
print(toPrint)
