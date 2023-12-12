import itertools
filePath = "./12-input.txt"

# Get input from file
lines = []
with open(filePath, "r") as f:
    lines = f.readlines()

lines = [x.strip('\n') for x in lines]

# Sample input
# lines = '''???.### 1,1,3
# .??..??...?##. 1,1,3
# ?#?#?#?#?#?#?#? 1,3,1,6
# ????.#...#... 4,1,1
# ????.######..#####. 1,6,5
# ?###???????? 3,2,1'''.split('\n')

springs = [(x.split()[0], [int(y) for y in x.split()[1].split(',')] if len(x.split())>1 else []) for x in lines]


def SplitGiven(given):
    original = []
    current = ""
    for char in given:
        if current == "" or current[-1] == char:
            current += char
        else:
            original.append(current)
            current = char
    if (current != ""):
        original.append(current)

    return original

def matchesLine(originalLine, givenLine):
    for i,char in enumerate(originalLine):
        if char != "?" and givenLine[i] != char:
            return False
    return True

def satisfiesRules(givenLine, parity):
    splitLine = [x for x in givenLine.split('.') if x != '']
    expectedGroups = ['#'*i for i in parity]
    return splitLine == expectedGroups
    


def FindPermutations(springLine):
    groups = []
    remainingLineLength = len(springLine[0])
    for i, num in enumerate(springLine[1]):
        candidate = "#"*num
        if (i == 0):
            candidate += '.'
        elif i == len(springLine[1])-1:
            candidate = '.' + candidate
        # TODO: if its an odd and not the first and not the last and not next to the last, put period on either side
        # else:
        #     candidate = '.' + candidate + '.'

        groups.append(candidate)
        remainingLineLength -= len(candidate)

    for i in range(remainingLineLength):
        groups.append('.')

    count = 0
    validCombos = []
    for combo in itertools.permutations(groups):
        count += 1
        if (count%1000000 == 0):
            print(count)
        combo = "".join(combo)
        if matchesLine(springLine[0], combo) and satisfiesRules(combo, springLine[1]):
            validCombos.append(combo)
    
    return len(list(set(validCombos)))


# print(FindPermutations(springs[0]))  
bigCount = 0
for spring in springs:
    answer = FindPermutations(spring)
    bigCount += answer
    print(answer)

print(f"\nFINAL: {bigCount}")