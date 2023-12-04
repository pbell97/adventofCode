filePath = "./3-input.txt"

# Get input from file
lines = []
with open(filePath, "r") as f:
    lines = f.readlines()

# Sample input
# lines = '''467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..'''.split('\n')

linesCount = len(lines)
lineLength = len(lines[0])

gearRatios = []


def getNumberAtLocation(lineIndex, characterIndex):
    number = lines[lineIndex][characterIndex]

    leftIndex = characterIndex - 1
    while leftIndex != -1 and lines[lineIndex][leftIndex].isnumeric():
        number = lines[lineIndex][leftIndex] + number
        leftIndex -= 1

    rightIndex = characterIndex + 1
    while rightIndex != lineLength and lines[lineIndex][rightIndex].isnumeric():
        number += lines[lineIndex][rightIndex]
        rightIndex += 1

    return int(number)


def getAdjacentNumbers(lineIndex, characterIndex):
    numbers = []
    # Above
    if lineIndex != 0 and lines[lineIndex-1][characterIndex].isnumeric():
        numbers.append(getNumberAtLocation(lineIndex-1, characterIndex))
    # Below
    if lineIndex != linesCount-1 and lines[lineIndex+1][characterIndex].isnumeric():
        numbers.append(getNumberAtLocation(lineIndex+1, characterIndex))
    # Left
    if characterIndex != 0 and lines[lineIndex][characterIndex-1].isnumeric():
        numbers.append(getNumberAtLocation(lineIndex, characterIndex-1))
    # Right
    if characterIndex != lineLength-1 and lines[lineIndex][characterIndex+1].isnumeric():
        numbers.append(getNumberAtLocation(lineIndex, characterIndex+1))
    # Above Right
    if lineIndex != 0 and characterIndex != lineLength-1 and lines[lineIndex-1][characterIndex+1].isnumeric():
        numbers.append(getNumberAtLocation(lineIndex-1, characterIndex+1))
    # Above Left
    if lineIndex != 0 and characterIndex != 0 and lines[lineIndex-1][characterIndex-1].isnumeric():
        numbers.append(getNumberAtLocation(lineIndex-1, characterIndex-1))
    # Below Right
    if lineIndex != linesCount-1 and characterIndex != lineLength-1 and lines[lineIndex+1][characterIndex+1].isnumeric():
        numbers.append(getNumberAtLocation(lineIndex+1, characterIndex+1))
    # Below Left
    if lineIndex != linesCount-1 and characterIndex != 0 and lines[lineIndex+1][characterIndex-1].isnumeric():
        numbers.append(getNumberAtLocation(lineIndex+1, characterIndex-1))

    return list(set(numbers))


for lineIndex in range(len(lines)):
    line = lines[lineIndex]
    currentNumber = ""
    isPartNumber = False
    for characterIndex in range(len(line)):
        character = line[characterIndex]

        if character == "*":
            possiblePartNumbers = getAdjacentNumbers(lineIndex, characterIndex)

            if len(possiblePartNumbers) == 2:
                gearRatios.append(
                    possiblePartNumbers[0]*possiblePartNumbers[1])

print(f"Sum of gear ratios: {sum(gearRatios)}")
