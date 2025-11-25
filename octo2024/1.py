print(open("./1-input.txt").read().lower().count('r'))

# Pt 2 Attempt 1
with open("./1-input2.txt") as f:
    lines = f.readlines()
    stats = {"c":0, "l":0}
    for line in lines:
        l = line.lower()
        c = l.count('a') + l.count('e') + l.count('i') + l.count('o') + l.count('u') + l.count('y')
        if c >= stats["c"]:
            stats["c"] = c
            stats["l"] = lines.index(line)
print(stats)

# Pt 2 Attempt 2
with open("./1-input2.txt") as f:
    stats = max((sum(line.lower().count(v) for v in 'aeiouy'), i) for i, line in enumerate(f.readlines()))
print({"c": stats[0], "l": stats[1]})

# Pt 2 Attempt 3
print(max((sum(line.lower().count(v) for v in 'aeiouy'), i) for i, line in enumerate(open("./1-input2.txt"))))