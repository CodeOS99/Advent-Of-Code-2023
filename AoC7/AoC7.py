from collections import Counter


def custom_card_sort(hand):
    """
    Sort the cards in the hand based on their value.
    """
    values_order = {'2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, '9': 7, 'T': 8, 'J': 9, 'Q': 10, 'K': 11,
                    'A': 12}
    return [values_order[card] for card in hand]


hands = []
bids = {}
fiveOfAKind = []
fourOfAKind = []
fullHouse = []
threeOfAKind = []
twoPair = []
onePair = []
highCard = []
vals = "23456789TJQKA"
with open('AoC7.txt', 'r') as f:
    """
    Read the input file and store the hands and bids in lists.
    """
    lines = [each.replace("\n", "") for each in f.readlines()]
    for each in lines:
        each = each.split()
        hands.append(each[0])
        bids[each[0]] = each[1]
countToNotUse = []
for each in hands:
    """
    Create a list of Counter objects for each hand.
    """
    countToNotUse.append(Counter(each))
counts = []
for counter in countToNotUse:
    """
    Create a list of lists of dictionaries of counts for each hand.
    """
    counts.append([])
    for val in counter:
        counts[-1].append({val: counter[val]})

for indx, hand in enumerate(counts):
    """
    For each hand, find the frequencies and store them in a list.
    """
    currents = []
    for val in hand:
        if list(val.values())[0] == 5:
            currents.append("five")
        elif list(val.values())[0] == 4:
            currents.append("four")
        elif list(val.values())[0] == 3:
            currents.append("three")
        elif list(val.values())[0] == 2:
            currents.append("two")
        elif list(val.values())[0] == 1:
            currents.append("one")
    flagForOne = 0
    for idx, each in enumerate(currents):
        """
        Iterate over the frequencies and determine the type of hand accordingly.
        """
        if each == "five":
            fiveOfAKind.append(hands[indx])
            print(f"{hands[indx]} is a five of a kind")
            break
        elif each == "four":
            fourOfAKind.append(hands[indx])
            print(f"{hands[indx]} is a four of a kind")
            break
        elif each == "three":
            if idx + 1 < len(currents):
                if currents[idx + 1] == "two" or (currents[idx - 1] == "two" and idx - 1 > 0):
                    fullHouse.append(hands[indx])
                    print(f"{hands[indx]} is a full house")
                    break
                else:
                    threeOfAKind.append(hands[indx])
                    print(f"{hands[indx]} is a three of a kind")
                    break
            else:
                if currents[idx - 1] == "two" and idx - 1 > 0:
                    fullHouse.append(hands[indx])
                    print(f"{hands[indx]} is a full house")
                    break
                else:
                    threeOfAKind.append(hands[indx])
                    print(f"{hands[indx]} is a three of a kind")
                    break
        elif each == "two":
            if idx + 1 < len(currents):
                if idx + 2 < len(currents):
                    if (currents[idx + 1] == "two" and idx + 1 < len(currents)) or (
                            currents[idx + 2] == "two" and idx + 2 < len(currents)) or (
                            currents[idx - 1] == "two" and idx - 1 > 0) or (currents[idx - 2] == "two" and idx - 2 > 0):
                        twoPair.append(hands[indx])
                        print(f"{hands[indx]} is a two pair")
                        break
                    elif (currents[idx + 1] == "three" and idx + 1 < len(currents)) or (
                            currents[idx + 2] == "three" and idx + 2 < len(currents)) or (
                            currents[idx - 1] == "three" and idx - 1 > 0) or (currents[idx - 2] == "three" and idx - 2 > 0):
                        fullHouse.append(hands[indx])
                        print(f"{hands[indx]} is a full house")
                        break
                    else:
                        onePair.append(hands[indx])
                        print(f"{hands[indx]} is a one pair")
                        break
                else:
                    if (currents[idx + 1] == "two" and idx + 1 < len(currents)) or (
                            currents[idx - 1] == "two" and idx - 1 > 0) or (currents[idx - 2] == "two" and idx - 2 > 0):
                        twoPair.append(hands[indx])
                        print(f"{hands[indx]} is a two pair")
                        break
                    elif (currents[idx + 1] == "three" and idx + 1 < len(currents)) or (
                            currents[idx - 1] == "three" and idx - 1 > 0) or (currents[idx - 2] == "three" and idx - 2 > 0):
                        fullHouse.append(hands[indx])
                        print(f"{hands[indx]} is a full house")
                        break
                    else:
                        onePair.append(hands[indx])
                        print(f"{hands[indx]} is a one pair")
                        break
            else:
                if (currents[idx - 1] == "two" and idx - 1 > 0) or (currents[idx - 2] == "two" and idx - 2 > 0):
                    twoPair.append(hands[indx])
                    print(f"{hands[indx]} is a two pair")
                    break
                elif (currents[idx - 1] == "three" and idx - 1 > 0) or (currents[idx - 2] == "three" and idx - 2 > 0):
                    fullHouse.append(hands[indx])
                    print(f"{hands[indx]} is a full house")
                    break
                else:
                    onePair.append(hands[indx])
                    print(f"{hands[indx]} is a one pair")
                    break
        else:
            flagForOne += 1

    if flagForOne == 5:
        print(f"{hands[indx]} is a high card")
        highCard.append(hands[indx])

# Sort the hands in descending order based on their rank.
highCard.sort(key=custom_card_sort)
onePair.sort(key=custom_card_sort)
twoPair.sort(key=custom_card_sort)
threeOfAKind.sort(key=custom_card_sort)
fourOfAKind.sort(key=custom_card_sort)
fullHouse.sort(key=custom_card_sort)
fiveOfAKind.sort(key=custom_card_sort)

# Create a list of all the sorted hands.
allSorted = []
for each in highCard:
    allSorted.append(each)
for each in onePair:
    allSorted.append(each)
for each in twoPair:
    allSorted.append(each)
for each in threeOfAKind:
    allSorted.append(each)
for each in fullHouse:
    allSorted.append(each)
for each in fourOfAKind:
    allSorted.append(each)
for each in fiveOfAKind:
    allSorted.append(each)

# Calculate the total amount of money that each player has won or lost.
toPrint = 0
for each in allSorted:
    toPrint += (int(bids.get(each)) * (allSorted.index(each) + 1))
print(toPrint)
