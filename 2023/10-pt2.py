import math
filePath = "./10-input.txt"

# Get input from file
lines = []
with open(filePath, "r") as f:
    lines = f.readlines()

lines = [x.strip('\n') for x in lines]

# Sample input
lines = '''.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...'''.split('\n')


# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.



# Returns (newPipeRow, new PipeColumn)
def GetNextPipe(pipeRow, pipeColumn, previousPipeRow, previousPipeColumn):
    pipeType = lines[pipeRow][pipeColumn]
    previousDirection = "Left" if pipeColumn > previousPipeColumn else "Right" if pipeColumn < previousPipeColumn else "Up" if previousPipeRow < pipeRow else "Down"
    if pipeType == "|":
        return (pipeRow+1, pipeColumn) if previousDirection == "Up" else (pipeRow-1, pipeColumn)
    elif pipeType == "-":
        return (pipeRow, pipeColumn+1) if previousDirection == "Left" else (pipeRow, pipeColumn-1)
    elif pipeType == "L":
        return (pipeRow, pipeColumn+1) if previousDirection == "Up" else (pipeRow-1, pipeColumn)
    elif pipeType == "J":
        return (pipeRow, pipeColumn-1) if previousDirection == "Up" else (pipeRow-1, pipeColumn)
    elif pipeType == "7":
        return (pipeRow+1, pipeColumn) if previousDirection == "Left" else (pipeRow, pipeColumn-1)
    elif pipeType == "F":
        return (pipeRow+1, pipeColumn) if previousDirection == "Right" else (pipeRow, pipeColumn+1)


# Find S
sCoords = ()
for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char == "S":
            sCoords =  (i,j)
            break
    if sCoords != ():
        break


# Get first pipe from Start
pipes = []
# Above
if sCoords[0] != 0 and lines[sCoords[0]-1][sCoords[1]] in ["F", "7", "|"]:
    pipes.append((sCoords[0]-1,sCoords[1]))
# Left
elif sCoords[1] != 0 and lines[sCoords[0]][sCoords[1]-1] in ["F", "L", "-"]:
    pipes.append((sCoords[0], sCoords[1]-1))
# Below
elif sCoords[0] != len(lines)-1 and lines[sCoords[0]+1][sCoords[1]] in ["J", "L", "|"]:
    pipes.append((sCoords[0]+1, sCoords[1]))
# Right
elif sCoords[0] != len(lines)-1 and lines[sCoords[0]][sCoords[1]+1] in ["J", "7", "-"]:
    pipes.append((sCoords[0], sCoords[1]+1))
else:
    print("Can't find the start to the pipe loop")
    exit()


# If almost works, edit the S to be whatever it should be


# Get all pipes
foundS = False
while not foundS:
    currentPipeCoords = pipes[-1]
    previousPipeCoords = pipes[-2] if (len(pipes) > 1) else sCoords
    nextPipeCoords = GetNextPipe(currentPipeCoords[0], currentPipeCoords[1], previousPipeCoords[0], previousPipeCoords[1])
    if nextPipeCoords != sCoords:
        pipes.append(nextPipeCoords)
    else:
        foundS = True


# Only care about if pipe is facing north
validPipes = ['|', 'J', 'L']    # NOTE: May need to include 'S' if your S is pretending to be one of these

pipes.insert(0, sCoords)
# Ray casting algorithm
innerTiles = []
for i in range(len(lines)):
    shouldCount = False
    for j in range(len(lines[0])):
        if (i,j) in pipes and lines[i][j] in validPipes:
            shouldCount = not shouldCount
        elif shouldCount and (i,j) not in pipes:
            innerTiles.append((i,j))

print(f"Inside tile counts: {len(set(innerTiles))}")

with open("10-testout.txt", 'w') as f:
    for i in range(len(lines)):
        row = []
        for j in range(len(lines[i])):
            if (i,j) in pipes:
                row.append(lines[i][j])
            elif (i,j) in innerTiles:
                row.append('I')
            else:
                row.append('.')
        row.append("\n")
        f.write("".join(row))