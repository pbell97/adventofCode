import re
useSample = False
filePath = f"./{'sample' if useSample else 'input'}.txt"

# Get input from file
lines = []
with open(filePath, "r") as f:
    lines = f.readlines()

total = 0
pattern = r"mul\(\d{1,3},\d{1,3}\)"

for line in lines:
    matches = re.findall(pattern, line)
    for match in matches:
        first = match.split('mul(')[1].split(',')[0]
        second = match.split('mul(')[1].split(',')[1][:-1]
        total += int(first) * int(second)

print(total)

