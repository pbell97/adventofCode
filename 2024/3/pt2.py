import re
useSample = False
filePath = f"./{'sample' if useSample else 'input'}.txt"

# Get input from file
lines = []
with open(filePath, "r") as f:
    lines = f.readlines()

total = 0
pattern = r"mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\)"

def Calculate(line):
    first = line.split('mul(')[1].split(',')[0]
    second = line.split('mul(')[1].split(',')[1][:-1]
    return int(first) * int(second)

matches = []

for line in lines:
    matches += re.findall(pattern, line)

do = True
for match in matches:
    if match == "do()":
        do = True
    elif match == "don't()":
        do = False
    elif do:
        total += Calculate(match)


print(total)

