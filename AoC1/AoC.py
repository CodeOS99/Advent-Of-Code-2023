import re
digL = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
def extractDigs(l):
    if l in digL:
        return str(digL.index(l))
    elif l in "0123456789":
        return str(l)
total = 0
regEx =r"(?=(one|two|three|four|five|six|seven|eight|nine|zero|\d))"


with open('AoC1.txt', 'r') as f:
    lines = f.readlines()
    for each in lines:
        digs = re.findall(regEx, each)
        total+= int(extractDigs(digs[0]) + extractDigs(digs[-1]))
print(total)