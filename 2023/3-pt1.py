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

partNumbers = []


def checkForSymbol(lineIndex, characterIndex):
    symbols = ['!', '@', '#', '$', '%', '^',
               '&', '*', '(', ')', '-', '+', '_', '=', '/']

    # Above
    if lineIndex != 0 and lines[lineIndex-1][characterIndex] in symbols:
        return True
    # Below
    if lineIndex != linesCount-1 and lines[lineIndex+1][characterIndex] in symbols:
        return True
    # Left
    if characterIndex != 0 and lines[lineIndex][characterIndex-1] in symbols:
        return True
    # Right
    if characterIndex != lineLength-1 and lines[lineIndex][characterIndex+1] in symbols:
        return True
    # Above Right
    if lineIndex != 0 and characterIndex != lineLength-1 and lines[lineIndex-1][characterIndex+1] in symbols:
        return True
    # Above Left
    if lineIndex != 0 and characterIndex != 0 and lines[lineIndex-1][characterIndex-1] in symbols:
        return True
    # Below Right
    if lineIndex != linesCount-1 and characterIndex != lineLength-1 and lines[lineIndex+1][characterIndex+1] in symbols:
        return True
    # Below Left
    if lineIndex != linesCount-1 and characterIndex != 0 and lines[lineIndex+1][characterIndex-1] in symbols:
        return True


for lineIndex in range(len(lines)):
    line = lines[lineIndex]
    currentNumber = ""
    isPartNumber = False
    for characterIndex in range(len(line)):
        character = line[characterIndex]
        if character.isnumeric():  # What if end of line?
            currentNumber += character
            isPartNumber = isPartNumber or checkForSymbol(
                lineIndex, characterIndex)
        if (not character.isnumeric() and currentNumber != "" and currentNumber != "") or (characterIndex == len(line)-1 and character.isnumeric()):
            number = int(currentNumber)
            if isPartNumber:
                partNumbers.append(number)
            currentNumber = ""
            isPartNumber = False

print(f"Sum of part numbers: {sum(partNumbers)}")
