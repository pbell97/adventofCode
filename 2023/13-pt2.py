import itertools
filePath = "/Users/patrickbell/Documents/repos/adventofCode/2023/13-input.txt"

# Get input from file
lines = []
with open(filePath, "r") as f:
    lines = f.readlines()

lines = [x.strip('\n') for x in lines]

# Sample input
# lines = '''#.##..##.
# ..#.##.#.
# ##......#
# ##......#
# ..#.##.#.
# ..##..##.
# #.#.##.#.

# #...##..#
# #....#..#
# ..##..###
# #####.##.
# #####.##.
# ..##..###
# #....#..#'''.split('\n')

# Assemble puzzles
puzzles = []
currentPuzzle = []
for i,line in enumerate(lines):
    if len(line) == 0:
        puzzles.append(currentPuzzle)
        currentPuzzle = []
    else:
        currentPuzzle.append(line)
    if i == len(lines)-1:
        puzzles.append(currentPuzzle)

# Returns number of columns to the left of the vertical mirror, or -1 if not there
def GetVerticalMirrorColumns(puzzle):
    checks = []
    for lineIndex,line in enumerate(puzzle):
        checks.append([])
        # Note: Dividing line is to the right of the indexed character
        for dividingLineIndex in range(len(line)):
            result = False
            first = line[0:dividingLineIndex+1]
            second = line[dividingLineIndex+1:]
            first = first[::-1]
            if len(first) == 0 or len(second) == 0:
                result = False
            elif len(first) < len(second):
                result = second.startswith(first)
            else:
                result = first.startswith(second)
            checks[lineIndex].append(result)

    # Finds where only one in each column didn't have a match and assumes that is the one
    for columnIndex in range(len(checks[0])):
        falses = []
        trues = []
        for rowIndex, row in enumerate(checks):
            if checks[rowIndex][columnIndex]:
                trues.append((rowIndex, columnIndex))
            else:
                falses.append((rowIndex, columnIndex))

        if len(falses) == 1:
            return columnIndex + 1
        
    return 0

count = 0
for i,puzzle in enumerate(puzzles):
    verticalCount = GetVerticalMirrorColumns(puzzle)
    flippedPuzzle = ["".join(x) for x in zip(*puzzle)]
    horizontalCount = GetVerticalMirrorColumns(flippedPuzzle)
    if verticalCount == 0 and horizontalCount == 0:
        print(f"Can't find a mirror for index {i}")
    elif  verticalCount > 0 and horizontalCount > 0:
        print(f"Found multiple mirrors for puzzle index {i} - Vertical: {verticalCount}, Horizontal: {horizontalCount}")
    elif verticalCount != 0:
        count += verticalCount
    else:
        count += 100*horizontalCount

print(f"Final count: {count}")
