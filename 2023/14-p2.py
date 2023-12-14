import itertools
import re
import time

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

def RotateTable90DegreesCounterClockwise(table):
    reversed_rows = [list(row[::-1]) for row in table]
    rotated_matrix = [list(row) for row in zip(*reversed_rows)]
    return ["".join(x) for x in rotated_matrix]


# Pivot the table 90 degrees for setup, Rocks need to push to the left now (North == Left)...
lines = ["".join(x) for x in zip(*lines)]

start = time.time()
for i in range(1000):
    lines = Tilt(lines)
    lines = RotateTable90DegreesCounterClockwise(lines)
    lines = Tilt(lines)
    lines = RotateTable90DegreesCounterClockwise(lines)
    lines = Tilt(lines)
    lines = RotateTable90DegreesCounterClockwise(lines)
    lines = Tilt(lines)
    lines = RotateTable90DegreesCounterClockwise(lines)
    print(f"{i} Count: {GetTableValue(lines)}")

totalTime = time.time() - start

print(f"Count: {GetTableValue(lines)}")
print(f"Total time: {totalTime}")

# for row in lines:
#     print(row)

# groups = Tilt(lines)
# for group in groups:
#     print(group)

# print(f"Count: {GetTableValue(groups)}")
