possibles = []
with open('AoC6.txt', 'r') as f:
    lines = f.readlines()
    times = [int(each) for each in lines[0].removesuffix("\n").split()[1:]]
    dists = [int(each) for each in lines[1].removesuffix("\n").split()[1:]]

    for race in zip(times, dists):
        possibles.append([])
        time, dist = race
        for timeHeld in range(1, time):
            remTime = time-timeHeld
            distTraveled = remTime * timeHeld
            if distTraveled > int(dist):
                possibles[-1].append(timeHeld)
toPrint = 1
for each in possibles:
    toPrint *= len(each)
print(toPrint)