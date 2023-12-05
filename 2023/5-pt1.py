filePath = "./5-input.txt"

# Get input from file
lines = []
with open(filePath, "r") as f:
    lines = f.readlines()

# Sample input
# lines = '''seeds: 79 14 55 13

# seed-to-soil map:
# 50 98 2
# 52 50 48

# soil-to-fertilizer map:
# 0 15 37
# 37 52 2
# 39 0 15

# fertilizer-to-water map:
# 49 53 8
# 0 11 42
# 42 0 7
# 57 7 4

# water-to-light map:
# 88 18 7
# 18 25 70

# light-to-temperature map:
# 45 77 23
# 81 45 19
# 68 64 13

# temperature-to-humidity map:
# 0 69 1
# 1 0 69

# humidity-to-location map:
# 60 56 37
# 56 93 4'''.split('\n')


seeds = [int(x) for x in lines[0].split(': ')[1].split(' ')]
locations = []
print(f"Seeds: {seeds}")

# Loop through 7 times (spaces)
for seed in seeds:
    foundMatchInCurrentSection = False
    currentSource = seed
    for line in lines[2:]:
        # If empty line, swapping maps
        if line.isspace():
            foundMatchInCurrentSection = False
            continue
        # Ignore map headers and ignore if we already have mapped currentSource
        if ":" in line or foundMatchInCurrentSection:
            continue
        # If currentSource is in the range, update value
        (destination, source, convertRange) = line.split(' ')
        if currentSource >= int(source) and currentSource <= int(source) + int(convertRange):
            currentSource = currentSource - int(source) + int(destination)
            foundMatchInCurrentSection = True
    locations.append(currentSource)

print(f"Min location: {min(locations)}")
        