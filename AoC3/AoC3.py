OFFSET = 141
# TODO
# TODO       PREVENT DOUBLE COUNT COUNT ERROR OF NUMBERS ( GL IG ) ALSO IF THATS TOO EASY THEN MAKE IT ACTUALLY WORK :D
c = None
g = 0
gearArchive = []
count = 0
gears = []
gearDone = []
mainGear = []

def numLoop(counta=None):
    if counta is None:
        counta = 0
    print(count)
    en = EngineNums
    n = [""]
    n[-1] = lines[idx]
    i = 1
    if idx + i < len(lines):
        while lines[idx + i] in "0123456789" and idx + i < len(lines):
            n[-1] += lines[idx + i]
            i += 1
    b = i
    i = 1
    if idx - i < len(lines) and idx - i > 0:
        while lines[idx - i] in "0123456789" and idx - i < len(lines):
            n[-1] = lines[idx - i] + n[-1]
            i += 1
    a = len(n[0]) - 1
    if count == 0 and counta == 0:
        EngineNums.append(n[0])
        EngineNums.append("")
        return b
    else:
        return n[0]


def gearLoop():
    print(count)
    en = EngineNums
    n = [""]
    n[-1] = lines[m]
    g = 1
    a = m
    gearDone.append(a)
    if a+g < len(lines):
        while lines[a+g] in "0123456789" and a+g < len(lines):
            n[-1] += lines[a+g]
            gearDone.append(a + g)
            g+=1

    b = a
    a = m
    g = 1
    if len(lines) > a-g > 0:
        while lines[a-g] in "0123456789" and a-g < len(lines):
            n[-1] = lines[a-g] + n[-1]
            gearDone.append(a - g)
            g+=1
    a = len(n[0]) - 1
    return n[0]


with open('AoC3.txt', 'r') as f:
    lines = f.readlines()
    nums = []
    symbols = {}
    EngineNums = []
    buf = ""
    possibles = []
    EngineNums = [""]
    for each in lines:
        each = each.removesuffix("\n")
        buf += each
    lines = buf
    print(lines)
    for idx, char in enumerate(lines):
        if count == 0:
            if char == "*" and lines[idx+11] == "9":
                g += 1
                if g == 2:
                    print("HMMMM")

                print("hmm")
            if char in "1234567890n" and idx not in [int(each) for each in gearArchive]:
                m = OFFSET + idx  # Next Line

                if 0 < m < len(lines) - 1:
                    if lines[m] is not None and lines[m] != "." and lines[m] not in "0123456789":
                        nums.append(int(char))
                        i = 1
                        c = numLoop()
                m = idx - OFFSET  # Line above

                if 0 < m < len(lines) - 1:
                    if lines[m] is not None and lines[m] != "." and lines[m] not in "0123456789":
                        nums.append(int(char))

                        c = numLoop()
                m = idx + 1  # Next

                if 0 < m < len(lines) - 1:
                    if lines[m] is not None and lines[m] != "." and lines[m] not in "0123456789":
                        nums.append(int(char))
                        c = numLoop()
                m = idx - 1  # Previous

                if 0 < m < len(lines) - 1:
                    if lines[m] is not None and lines[m] != "." and lines[m] not in "0123456789":
                        nums.append(int(char))

                        c = numLoop()
                m = idx + OFFSET + 1  # Next line + diagonal next

                if 0 < m < len(lines) - 1:
                    if lines[m] is not None and lines[m] != "." and lines[m] not in "0123456789":
                        nums.append(int(char))

                        c = numLoop()
                m = idx + OFFSET - 1  # Next lines + diagonal prev

                if 0 < m < len(lines) - 1:
                    if lines[m] is not None and lines[m] != "." and lines[m] not in "0123456789":
                        nums.append(int(char))

                        c = numLoop()
                m = idx - OFFSET + 1  # Previous lines and diagonal next

                if 0 < m < len(lines) - 1:
                    if lines[m] is not None and lines[m] != "." and lines[m] not in "0123456789":
                        nums.append(int(char))

                        c = numLoop()
                m = idx - OFFSET - 1

                if 0 < m < len(lines) - 1:  # Previous lines + diagonal prev
                    if lines[m] is not None and lines[m] != "." and lines[m] not in "0123456789":
                        nums.append(int(char))

                        c = numLoop()
                if c is not None:
                    count = c - 1
                    c = None
            elif char in "*":
                m = OFFSET + idx  # Next Line

                if 0 < m < len(lines) - 1 and m not in gearDone:
                    if lines[m] is not None:
                        if lines[m] != "." and lines[m] in "0123456789":
                            i = 1
                            gears.append(gearLoop())
                m = idx - OFFSET  # Line above

                if 0 < m < len(lines) - 1 and m not in gearDone:
                    if lines[m] is not None and lines[m] != "." and lines[m] in "0123456789":
#                        nums.append(int(char))

                        gears.append(gearLoop())
                m = idx + 1  # Next

                if 0 < m < len(lines) - 1 and m not in gearDone:
                    if lines[m] is not None and lines[m] != "." and lines[m] in "0123456789":
                        gears.append(gearLoop())
                m = idx - 1  # Previous

                if 0 < m < len(lines) - 1 and m not in gearDone:
                    if lines[m] is not None and lines[m] != "." and lines[m] in "0123456789":
                        gears.append(gearLoop())
                m = idx + OFFSET + 1  # Next line + diagonal next

                if 0 < m < len(lines) - 1 and m not in gearDone:
                    if lines[m] is not None and lines[m] != "." and lines[m] in "0123456789":
                        gears.append(gearLoop())
                m = idx + OFFSET - 1  # Next lines + diagonal prev

                if 0 < m < len(lines) - 1 and m not in gearDone:
                    if lines[m] is not None and lines[m] != "." and lines[m] in "0123456789":
                        gears.append(gearLoop())
                m = idx - OFFSET + 1  # Previous lines and diagonal next

                if 0 < m < len(lines) - 1 and m not in gearDone:
                    if lines[m] is not None and lines[m] != "." and lines[m] in "0123456789":
                        gears.append(gearLoop())
                m = idx - OFFSET - 1

                if 0 < m < len(lines) - 1 and m not in gearDone:  # Previous lines + diagonal prev
                    if lines[m] is not None and lines[m] != "." and lines[m] in "0123456789":
                        gears.append(gearLoop())
                if len(gears) == 2:
                    hmm = 1
                    while gears[0] in EngineNums and hmm < 2:
                        EngineNums.remove(str(gears[0]))
                        hmm+=1
                    hmm = 1
                    while gears[-1] in EngineNums and hmm < 2:
                        EngineNums.remove(str(gears[-1]))
                        hmm+=1
                    mainGear.append(int(gears[0]) * int(gears[1]))
                    for every in gearDone:
                        gearArchive.append(str(every))
                    gears = []
                    gearDone = []
                else:
                    gears = []
                    gearDone =  []
        else:
            count -= 1
    toSum = [int(each) for each in EngineNums if each != ""]
    print(mainGear)
    print(sum(mainGear))
