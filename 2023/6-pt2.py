filePath = "./6-input.txt"

# Get input from file
lines = []
with open(filePath, "r") as f:
    lines = f.readlines()

# Sample input
# lines = '''Time:      7  15   30
# Distance:  9  40  200'''.split('\n')

times = int("".join(lines[0].split()[1:]))
distances = int("".join(lines[1].split()[1:]))

waysToWin = 0
for holdDownTime in range(times):
    calculatedDistance = holdDownTime*(times-holdDownTime)
    if distances < calculatedDistance:
        waysToWin += 1
    elif waysToWin != 0:
        break


print(f"Ways to win for race: {waysToWin}")