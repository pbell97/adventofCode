useSample = False
filePath = f"./{'sample' if useSample else 'input'}.txt"

# Get input from file
lines = []
with open(filePath, "r") as f:
    lines = f.readlines()

left = []
right = []

for line in lines:
    line = line.split('   ')
    left.append(int(line[0]))
    right.append(int(line[1]))

left.sort()
right.sort()

total = 0
for num1, num2 in zip(left, right):
    total += abs(num1 - num2)


print("Sum: ", total)
