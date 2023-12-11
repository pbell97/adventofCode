import math
filePath = "./10-input.txt"

# Get input from file
lines = []
with open(filePath, "r") as f:
    lines = f.readlines()

lines = [x.strip('\n') for x in lines]

# Sample input
# lines = '''-L|F7
# 7S-7|
# L|7||
# -L-J|
# L|-JF'''.split('\n')


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


print(f"Len of loop: {len(pipes)}")
print(f"Furthest steps away {math.ceil(len(pipes)/2)}")