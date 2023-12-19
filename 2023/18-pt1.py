import re
filePath = "/Users/patrickbell/Documents/repos/adventofCode/2023/18-input.txt"

# Get input from file
lines = []
with open(filePath, "r") as f:
    lines = f.readlines()

lines = [x.strip('\n') for x in lines]

# Sample input
# lines = '''R 6 (#70c710)
# D 5 (#0dc571)
# L 2 (#5713f0)
# D 2 (#d2c081)
# R 2 (#59c680)
# D 2 (#411b91)
# L 5 (#8ceee2)
# U 2 (#caa173)
# L 1 (#1b58a2)
# U 2 (#caa171)
# R 2 (#7807d2)
# U 3 (#a77fa3)
# L 2 (#015232)
# U 2 (#7a21e3)'''.split('\n')

# Make a 2000 by 2000 grid
gridWidth = 2000
grid = [["."]*gridWidth for i in range(gridWidth)]
currentSpot = (int(gridWidth/2),int(gridWidth/2))
grid[currentSpot[0]][currentSpot[1]] = "#"

instructions = [{"direction": x.split()[0], "moves": int(x.split()[1]), "color": x.split()[2].strip("(").strip(")")} for x in lines]

def WriteOut(grid):
    with open("./18-output.txt", "w") as f:
        for line in grid:
            f.write("".join(line) + "\n")

# Draw trench
for instruction in instructions:
    for i in range(instruction["moves"]):
        if instruction["direction"] == "U":
            currentSpot = (currentSpot[0] - 1, currentSpot[1])
        elif instruction["direction"] == "D":
            currentSpot = (currentSpot[0] + 1, currentSpot[1])
        if instruction["direction"] == "L":
            currentSpot = (currentSpot[0], currentSpot[1]-1)
        if instruction["direction"] == "R":
            currentSpot = (currentSpot[0], currentSpot[1]+1)
        grid[currentSpot[0]][currentSpot[1]] = "#"


WriteOut(grid)
input("")

firstLineIndex = None
for i,line in enumerate(grid):
    if "#" in line:
        firstLineIndex = i
        break

lastLineIndex = None
for i in range(len(grid)-1,0,-1):
    if "#" in grid[i]:
        lastLineIndex = i




for lineIndex, line in enumerate(grid):
    if lineIndex == firstLineIndex or lineIndex == lastLineIndex:
        continue
    if "#" not in line:
        continue

    lineString = "".join(line)
    groups = re.split(r'(\#)',lineString)
    newGroups = []
    for group in groups:
        if '.' in group:
            newGroups.append(group)
        elif group == "#" and len(newGroups) > 0 and "#" in newGroups[-1]:
            newGroups[-1] += group
        elif group == "":
            continue
        else:
            newGroups += group
    groups = newGroups

    inShape = "#" in groups[0]
    newLine = ""

    if not inShape:
        newLine += groups[0]
        groups = groups[1:]


    # TODO: Just look up flood fill...
        # Get input location, change to I, then add all neighbors to a queue if they aren't already in the queue and aren't a '#'
        # Start node can be diagonally under the actual start position...

    for group in groups:
        if "#" in group:
            inShape = not inShape

        if inShape:
            newLine += "I"*len(group)
        else:
            newLine += group
    grid[lineIndex] = newLine

    # if lineIndex == firstLineIndex or lineIndex == lastLineIndex:
    #     continue
    # previousChar = ""
    # isOnLine = False
    # isInShape = False
    # for charIndex, char in enumerate(line):
    #     if char == "#" and grid[lineIndex][charIndex+1] != "#":
    #         isInShape = not isInShape
    #     elif isInShape:
    #         grid[lineIndex][charIndex] = "I"

    if (lineIndex > 850):
        WriteOut(grid)
        input("")
                
counts = sum([line.count("I") + line.count("#") for line in grid])
print(f"Total cound: {counts}")


    

