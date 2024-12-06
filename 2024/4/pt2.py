import re
useSample = False
filePath = f"./{'sample' if useSample else 'input'}.txt"

# Get input from file
lines = []
with open(filePath, "r") as f:
    lines = [x.strip('\n') for x in f.readlines()]

total = 0

maxWidth = len(lines[0]) -1
maxHeight = len(lines) -1
for row in range(len(lines)):
    for col in range(len(lines[row])):
        if row > 0 and row < maxHeight and col > 0 and col < maxWidth and lines[row][col] == "A":
            downRight = f"{lines[row-1][col-1]}{lines[row][col]}{lines[row+1][col+1]}"
            downLeft = f"{lines[row-1][col+1]}{lines[row][col]}{lines[row+1][col-1]}"
            if (downRight == "MAS" or downRight == "SAM") and (downLeft == "MAS" or downLeft == "SAM"):
                print(f"Found at {row}, {col} - {downRight} - {downLeft}")
                total += 1


print(total)