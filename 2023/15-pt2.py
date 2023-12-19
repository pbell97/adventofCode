filePath = "D:/repos/Testbed/AdventOfCode/2023/15-input.txt"

# Get input from file
lines = []
with open(filePath, "r") as f:
    lines = f.readline()

sequences = lines.split(',')

# Sample input
# sequences = '''rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'''.split(',')

def GetHash(sequence):
    count = 0
    for char in sequence:
        count = (count + ord(char))*17 % 256
    return count

def GetFocusingPower(boxIndex, slotIndex, focalLength):
    return (boxIndex + 1) * (slotIndex + 1) * focalLength

# Init boxes
boxes = [{"index": i, "lenses": []} for i in range(256)]

# Operations on box
for sequence in sequences:
    if "-" in sequence:
        label = sequence.split('-')[0]
        boxIndex = GetHash(label)
        box = boxes[boxIndex]
        matchingLenses = [x for x in box["lenses"] if x["label"] == label]
        if len(matchingLenses) > 0:
            box["lenses"].remove(matchingLenses[0])
    elif "=" in sequence:
        label = sequence.split('=')[0]
        focalLength = int(sequence.split('=')[1])
        boxIndex = GetHash(label)
        newLens = {"label": label, "focalLength": focalLength}
        box = boxes[boxIndex]
        matchingLenses = [x for x in box["lenses"] if x["label"] == label]
        if len(matchingLenses) > 0:
            box["lenses"][box["lenses"].index(matchingLenses[0])] = newLens
        else:
            box["lenses"].append(newLens)


totalFocusingPower = 0
for boxIndex, box in enumerate(boxes):
    for lensIndex, lens in enumerate(box["lenses"]):
        totalFocusingPower += GetFocusingPower(boxIndex, lensIndex, lens["focalLength"])

print(f"Total focusing power: {totalFocusingPower}")
