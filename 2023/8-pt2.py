filePath = "./8-input.txt"

# Get input from file
lines = []
with open(filePath, "r") as f:
    lines = f.readlines()

# Sample input
# lines = '''LR

# 11A = (11B, XXX)
# 11B = (XXX, 11Z)
# 11Z = (11B, XXX)
# 22A = (22B, XXX)
# 22B = (22C, 22C)
# 22C = (22Z, 22Z)
# 22Z = (22B, 22B)
# XXX = (XXX, XXX)'''.split('\n') 

instructions = list(lines[0].strip('\n'))

maps = {}
for line in lines[2:]:
    line = line.strip('\n')
    location = line.split(' = ')[0]
    left = line.split(' = (')[1].split(',')[0]
    right = line.split(' = (')[1].split(', ')[1][:-1]
    maps[location] = {"L": left, "R": right}

steps = 0
instructionIndex = 0
currentLocations = [x for x in maps.keys() if x[2] == 'A']
distanceSinceLastOne = [(0, 0) for x in maps.keys() if x[2] == 'A']
while True:
    direction = instructions[instructionIndex]
    if instructionIndex == len(instructions) -1:
        instructionIndex = 0
    else:
        instructionIndex += 1

    steps += 1
    for i, location in enumerate(currentLocations):
        currentLocations[i] = maps[location][direction]
        if currentLocations[i][2] == 'Z' and i == 5:
            distanceSinceLastOne[i] = (steps - distanceSinceLastOne[i][0], steps)
            print(f"{i} - {distanceSinceLastOne[i]}")

    if all([x[2] == 'Z' for x in currentLocations]):
        break
    elif steps % 1000000 == 0:
        print(f"Steps: {steps} - CurrentLocations: {currentLocations}")

print(f"Total steps: {steps}")
