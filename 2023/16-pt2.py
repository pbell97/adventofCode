filePath = "/Users/patrickbell/Documents/repos/adventofCode/2023/16-input.txt"

# Get input from file
lines = []
with open(filePath, "r") as f:
    lines = f.readlines()

lines = [x.strip('\n') for x in lines]

# Sample input
# lines = '''.|...\\....
# |.-.\\.....
# .....|-...
# ........|.
# ..........
# .........\\
# ..../.\\\\..
# .-.-/..|..
# .|....-|.\\
# ..//.|....'''.split('\n')

# Generate all start positions
startingLasers = []
width = len(lines[0])
height = len(lines)
for i in range(0,width):
    startingLasers.append({"location": (-1,i), "direction": "down"})
    startingLasers.append({"location": (height,i), "direction": "up"})
for i in range(0,height):
    startingLasers.append({"location": (i,-1), "direction": "right"})
    startingLasers.append({"location": (i,width), "direction": "left"})

# Keep track of best position so far
highestCount = 0
highestCountLaser = None


def WriteOut(lines, lasers, energizedPanels):
    with open("./16-output.txt", 'w') as f:
        laserLocations = [x["location"] for x in lasers]
        for i, line in enumerate(lines):
            assembledLine = ""
            for j, char in enumerate(line):
                if (i,j) in energizedPanels:
                    assembledLine += "#"
                else:
                    assembledLine += lines[i][j]
            f.write(assembledLine + "\n")

for i, startingLaser in enumerate(startingLasers):
    lasers = [startingLaser]
    energizedPanels = []
    lasersCache = [] # Stops lasers if that path has already been traveled

    while len(lasers) > 0:
        # input("") # Uncomment to visualize step by step
        # WriteOut(lines, lasers, energizedPanels)

        copyOfEnergizedPanels = energizedPanels.copy()
        newLasers = []
        for _laser in lasers:
            laser = _laser.copy()
            currentDirection = laser["direction"]
            yDelta = 1 if currentDirection == "right" else -1 if currentDirection == "left" else 0
            xDelta = 1 if currentDirection == "down" else -1 if currentDirection == "up" else 0
            nextLocation = (laser["location"][0] + xDelta, laser["location"][1] + yDelta)

            # Forget about laser if it has reached out of bounds
            if nextLocation[0] >= len(lines[0]) or nextLocation[1] >= len(lines) or nextLocation[0] < 0 or nextLocation[1] < 0:
                continue
            nextLocationChar = lines[nextLocation[0]][nextLocation[1]]

            # Count the panel as energized
            if (nextLocation not in energizedPanels):
                energizedPanels.append(nextLocation)


            if nextLocationChar == ".":
                laser["location"] = nextLocation
                if (laser not in lasersCache):
                    newLasers.append(laser) if laser not in newLasers else None
                    lasersCache.append(laser)
            elif nextLocationChar == "/":
                laser["location"] = nextLocation
                laser["direction"] = "right" if currentDirection == "up" else "down" if currentDirection == "left" else "up" if currentDirection == "right" else "left"
                if (laser not in lasersCache):
                    newLasers.append(laser) if laser not in newLasers else None
                    lasersCache.append(laser)
            elif nextLocationChar == "\\":
                laser["location"] = nextLocation
                laser["direction"] = "right" if currentDirection == "down" else "down" if currentDirection == "right" else "up" if currentDirection == "left" else "left"
                if (laser not in lasersCache):
                    newLasers.append(laser) if laser not in newLasers else None
                    lasersCache.append(laser)
            elif nextLocationChar == "|" and (currentDirection == "left" or currentDirection == "right"):
                laser["location"] = nextLocation
                laser["direction"] = "up"
                if (laser not in lasersCache):
                    newLasers.append(laser) if laser not in newLasers else None
                    lasersCache.append(laser)
                secondLaser = laser.copy()
                secondLaser["direction"] = "down"
                if (secondLaser not in lasersCache):
                    newLasers.append(secondLaser) if secondLaser not in newLasers else None
                    lasersCache.append(secondLaser)
            elif nextLocationChar == "-" and (currentDirection == "up" or currentDirection == "down"):
                laser["location"] = nextLocation
                laser["direction"] = "left"
                if (laser not in lasersCache):
                    newLasers.append(laser) if laser not in newLasers else None
                    lasersCache.append(laser)
                secondLaser = laser.copy()
                secondLaser["direction"] = "right"
                if (secondLaser not in lasersCache):
                    newLasers.append(secondLaser) if secondLaser not in newLasers else None
                    lasersCache.append(secondLaser)
            else:
                laser["location"] = nextLocation
                if (laser not in lasersCache):
                    newLasers.append(laser) if laser not in newLasers else None
                    lasersCache.append(laser)

        lasers = newLasers
        # print(len(energizedPanels), len(lasers), len(lasersCache))
            
    print(f"{i}/{len(startingLasers)} Total energized panels: {len(energizedPanels)}")

    if len(energizedPanels) > highestCount:
        highestCount = len(energizedPanels)
        highestCountLaser = startingLaser

print(f"Highest count: {highestCount} - {highestCountLaser}")
