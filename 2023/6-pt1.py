filePath = "./6-input.txt"

# Get input from file
lines = []
with open(filePath, "r") as f:
    lines = f.readlines()

# Sample input
# lines = '''Time:      7  15   30
# Distance:  9  40  200'''.split('\n')

times = [int(x) for x in lines[0].split()[1:]]
distances = [int(x) for x in lines[1].split()[1:]]

races = [{"time": times[i], "bestDistance": distances[i]} for i in range(len(times))]

waysToWinPerRace = []
for race in races:
    waysToWin = 0
    for holdDownTime in range(race["time"]):
        calculatedDistance = holdDownTime*(race["time"]-holdDownTime)
        if race["bestDistance"] < calculatedDistance:
            waysToWin += 1
        elif waysToWin != 0:
            break
    waysToWinPerRace.append(waysToWin)

finalValue = 1
for way in waysToWinPerRace:
    finalValue = finalValue * way

print(f"Ways to win for each: {waysToWinPerRace}")
print(f"Multiplied: {finalValue}")