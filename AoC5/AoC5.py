seeds = [[]]
#TODO       CHECK IF VALUE IN RANGE, AND IF SO, THEN DO SOME MAP RANGE SHENANIGINS :DD
toSoil = []
seedToSoil = []
soilTofert = []
fertToWater = []
waterToLight = []
lightToTemp = []
tempToHumid = []
humidToLocat = []
extract = ""
locats = []
def extractRange(start1, start2, end):
    return [range(int(start1), int(start1)+int(end)), range(int(start2), int(start2)+int(end))]

def mapValuesWithRange(startRanges, endRanges, toConvert):
    for idx, startRange in enumerate(startRanges):
        if toConvert in startRange:
            return endRanges[idx][startRange.index(toConvert)]
    else:
        return toConvert

with open('AoC5.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        line = line.removesuffix("\n")
        if extract == "":
            if line.startswith("seeds:"):
                n1 = 0
                for idx, seed in enumerate(line[6:].strip().split()):
                    if idx % 2 == 0:
                        n1 = int(seed)
                    else:
                        seeds[0].append(range(int(seed), n1))
                toConv = seeds[0]
            elif line.startswith("seed-to-soil"):
                extract = "seed-to-soil"
        elif extract == "seed-to-soil":
            if line[0]:
                if line[0].isdigit():
                    toSoil.append(extractRange(line.split()[0] , line.split()[1], line.split()[2]))
                else:
                    extract = "soil-to-fert"
        elif extract == "soil-to-fert":
            if line[0]:
                if line[0].isdigit():
                    soilTofert.append(extractRange(line.split()[0], line.split()[1], line.split()[2]))
                else:
                    extract = "fert-to-water"
        elif extract == "fert-to-water":
            if line[0]:
                if line[0].isdigit():
                    fertToWater.append(extractRange(line.split()[0], line.split()[1], line.split()[2]))
                else:
                    extract = "water-to-light"
        elif extract == "water-to-light":
            if line[0]:
                if line[0].isdigit():
                    waterToLight.append(extractRange(line.split()[0], line.split()[1], line.split()[2]))
                else:
                    extract = "light-to-temp"
        elif extract == "light-to-temp":
            if line[0]:
                if line[0].isdigit():
                    lightToTemp.append(extractRange(line.split()[0], line.split()[1], line.split()[2]))
                else:
                    extract = "temp-to-humid"
        elif extract == "temp-to-humid":
            if line[0]:
                if line[0].isdigit():
                    tempToHumid.append(extractRange(line.split()[0], line.split()[1], line.split()[2]))
                else:
                    extract = "humid-to-locat"
        elif extract == "humid-to-locat":
            humidToLocat.append(extractRange(line.split()[0], line.split()[1], line.split()[2]))

            print(seeds, toSoil, soilTofert, fertToWater, waterToLight, lightToTemp, tempToHumid, humidToLocat)

for seed in seeds[0]:
    toConv = int(seed)
    inp = []
    end = []
    for idx, each in enumerate(toSoil):
        inp.append(each[1])
        end.append(each[0])

    toConv = mapValuesWithRange(inp, end, toConv)
    inp = []
    end = []
    for idx, each in enumerate(soilTofert):
        inp.append(each[1])
        end.append(each[0])

    toConv = mapValuesWithRange(inp, end, toConv)
    inp = []
    end = []
    for idx, each in enumerate(fertToWater):
        inp.append(each[1])
        end.append(each[0])

    toConv = mapValuesWithRange(inp, end, toConv)
    inp = []
    end = []
    for idx, each in enumerate(waterToLight):
        inp.append(each[1])
        end.append(each[0])

    toConv = mapValuesWithRange(inp, end, toConv)
    inp = []
    end = []
    for idx, each in enumerate(lightToTemp):
        inp.append(each[1])
        end.append(each[0])

    toConv = mapValuesWithRange(inp, end, toConv)
    inp = []
    end = []
    for idx, each in enumerate(tempToHumid):
        inp.append(each[1])
        end.append(each[0])

    toConv = mapValuesWithRange(inp, end, toConv)
    inp = []
    end = []
    for idx, each in enumerate(humidToLocat):
        inp.append(each[1])
        end.append(each[0])

    toConv = mapValuesWithRange(inp, end, toConv)


    locats.append(toConv)

locats.sort()
print(locats[0])