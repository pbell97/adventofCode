first = 22411
second = 18727
third = 24253
fourth = 14429
fifth = 16271
sixth = 20569


def getzs(start, x, multiplier):
    zs = [0]
    for i in range(start, x):
        zs.append(multiplier*i)
    return zs

start = 29999999
count = 39999999
firsts = getzs(start, count, first)
seconds = getzs(start, count, second)
thirds = getzs(start, count, third)
fourths = getzs(start, count, fourth)
fifths = getzs(start, count, fifth)
sixths = getzs(start, count, sixth)

d = [firsts,seconds,thirds,fourths,fifths,sixths]

result = firsts
for item in d:
    result = set(item).intersection(result)

print(result)
# print(firsts[-1], seconds[-1], thirds[-1])

# TODO: Get dif of first and second of each, then use the built in least common multiple to get the answer