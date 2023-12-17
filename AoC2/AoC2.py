def isPossible(case):
    red = []
    green = []
    blue = []
    case = case.strip()
    separated = case.split(",")
    for cube in separated:
        color = cube.split()[1]
        match color:
            case "red":
                red.append(cube.split()[0])
            case "green":
                    green.append(cube.split()[0])
            case "blue":
                blue.append(cube.split()[0])
    return (red, green, blue)


with open('AoC2.txt', 'r') as f:
    correct = []
    maxR = 12
    maxG = 13
    maxB = 14
    lines = f.readlines()
    red = []
    green = []
    blue = []
    for each in lines:
        red.append(0)
        green.append(0)
        blue.append(0)
        name = each.split(":")[0][5:]
        cases = each.split(":")[1].split(";")
        for case in cases:
            redG, greenG, blueG = isPossible(case)
            if redG != []:
                returned = int(redG[0])
                if returned > red[-1]:
                    red[-1] = returned
            if greenG != []:
                returned = int(greenG[0])
                if returned > green[-1]:
                    green[-1] = returned
            if blueG != []:
                returned = int(blueG[0])
                if returned > blue[-1]:
                    blue[-1] = returned
    print(red)
    print(green)
    print(blue)
    for idx, n in enumerate(list(zip(red, green, blue))):
        r, g, b = n
        correct.append(r*g*b)
    print(sum(correct))