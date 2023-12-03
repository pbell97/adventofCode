filePath = "./1-input.txt"

# Get input from file
lines = []
with open(filePath, "r") as f:
    lines = f.readlines()

numbers = []

for line in lines:
    firstDigit = ""
    secondDigit = ""
    for i in range(len(line)):
        try:
            digit = int(line[i])
            if (firstDigit == ""):
                firstDigit = digit
                secondDigit = digit
            else:
                secondDigit = digit
        except:
            None
    numbers.append(int(f"{firstDigit}{secondDigit}"))


print("Sum: ", sum(numbers))
