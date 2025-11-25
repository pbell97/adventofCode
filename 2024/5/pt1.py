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

total = 0
for update in updates:
    isValid = True
    for number in update:
        numbersBefore = update[:update.index(number)]
        numbersAfter = update[update.index(number)+1:]
        numbersThatCantBeAfter = rules[number]['after']
        numbersThatCantBeBefore = rules[number]['before']

        # print(f"{number}")
        # print(f"{numbersBefore} - {numbersAfter}")
        # print(f"{needsToBeAfter} - {needsToBeBefore}")

        areSomeBefore = any(i in numbersBefore for i in numbersThatCantBeBefore)
        areSomeAfter = any(i in numbersAfter for i in numbersThatCantBeAfter)
        # print(f"{areSomeBefore} - {areSomeAfter}")
        if areSomeBefore or areSomeAfter:
            isValid = False
            break
    if isValid:
        total += int(update[len(update)//2])

print(total)