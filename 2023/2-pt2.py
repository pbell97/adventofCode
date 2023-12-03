filePath = "./2-input.txt"

# Get input from file
lines = []
with open(filePath, "r") as f:
    lines = f.readlines()

# Game Id is index + 1
games = [" ".join(x.split(' ')[2:]) for x in lines]

# Q: only 12 red cubes, 13 green cubes, and 14 blue cubes
powers = []

for i in range(len(games)):
    game = games[i]
    totalPossibleColors = {"red": 0, "blue": 0, "green": 0}
    handfuls = game.split(';')
    for handful in handfuls:
        groups = handful.split(', ')
        for group in groups:
            count = int(group.lstrip(' ').split(' ')[0])
            color = group.lstrip(' ').split(' ')[1].strip('\n')
            if totalPossibleColors[color] < count:
                totalPossibleColors[color] = count
    powers.append(
        totalPossibleColors["red"]*totalPossibleColors["green"]*totalPossibleColors["blue"])

print("Sum powers: ", sum(powers))
