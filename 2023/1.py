filePath = "./1input.txt"

# Get input from file
lines = []
with open(filePath, "r") as f:
    lines = f.readlines()

possibleNumbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
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
            for word in possibleNumbers:
                try:
                    if line[i:i+len(word)] == word:
                        digit = possibleNumbers.index(word) + 1
                        if (firstDigit == ""):
                            firstDigit = digit
                            secondDigit = digit
                        else:
                            secondDigit = digit
                except:
                    None
    numbers.append(int(f"{firstDigit}{secondDigit}"))


print("Sum: ", sum(numbers))
