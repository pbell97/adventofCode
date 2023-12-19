import itertools
import re
filePath = "D:/repos/Testbed/AdventOfCode/2023/15-input.txt"

# Get input from file
lines = []
with open(filePath, "r") as f:
    lines = f.readline()

sequences = lines.split(',')

# Sample input
# sequences = '''rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'''.split(',')

def GetHash(sequence):
    count = 0
    for char in sequence:
        count = (count + ord(char))*17 % 256
    return count


overallCount = 0
for seq in sequences:
    overallCount += GetHash(seq)
print(len(sequences))
print(f"Final value: {overallCount}")

