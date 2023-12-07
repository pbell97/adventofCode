filePath = "./7-input.txt"

# Get input from file
lines = []
with open(filePath, "r") as f:
    lines = f.readlines()

# Sample input
# lines = '''32T3K 765
# T55J5 684
# KK677 28
# KTJJT 220
# QQQJA 483'''.split('\n') 

cardRanks = ["offset1", "offset2", "2","3","4","5","6","7","8","9","T","J","Q","K","A"]

def GetCardOrderValue(originalCards):
    cards = list(originalCards)
    value = ""
    for card in cards:
        value += str(hex(cardRanks.index(card))).replace('0x','')
    return int(value, 16)

def GetHandTypeRank(originalCards):
    cards = list(originalCards)
    cards.sort()

    value = 0
    uniqueCards = list(set(cards))
    counts = [cards.count(x) for x in uniqueCards]

    # Five of a kind
    if 5 in counts:
        value = 700
    # Four of a kind
    elif 4 in counts:
        value = 600
    # Full house
    elif 3 in counts and 2 in counts:
        value = 500
    # Three of a kind
    elif 3 in counts:
        value = 400
    # 2 pair
    elif counts.count(2) == 2:
        value = 300
    # One pair
    elif counts.count(2) == 1:
        value = 200
    else:
        value = 100

    return value


hands = [{"cards": line.split()[0], "bid": int(line.split()[1]), "handTypeValue": GetHandTypeRank(line.split()[0]), "cardOrderValue": GetCardOrderValue(line.split()[0])} for line in lines]

# Sort by hand value (Might not be needed?)
hands.sort(reverse=True, key=lambda x : x["handTypeValue"])


# Sort into groups based on hands
groups = {}
groupOrder = []
for hand in hands:
    if hand["handTypeValue"] in groups.keys():
        groups[hand["handTypeValue"]].append(hand)
    else:
        groups[hand["handTypeValue"]] = [hand]
        groupOrder.append(hand["handTypeValue"])

# Sort within each group based on card values and recombine
finalOrder = []
for groupName in groupOrder:
    group = groups[groupName]
    group.sort(reverse=True, key=lambda x : x["cardOrderValue"])
    finalOrder += group


# Flipping so rank lines up with index (off by one)
finalOrder.reverse()
finalValue = 0
for i in range(len(finalOrder)):
    finalOrder[i]["value"] = finalOrder[i]["bid"] * (i+1)
    finalOrder[i]["rank"] = i+1

for card in finalOrder:
    print(card)

print(sum([x["value"] for x in finalOrder]))

