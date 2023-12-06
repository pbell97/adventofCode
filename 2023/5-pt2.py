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


# Sort ranges within a map to be by order of givenSource, take the first that fits the bottom of the givenSeed and see how far it lets you go (add new range to a list), then what ever the leftover range is use that as the new values


seedInputs = [int(x) for x in lines[0].split(': ')[1].split(' ')]
seedRanges = []
for i in range(0, len(seedInputs), 2):
    seedRanges.append((int(seedInputs[i]), int(
        seedInputs[i]) + int(seedInputs[i+1])-1))

# print(f"Seed seedRanges: {seedRanges}\n")


def GetMinLocationOfARange(givenMinSeed, givenMaxSeed, mappings):
    # ex. [(minNumb, maxNum), (minNum, maxNum)]
    currentSeedRanges = [(givenMinSeed, givenMaxSeed)]

    # Loops through the mappings
    for map_ in mappings:
        tempCurrentSeedRanges = []
        # Within each mapping, exhuast all the needed ranges
        for grouping in currentSeedRanges:
            # Sort ranges based on starting source
            map_.sort(key=lambda x: x[1])

            # The resulting ranges constructed from this mapping ex. [(minNumb, maxNum), (minNum, maxNum)]
            newSeedRanges = []

            currentMinSeed = grouping[0]
            currentMaxSeed = grouping[1]
            someAreLeftOver = True

            # Loops through all the ranges within a mapping to get new seed ranges
            for transformationRange in map_:
                lowerLimit = transformationRange[1]
                upperLimit = transformationRange[1] + \
                    transformationRange[2] - 1
                diff = transformationRange[0]-transformationRange[1]

                # If values are completely out of the range, ignore it since they are sorted and this is lowest range available
                if currentMaxSeed < lowerLimit:
                    newSeedRanges.append((currentMinSeed, currentMaxSeed))
                    someAreLeftOver = False
                    break  # If ranges are sorted, then no future ranges will work so just use given numbers for next one

                # This range is too small, move to next one
                elif currentMinSeed > upperLimit:
                    continue

                # Seeds are fully contained by the range
                elif currentMinSeed >= lowerLimit and currentMaxSeed <= upperLimit:
                    # Get dif in dest and source and add it to minSeed and maxSeed
                    newSeedRanges.append(
                        (diff + currentMinSeed, diff + currentMaxSeed))
                    someAreLeftOver = False
                    break

                # Seeds contain the full range but it goes over some
                elif currentMinSeed < lowerLimit and currentMaxSeed > upperLimit:
                    newSeedRanges.append((currentMinSeed, lowerLimit-1))
                    newSeedRanges.append(
                        (diff + lowerLimit, diff + upperLimit))
                    currentMinSeed = upperLimit + 1

                # Only bottom part of seeds are contained by range
                elif currentMinSeed >= lowerLimit and currentMaxSeed > upperLimit:
                    newSeedRanges.append(
                        (diff + currentMinSeed, diff + upperLimit))
                    currentMinSeed = upperLimit + 1

                # Only upper part of seeds are contained by range
                elif currentMinSeed < lowerLimit and currentMaxSeed >= lowerLimit and currentMaxSeed <= upperLimit:
                    newSeedRanges.append((currentMinSeed, lowerLimit-1))
                    newSeedRanges.append(
                        (diff + lowerLimit, diff + currentMaxSeed))
                    someAreLeftOver = False
                    break

            # If there are left over numbers, add them to the new ranges as-is
            if (someAreLeftOver):
                newSeedRanges.append((currentMinSeed, currentMaxSeed))
            newSeedRanges = [
                x for x in newSeedRanges if x[0] != 0 and x[1] != 0 and x[0] != x[1]]

            # At the end of each iteration of a singular map, add the resulting ranges to the temp storage so that when all the interations for this map is done the next map will have the new ones
            tempCurrentSeedRanges += list(set(newSeedRanges))

        currentSeedRanges = tempCurrentSeedRanges

    currentSeedRanges.sort(key=lambda x: x[0])
    minLocation = min([x[0] for x in currentSeedRanges])
    return minLocation


mappings = []
currentRanges = []
for line in lines[2:]:
    # If empty line, swapping maps
    if line.isspace() or line == "\n" or len(line) == 0:
        mappings.append(currentRanges)
        currentRanges = []
        continue
    # Ignore map headers and ignore if we already have mapped currentSource
    elif ":" in line:
        continue
    else:
        # If currentSource is in the range, update value
        (destination, source, convertRange) = line.split(' ')
        currentRanges.append(
            (int(destination), int(source), int(convertRange)))
mappings.append(currentRanges)

allMinLocations = []
for seedRange in seedRanges:
    minLocation = GetMinLocationOfARange(seedRange[0], seedRange[1], mappings)
    allMinLocations.append(minLocation)
    # print(f"Min location for {seedRange}: {minLocation}\n")
print(f"Overall min location: {min(allMinLocations)}")
print()
