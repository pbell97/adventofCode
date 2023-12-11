import itertools
filePath = "./11-input.txt"

# Get input from file
lines = []
with open(filePath, "r") as f:
    lines = f.readlines()

lines = [x.strip('\n') for x in lines]

# Sample input
# lines = '''...#......
# .......#..
# #.........
# ..........
# ......#...
# .#........
# .........#
# ..........
# .......#..
# #...#.....'''.split('\n')

# Expand the universe by row
numOfLines = len(lines)
emptyRowIndexes = [i for i, row in enumerate(lines) if all([x == "." for x in row])]
emptyColIndexes = [col for col in range(len(lines[0])) if all([lines[row][col] == "." for row in range(numOfLines)])]
emptyRowIndexes.reverse()
emptyColIndexes.reverse()

# Find all pairs and shortest distance between each
galexyLocations = []
for i, row in enumerate(lines):
    for j, col in enumerate(row):
        if col == "#":
            galexyLocations.append((i,j))

# Get all permutations/combinations
combinations = list(itertools.combinations(galexyLocations, 2))

# Get distances between each one
distances = []
expansionRate = 1000000-1
for pair in combinations:
    first = pair[0]
    second = pair[1]
    distance = abs(second[0] - first[0]) + abs(second[1] - first[1])
    
    xSorted = sorted([first[0], second[0]])
    ySorted = sorted([first[1], second[1]])
    addedXRows = sum([expansionRate for x in range(xSorted[0], xSorted[1]) if x in emptyRowIndexes])
    addedYRows = sum([expansionRate for x in range(ySorted[0], ySorted[1]) if x in emptyColIndexes])

    distances.append(distance + addedXRows + addedYRows)

print(f"Distances sum: {sum(distances)}")