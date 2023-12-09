filePath = "./9-input.txt"

# Get input from file
lines = []
with open(filePath, "r") as f:
    lines = f.readlines()

lines = [x.strip('\n') for x in lines]

# Sample input
# lines = '''0 3 6 9 12 15
# 1 3 6 10 15 21
# 10 13 16 21 30 45'''.split('\n')


for i, line in enumerate(lines):
    lines[i] = [int(x) for x in line.split()]


def GetDiffSequences(sequences):
    currentSequence = sequences[-1]
    diff = []
    for i, num in enumerate(currentSequence):
        if i != len(currentSequence) - 1:
            diff.append(currentSequence[i + 1]-currentSequence[i])

    returnedSequences = sequences
    returnedSequences.append(diff)

    if (not all([x == 0 for x in diff])):
        returnedSequences = GetDiffSequences(returnedSequences)

    return returnedSequences


def PredictNextNumInSequences(sequences):
    sequences.reverse()

    # Assumes theres more 2 sequcnes
    if (len(sequences) > 2):
        for i, sequence in enumerate(sequences):
            if i == 0:
                continue
            sequence.append(sequence[-1] + sequences[i-1][-1])
            sequences[i] = sequence
    # If not, that means all numbers in original sequence are the same
    else:
        sequences[1].append(sequences[1][-1])

    return sequences


def GetNextNumForEachSequence(sequence):
    sequences = GetDiffSequences([sequence])
    nextNumIneach = PredictNextNumInSequences(sequences)
    return nextNumIneach[-1][-1]


newValues = []

for line in lines:
    newValues.append(GetNextNumForEachSequence(line))

print(f"Sum of next numbers: {sum(newValues)}")
