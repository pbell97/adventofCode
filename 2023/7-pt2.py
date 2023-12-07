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

cardRanks = ["offset1", "offset2", "J", "2","3","4","5","6","7","8","9","T","Q","K","A"]

def GetCardOrderValue(originalCards):
    cards = list(originalCards)
    value = ""
    for card in cards:
        value += str(hex(cardRanks.index(card))).replace('0x','')
    return int(value, 16)

def GetHandTypeRank(originalCards):
    jokerCount = list(originalCards).count('J')
    originalCards = originalCards.replace('J','')
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
        if jokerCount == 1:
            value = 700
    # Full house
    elif 3 in counts and 2 in counts:
        value = 500
        # Won't have jokers in this scenario
    # Three of a kind
    elif 3 in counts:
        value = 400
        if jokerCount == 1:
            value = 600
        elif jokerCount == 2:
            value = 700
    # Two pair
    elif counts.count(2) == 2:
        value = 300
        if jokerCount == 1: # FullHouse
            value = 500
    # One pair
    elif counts.count(2) == 1:
        value = 200
        if jokerCount == 1: # Three of a kind
            value = 400
        elif jokerCount == 2: # Four of a kind
            value = 600
        elif jokerCount == 3: # Five of a kind
            value = 700
    else:
        value = 100
        if jokerCount == 1: # One pair
            value = 200
        elif jokerCount == 2: # Three of a kind
            value = 400
        elif jokerCount == 3: # Four of a kind
            value = 600
        elif jokerCount == 4 or jokerCount == 5: # Five of a kind
            value = 700

    return value


hands = [{"cards": line.split()[0], "bid": int(line.split()[1]), "handTypeValue": GetHandTypeRank(line.split()[0]), "cardOrderValue": GetCardOrderValue(line.split()[0])} for line in lines]

# Putting values in a tuple sorts them by each value then the next
hands.sort(key=lambda x: (x["handTypeValue"], x["cardOrderValue"]))

# Flipping so rank lines up with index (off by one)
finalValue = 0
for i in range(len(hands)):
    hands[i]["value"] = hands[i]["bid"] * (i+1)
    hands[i]["rank"] = i+1

for card in hands:
    print(card)

print(sum([x["value"] for x in hands]))

