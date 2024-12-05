useSample = False
filePath = f"D:/repos/Testbed/adventofCode/2024/2/{'sample' if useSample else 'input'}.txt"

# Get input from file
lines = []
with open(filePath, "r") as f:
    lines = f.readlines()

reports = [line.split(' ') for line in lines]
validReports = 0

for report in reports:
    report = list(map(lambda x: int(x), report))
    isNegative = report[0] - report[1] > 0
    isValid = True
    for i in range(len(report) -1 ):
        difference = report[i] - report[i+1]
        if abs(difference) < 1 or abs(difference) > 3 or difference > 0 and not isNegative or difference < 0 and isNegative:
            isValid = False
            break
    if isValid:
        validReports += 1
        #print(f"Valid report: {report}")


print("Valid reports: ", validReports)
