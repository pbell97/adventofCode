filePath = "./8-input.txt"

# Get input from file
lines = []
with open(filePath, "r") as f:
    lines = f.readlines()

# Sample input
# lines = '''RL

# AAA = (BBB, CCC)
# BBB = (DDD, EEE)
# CCC = (ZZZ, GGG)
# DDD = (DDD, DDD)
# EEE = (EEE, EEE)
# GGG = (GGG, GGG)
# ZZZ = (ZZZ, ZZZ)'''.split('\n') 

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
currentLocation = 'AAA'
while True:
    direction = instructions[instructionIndex]
    if instructionIndex == len(instructions) -1:
        instructionIndex = 0
    else:
        instructionIndex += 1

    currentLocation = maps[currentLocation][direction]
    steps += 1

    if currentLocation == "ZZZ":
        break

print(f"Total steps: {steps}")