import re
useSample = False
filePath = f"./{'sample' if useSample else 'input'}.txt"

# Get input from file
lines = []
with open(filePath, "r") as f:
    lines = [x.strip('\n') for x in f.readlines()]


def flip_matrix(matrix):
    return [list(row) for row in zip(*matrix)]

total = 0
# Look horizontal
for line in lines:
    total += line.count("XMAS") + line.count("SAMX")

# Look vertical
flippedLines = flip_matrix(lines)
for line in flippedLines:
    line = "".join(line)
    total += line.count("XMAS") + line.count("SAMX")


# Look diagonal
maxWidth = len(lines[0])
maxHeight = len(lines)
for row in range(len(lines)):
    for col in range(len(lines[row])):
        if row + 4 <= maxHeight and col + 4 <= maxWidth:
            downRight = f"{lines[row][col]}{lines[row+1][col+1]}{lines[row+2][col+2]}{lines[row+3][col+3]}"
            if downRight == "XMAS" or downRight == "SAMX":
                total += 1
        if row + 4 <= maxHeight and col >= 3:
            downLeft = f"{lines[row][col]}{lines[row+1][col-1]}{lines[row+2][col-2]}{lines[row+3][col-3]}"
            if downLeft == "XMAS" or downLeft == "SAMX":
                total += 1


print(total)