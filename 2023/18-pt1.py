import re
filePath = "D:/repos\Testbed\AdventOfCode/2023/18-input.txt"

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

firstLineIndex = None
for i,line in enumerate(grid):
    if "#" in line:
        firstLineIndex = i
        break

lastLineIndex = None
for i in range(len(grid)-1,0,-1):
    if "#" in grid[i]:
        lastLineIndex = i



# Flood fill starting diagonally under the start node
startSpot = (900,900)
queue = [startSpot]
count = 0
while len(queue) > 0:
    count += 1
    location = queue.pop()
    grid[location[0]][location[1]] = "I"
    # Down
    if grid[location[0]+1][location[1]] not in ["#","I"] and (location[0]+1,location[1]) not in queue:
        queue.insert(0, (location[0]+1,location[1]))
    # Up
    if grid[location[0]-1][location[1]] not in ["#","I"] and (location[0]-1,location[1]) not in queue:
        queue.insert(0, (location[0]-1,location[1]))
    # Left
    if grid[location[0]][location[1]-1] not in ["#","I"] and (location[0],location[1]-1) not in queue:
        queue.insert(0, (location[0],location[1]-1))
    # Right
    if grid[location[0]][location[1]+1] not in ["#","I"] and (location[0],location[1]+1) not in queue:
        queue.insert(0, (location[0],location[1]+1))
    queue = list(set(queue))

    if (count%25000 == 0):
        WriteOut(grid)
        print(f"Printing at count = {count}")
                
WriteOut(grid)
counts = sum([line.count("I") + line.count("#") for line in grid])
print(f"Total count: {counts}")


# TODO: Look into shoe string formula

