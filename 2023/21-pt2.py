import datetime
filePath = "D:/repos\Testbed\AdventOfCode/2023/21-input.txt"

# Get input from file
lines = []
with open(filePath, "r") as f:
    lines = f.readlines()

lines = [x.strip('\n') for x in lines]

# Sample input
# lines = '''...........
# .....###.#.
# .###.##..#.
# ..#.#...#..
# ....#.#....
# .##..S####.
# .##..#...#.
# .......##..
# .##.#.####.
# .##..##.##.
# ...........'''.split('\n')

def WriteOut(lines, plots):
    with open("./21-output.txt", "w") as f:
        for i, line in enumerate(lines):
            newLine = ""
            for j, char in enumerate(line):
                if (i,j) in plots:
                    newLine += "O"
                else:
                    newLine += char
            f.write(newLine + "\n")

startingSpot = [(i, line.index("S")) for i, line in enumerate(lines) if "S" in line][0]

queue = [startingSpot]
steps = 65

for i in range(steps):
    newQueue = []
    while len(queue) > 0:
        currentItem = queue.pop(0)
        # Above
        if currentItem[0] != 0 and lines[currentItem[0]-1][currentItem[1]] != "#" and (currentItem[0]-1,currentItem[1]) not in newQueue:
            newQueue.append((currentItem[0]-1,currentItem[1]))
        # Below
        if currentItem[0] != len(lines)-1 and lines[currentItem[0]+1][currentItem[1]] != "#" and (currentItem[0]+1,currentItem[1]) not in newQueue:
            newQueue.append((currentItem[0]+1,currentItem[1]))
        # Left
        if currentItem[1] != 0 and lines[currentItem[0]][currentItem[1]-1] != "#" and (currentItem[0],currentItem[1]-1) not in newQueue:
            newQueue.append((currentItem[0],currentItem[1]-1))
        # Right
        if currentItem[1] != len(lines[0])-1 and lines[currentItem[0]][currentItem[1]+1] != "#" and (currentItem[0],currentItem[1]+1) not in newQueue:
            newQueue.append((currentItem[0],currentItem[1]+1))
    queue = newQueue

WriteOut(lines, queue)
print(f"Possible steps: {len(queue)}")

inputSize = 26501365
mapWidth = mapHeight = 131
finalWidth = finalHeight = inputSize*2 + 1
area = finalHeight*finalWidth/2

# inputSize = 26501365
# Width = inputsize*2 + 1
# Widht = 53002731
# 404601 maps wide

# - for each line, calculate how many maps it covers and have a formula for how many O's it'll be (alternating, so odd number will be x, and even number will be y)
# - I think each one will be either whole, or a trianglular portion of each map for the edges (imagine one edge flows down into another)