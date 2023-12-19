import itertools
import re
filePath = "D:/repos/Testbed/AdventOfCode/2023/14-input.txt"

# Get input from file
lines = []
with open(filePath, "r") as f:
    lines = f.readlines()

lines = [x.strip('\n') for x in lines]

# Sample input
# lines = '''O....#....
# O.OO#....#
# .....##...
# OO.#O....O
# .O.....O#.
# O.#..O.#.#
# ..O..#O..O
# .......O..
# #....###..
# #OO..#....'''.split('\n')

# REgex and capture groups \#

# Pivot the table 90 degrees, Rocks need to push to the left now (North == Left)...
lines = ["".join(x) for x in zip(*lines)]

def Tilt(table):
    groups = [re.split(r'(\#)',x) for x in table]
    for i, group in enumerate(groups):
        newGroup = ""
        for chars in group:
            OCount = chars.count('O')
            if OCount > 0:
                newGroup += 'O'*OCount + '.'*(len(chars)-OCount)
            else:
                newGroup += chars
        groups[i] = newGroup

    return groups

def GetTableValue(table):
    count = 0
    lineCount = len(table[0])
    for line in table:
        for i,char in enumerate(line):
            if char == "O":
                count += lineCount - i
    return count

groups = Tilt(lines)
for group in groups:
    print(group)

print(f"Count: {GetTableValue(groups)}")