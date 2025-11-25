from functools import cmp_to_key
useSample = False
filePath = f"./{'sample' if useSample else 'input'}.txt"

# Get input from file
lines = []
with open(filePath, "r") as f:
    lines = [x.strip('\n') for x in f.readlines()]

rules = {}
updates = []

# Parse input
for line in lines:
    if "|"  in line:
        first = line.split("|")[0]
        second = line.split("|")[1]
        if first not in rules.keys():
            rules[first] = {'before': [], 'after': []}
        if second not in rules.keys():
            rules[second] = {'before': [], 'after': []}
        rules[first]['before'].append(second)
        rules[second]['after'].append(first)   
    if "," in line:
        updates.append(line.split(","))

# 'Before' means means the given number needs to appear before those numbers in the 'before' list
# 'After' means means the given number needs to appear after those numbers in the 'after' list

incorrectUpdates = []

for update in updates:
    isValid = True
    for number in update:
        numbersBefore = update[:update.index(number)]
        numbersAfter = update[update.index(number)+1:]
        numbersThatCantBeAfter = rules[number]['after']
        numbersThatCantBeBefore = rules[number]['before']

        areSomeBefore = any(i in numbersBefore for i in numbersThatCantBeBefore)
        areSomeAfter = any(i in numbersAfter for i in numbersThatCantBeAfter)
        if areSomeBefore or areSomeAfter:
            isValid = False
            break
    if not isValid:
        incorrectUpdates.append(update)


# Doing: Could expand the 'before' and 'after' list to include ALL numbers

for key in rules.keys():
    numbersLookedAt = []
    while (len(numbersLookedAt) < len(rules.keys())-1):
        numbersBefore = rules[key]['before']
        for number in numbersBefore:
            numbersLookedAt.append(number)
            numbersLookedAt = list(set(numbersLookedAt))
            numbersBefore += rules[number]['before']
            numbersBefore = list(set(numbersBefore))

        numbersAfter = rules[key]['after']
        for number in numbersAfter:
            numbersLookedAt.append(number)
            numbersLookedAt = list(set(numbersLookedAt))
            numbersAfter += rules[number]['after']
            numbersAfter = list(set(numbersAfter))

    rules[key]['before'] = numbersBefore
    rules[key]['after'] = numbersAfter

# return a negative value (< 0) when the left item should be sorted before the right item
def SortByRules(a, b):
    if b in rules[a]['before']:
        # print(f"{a} should appear before {b}")
        return -1
    else: 
        return 1

total = 0
for update in incorrectUpdates:
    isValid = True
    sortedUpdate = sorted(update, key=cmp_to_key(SortByRules))
    print(f"Before: {update}")
    print(f"After: {sortedUpdate}")
    total += int(sortedUpdate[len(sortedUpdate)//2])

    
tempL = rules.keys()
tempLSorted = sorted(tempL, key=cmp_to_key(SortByRules))
print(tempLSorted)


print(total)
