useSample = True
filePath = f"D:/repos/Testbed/adventofCode/2024/2/{'sample' if useSample else 'input'}.txt"

# Get input from file
lines = []
with open(filePath, "r") as f:
    lines = f.readlines()

reports = [line.split(' ') for line in lines]
validReports = 0

def IsValidReport(report, checkFurther = True):
    sortedAcs = sorted(report)
    sortedDesc = sorted(report, reverse=True)
    isSorted = report == sortedAcs or report == sortedDesc
    isNotTooLarge = [abs(report[i] - report[i+1]) <= 3 and abs(report[i] - report[i+1]) > 0 for i in range(len(report) - 1)] # This is giving false True's because it doesn't consider direction change...
    result = isSorted and all(isNotTooLarge)
    if not result and checkFurther and isNotTooLarge.count(False) == 1:
        secondResult = IsValidReport(report[:isNotTooLarge.index(False)] + report[isNotTooLarge.index(False) + 1:], False)
        if secondResult:
            result = True
    if (checkFurther):
        print (f"Report: {report} is valid: {result}")

    if (checkFurther and not result):
        print(f"{isNotTooLarge}")
    return result

for report in reports:
    report = list(map(lambda x: int(x), report))
    if IsValidReport(report):
        validReports += 1

print("Valid reports: ", validReports)
