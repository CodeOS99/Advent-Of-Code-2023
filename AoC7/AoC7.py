from collections import Counter
hands = []
bids =[]
with open('AoC7.txt', 'r') as f:
    lines = [each.replace("\n", "") for each in f.readlines()]
    for each in lines:
        each = each.split()
        hands.append(each[0])
        bids.append(each[1])
print(hands)
print(bids)
countToNotUse = []
for each in hands:
    countToNotUse.append(Counter(each))
counts = []
for each in countToNotUse:
    counts.append({})

