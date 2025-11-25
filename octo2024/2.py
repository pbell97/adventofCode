# Pt 1 Answer: 26069111
# print(sum(map(lambda x: x*x, filter(lambda x: x > 0, map(int,open("./2.txt", "r").read().split("\n")[:-1])))))
print(sum(x*x for x in map(int, open("./2.txt").read().split()) if x > 0))

# Pt 2 Answer: 999
def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    p = 2
    while p * p <= limit:
        if primes[p]:
            for i in range(p * p, limit + 1, p):
                primes[i] = False
        p += 1
    return [p for p in range(2, limit + 1) if primes[p]]

def sum_primes_from_file(file_path):
    with open(file_path, "r") as f:
        numbers = list(map(int, f.read().split()))
    if not numbers:
        return 0
    limit = max(numbers)*max(numbers)
    primes = set(sieve_of_eratosthenes(limit))
    primeNums = [num for num in numbers if num in primes]
    print(primeNums)
    return sum(num for num in numbers if num in primes)

# Example usage:
file_path = "./2-2.txt"
print(sum_primes_from_file(file_path))

def IsPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
        

# Pt 2 again
numbers = map(int, open("./2-2.txt").read().split())
t = [num for num in numbers if not any([num % i == 0 for i in range(2, num)]) and num > 1]

# Pt 2 simpler
print(sum([num for num in map(int, open("./2-2.txt").read().split()) if not any([num % i == 0 for i in range(2, num)]) and num > 1]))
