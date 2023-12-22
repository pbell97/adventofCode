import json
filePath = "D:/repos\Testbed\AdventOfCode/2023/19-input.txt"

# Get input from file
lines = []
with open(filePath, "r") as f:
    lines = f.readlines()

lines = [x.strip('\n') for x in lines]

# Sample input
# lines = '''px{a<2006:qkq,m>2090:A,rfg}
# pv{a>1716:R,A}
# lnx{m>1548:A,A}
# rfg{s<537:gd,x>2440:R,A}
# qs{s>3448:A,lnx}
# qkq{x<1416:A,crn}
# crn{x>2662:A,R}
# in{s<1351:px,qqz}
# qqz{s>2770:qs,m<1801:hdj,R}
# gd{a>3333:R,R}
# hdj{m>838:A,pv}

# {x=787,m=2655,a=1222,s=2876}
# {x=1679,m=44,a=2067,s=496}
# {x=2036,m=264,a=79,s=2244}
# {x=2461,m=1339,a=466,s=291}
# {x=2127,m=1623,a=2188,s=1013}'''.split('\n')

givenWorkflows = lines[:lines.index("")]
parts = [json.loads(x.replace("x", '"x"').replace("m",'"m"').replace("a",'"a"').replace("s",'"s"').replace("=",":")) for x in lines[lines.index("")+1:]]
workflows = {}

def InterpretWorkflow(givenWorkflow):
    name = givenWorkflow.split('{')[0]
    givenConditions = givenWorkflow.split('{')[1].split(',')
    lastResort = givenConditions.pop()[:-1]
    conditions = []
    for condition in givenConditions:
        symbol = ">" if ">" in condition else "<"
        quality = condition.split(symbol)[0]
        metric = int(condition.split(symbol)[1].split(":")[0])
        outcome = condition.split(":")[1]
        conditions.append({"quality": quality, "symbol": symbol, "value": metric, "outcomeWorkflow": outcome})
    return (name, {"conditions": conditions, "lastResort": lastResort})


for workflow in givenWorkflows:
    outcome = InterpretWorkflow(workflow)
    workflows[outcome[0]] = outcome[1]

def ApproveOrReject(part, workflow):
    nextStep = workflow["lastResort"]
    for condition in workflow["conditions"]:
        if condition["symbol"] == ">":
            Pass = part[condition["quality"]] > condition["value"]
        else:
            Pass = part[condition["quality"]] < condition["value"]
        if Pass:
            nextStep = condition["outcomeWorkflow"]
            break
    if nextStep == "A":
        return True
    elif nextStep == "R":
        return False
    else:
        return ApproveOrReject(part, workflows[nextStep])


approvedParts = [x for x in parts if ApproveOrReject(x, workflows["in"])]
finalValue = sum([sum([p["x"], p["m"], p["a"], p["s"]]) for p in approvedParts])
print(f"Final value: {finalValue}")