filePath = "./5-input.txt"

# Get input from file
lines = []
# with open(filePath, "r") as f:
#     lines = f.readlines()

# Sample input
lines = '''seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4'''.split('\n')


# Sort ranges within a map to be by order of givenSource, take the first that fits the bottom of the givenSeed and see how far it lets you go (add new range to a list), then what ever the leftover range is use that as the new values


seedInputs = [int(x) for x in lines[0].split(': ')[1].split(' ')]
seeds = []
minLocation = 999999999999999999999999999999


# Get pairs of seed value and ranges added to list of seeds
# for i in range(0, len(seedInputs), 2):
#     baseSeed = int(seedInputs[i])
#     maxSeed = baseSeed + int(seedInputs[i+1])
#     print(f"On seed group {baseSeed}")
#     for num in range(int(seedInputs[i+1])):
#         location = FindLocation(baseSeed + num)
#         if (location < minLocation):
#             minLocation = location

#(48, 104)
def GetMapping(givenMinSeed, givenMaxSeed):
    given = '''50 98 2
52 50 48'''.split('\n')
    
    # List of (destination, source, convertRange)
    ranges = []
    for line in given:
        nums = line.split(' ')
        ranges.append((int(nums[0]),int(nums[1]),int(nums[2])))

    # Sort ranges based on starting source
    ranges.sort(key=lambda x:x[1])

    newRanges = []

    currentMinSeed = givenMinSeed
    currentMaxSeed = givenMaxSeed
    for range in ranges:
        lowerLimit = range[1]
        upperLimit = range[1] + range[2]
        diff = range[0]-range[1]

        # If values are completely out of the range, ignore it              
        if currentMaxSeed < lowerLimit:
            newRanges.append((currentMinSeed, currentMaxSeed))
            break # If ranges are sorted, then no future ranges will work so just use given numbers for next one

        # This range is too small, move to next one
        if currentMinSeed > upperLimit:
            continue

        # Seeds are fully contained by the range
        if currentMinSeed >= lowerLimit and currentMaxSeed <= upperLimit:
            # Get dif in dest and source and add it to minSeed and maxSeed
            newRanges.append( ( diff + currentMinSeed, diff + currentMaxSeed) )
            break # Continue

        # Only bottom part of seeds are contained by range
        if currentMinSeed >= lowerLimit and currentMaxSeed > upperLimit:
            newRanges.append( ( diff + currentMinSeed, diff + upperLimit) ) 
            currentMinSeed = upperLimit
        
        # Only upper part of seeds are contained by range
        if currentMinSeed < lowerLimit and currentMaxSeed >= lowerLimit and currentMaxSeed <= upperLimit:
            newRanges.append( ( diff + lowerLimit, diff + currentMaxSeed) ) 
            currentMaxSeed = lowerLimit

        # Seeds contain the full range but it goes over some
        if currentMinSeed < lowerLimit and currentMaxSeed > upperLimit:
            newRanges.append( ( currentMinSeed,lowerLimit-1) ) 
            newRanges.append( ( diff + lowerLimit, diff + upperLimit) ) 
            currentMinSeed = upperLimit

        # If given seeds have been fully evaluated move on
        if currentMinSeed == 0 and currentMaxSeed == 0:
            break
    
    # If there are left over numbers, add them to the new ranges as-is
    if currentMinSeed != currentMaxSeed:
        newRanges.append( ( currentMinSeed, currentMaxSeed ) ) #TODO: Fix range

    print(newRanges)

GetMapping(48, 104)


# # Loop through 7 times (spaces)
# def FindLocation(seed):
#     foundMatchInCurrentSection = False
#     currentSource = seed
#     for line in lines[2:]:
#         # If empty line, swapping maps
#         if line.isspace():
#             foundMatchInCurrentSection = False
#             continue
#         # Ignore map headers and ignore if we already have mapped currentSource
#         if ":" in line or foundMatchInCurrentSection:
#             continue
#         # If currentSource is in the range, update value
#         (destination, source, convertRange) = line.split(' ')
#         if currentSource >= int(source) and currentSource <= int(source) + int(convertRange):
#             currentSource = currentSource - int(source) + int(destination)
#             foundMatchInCurrentSection = True
#     return currentSource





# print(f"Min location: {minLocation}")
        