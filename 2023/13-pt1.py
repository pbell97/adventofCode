import itertools
filePath = "./13-input.txt"

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

    for columnIndex in range(len(checks[0])):
        isMirror = True
        for row in checks:
            isMirror = checks[checks.index(row)][columnIndex] and isMirror
        if isMirror:
            return columnIndex + 1
    return 0

count = 0
for i,puzzle in enumerate(puzzles):
    print(f"Checking {i}")
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
