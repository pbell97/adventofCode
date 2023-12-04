filePath = "./4-input.txt"

# Get input from file
lines = []
with open(filePath, "r") as f:
    lines = f.readlines()

# Sample input
# lines = '''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'''.split('\n')

matchingNumbersForEachCard = {}
numberOfInstancesPerCard = {}
for i in range(len(lines)):
    matchingNumbersForEachCard[i] = 0
    numberOfInstancesPerCard[i] = 0


# Get number of matches for each card
for i in range(len(lines)):
    line = lines[i].split(': ')[1]
    winningNumbers = [int(x)
                      for x in line.split(' | ')[0].split(' ') if x != '']
    myNumbers = [int(x) for x in line.split(' | ')[1].split(' ') if x != '']
    matches = [x for x in myNumbers if x in winningNumbers]
    if len(matches) != 0:
        matchingNumbersForEachCard[i] = len(matches)

# Accumulate how many cards each is equal to, starting from the bottom going up
for cardIndex in range(len(lines)-1, -1, -1):
    totalCards = 1  # Give it one to count for itself
    # If it won any check how much each is worth
    if matchingNumbersForEachCard[cardIndex] != 0:
        numOfCards = matchingNumbersForEachCard[cardIndex]
        # Sum up how much each card below is worth that it received
        for i in range(1, numOfCards+1):
            totalCards += numberOfInstancesPerCard[cardIndex + i]
    numberOfInstancesPerCard[cardIndex] = totalCards

totalCount = sum([numberOfInstancesPerCard[key]
                  for key in numberOfInstancesPerCard.keys()])
print(f"Sum of all cards: {totalCount}")
