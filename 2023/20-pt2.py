import datetime
filePath = "D:/repos\Testbed\AdventOfCode/2023/20-input.txt"

# Get input from file
lines = []
with open(filePath, "r") as f:
    lines = f.readlines()

lines = [x.strip('\n') for x in lines]

# Sample input
# lines = '''broadcaster -> a
# %a -> inv, con
# &inv -> b
# %b -> con
# &con -> output'''.split('\n')

masterQueue = [] # List of instructions: ex {'target': a, 'signalType': 'low', sendingName: 'a'}
allModules = {}
highCount = 0
lowCount = 0
buttonCount = 0


class Module:
    def __init__(self, name, moduleType, connections, masterQueueRef, allModulesRef):
        self.name = name
        self.moduleType = moduleType
        self.connections = connections
        self.masterQueueRef = masterQueueRef
        self.allModulesRef = allModulesRef

        # Used only for flip flop module
        self.isOn = False

        # Used only for Conjunction modules
        self.inputMemory = {}

    def Receive(self, signalType, sendingName):
        # Types: 'broadcaster', 'button', %, &
        
        # Flip flop
        if self.moduleType == "%":
            # If off and get high, ignore
            if signalType == "high":
                return
            
            # If it gets a low signal it flips between on/off
            else:
                # If it was off, it turns on and sends a high pulse. 
                if not self.isOn:
                    for connection in self.connections:
                        self.masterQueueRef.append({"target": connection, "signalType": "high", "sendingName": self.name})
                # If it was on, it turns off and sends a low pulse
                else:
                    for connection in self.connections:
                        self.masterQueueRef.append({"target": connection, "signalType": "low", "sendingName": self.name})

                self.isOn = not self.isOn
                return

        # Conjunction (Consider building the list before hand...might need to and set to low)
        elif self.moduleType == "&":
            # Remembers what it last received from EACH input. Defaults to low.
            # Updates it memory when receives
                self.inputMemory[sendingName] = signalType
                # If it is high for ALL inputs stored then it sends out a low pulse
                if all([x == "high" for x in self.inputMemory.values()]):
                    for connection in self.connections:
                        self.masterQueueRef.append({"target": connection, "signalType": "low", "sendingName": self.name})
                # Otherwise it sends out a high pulse
                else:
                    for connection in self.connections:
                        self.masterQueueRef.append({"target": connection, "signalType": "high", "sendingName": self.name})
            
        elif self.moduleType == "broadcaster":
            # Sends whatever signal type it got to all signals in its connection
            for connection in self.connections:
                self.masterQueueRef.append({"target": connection, "signalType": signalType, "sendingName": self.name})
        elif self.moduleType == "button":
            # Send low pulse to broadcaster
            self.masterQueueRef.append({"target": "broadcaster", "signalType": "low", "sendingName": self.name})
        else:
            print(f"{self.name} - Don't know what to do with {signalType} {sendingName}")

# Parse input for all modules
for line in lines:
    name = line.split(' -> ')[0]
    connections = line.split(' -> ')[1].split(', ')
    if "broadcaster" not in name:
        moduleType = name[:1]
        name = name[1:]
    else:
        moduleType = "broadcaster"
    module = Module(name, moduleType, connections, masterQueue, allModules)
    allModules[name] = module
allModules["button"] = Module("button", "button", ["broadcaster"], masterQueue, allModules)

# Put empty modules in for those that are just outputs
for module in list(allModules.values()).copy():
    for connection in module.connections:
        if connection not in allModules.keys():
            allModules[connection] = Module(connection, "&", [], masterQueue, allModules)

# Pre-populate the list of inputs for all conjunctions
conjunctionModules = [key for key in allModules.keys() if allModules[key].moduleType == "&"]
for key in conjunctionModules:
    inputs = [x.name for x in allModules.values() if allModules[key].name in x.connections]
    for _input in inputs:
        allModules[key].inputMemory[_input] = "low"

# Main Loop thru all steps
while(True):
    # Add button push
    masterQueue.append({"target": "broadcaster", "signalType": "low", "sendingName": "button"})
    buttonCount += 1
    breakOut = False

    while len(masterQueue) > 0:
        instruction = masterQueue.pop(0)
        if instruction["target"] == "rx" and instruction["signalType"] == "low":
            breakOut = Truer
        if instruction["signalType"] == "high":
            highCount += 1
        else:
            lowCount += 1
        allModules[instruction["target"]].Receive(instruction["signalType"], instruction["sendingName"])

    if buttonCount % 1000000 == 0:
        print(f"{datetime.datetime.now()} - ButtonCount: {buttonCount}")
    if breakOut:
        break


print(f"Final ButtonCount: {buttonCount}")
