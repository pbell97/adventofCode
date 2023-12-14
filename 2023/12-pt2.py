import itertools
filePath = "./12-input.txt"

# Get input from file
lines = []
with open(filePath, "r") as f:
    lines = f.readlines()

lines = [x.strip('\n') for x in lines]

# Sample input
lines = '''???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1'''.split('\n')

springs = [(x.split()[0], [int(y) for y in x.split()[1].split(',')] if len(x.split())>1 else []) for x in lines]

# TODO: Multiple input by 5

def matchesLine(originalLine, givenLine):
    for i,char in enumerate(originalLine):
        if char != "?" and givenLine[i] != char:
            return False
    return True

def satisfiesRules(givenLine, parity):
    splitLine = [x for x in givenLine.split('.') if x != '']
    expectedGroups = ['#'*i for i in parity]
    return splitLine == expectedGroups


def FindCombinations(springLine):
    groups = []
    remainingLineLength = len(springLine[0])
    for i, num in enumerate(springLine[1]):
        candidate = "#"*num
        if (i == 0):
            candidate += '.'
        elif i == len(springLine[1])-1 and len(springLine[1]) != 2:
            candidate = '.' + candidate
        elif i == 2 and len(springLine[1]) >= 5 or i == 4 and len(springLine[1]) >= 7:
            candidate = '.' + candidate + '.'

        groups.append(candidate)
        remainingLineLength -= len(candidate)

    for i in range(remainingLineLength):
        groups.append('.')

    validCombos = []
    for combo in itertools.product(["#", '.'], repeat=len(springLine[0])):
        combo = "".join(combo)
        if matchesLine(springLine[0], combo) and satisfiesRules(combo, springLine[1]):
            validCombos.append(combo)
    
    return len(list(set(validCombos)))


# TODO: Thinking you need to break it down into groups of '?', find the permutations for those and recursively loop through them, while still keeping the real spaces in between  ( might not work for all '?' input tho)


bigCount = 0
for i,spring in enumerate(springs):
    answer = FindCombinations(spring)
    bigCount += answer
    print(f"{i} - answer: {answer}. CurrentCount: {bigCount}")

print(f"\nFINAL: {bigCount}")