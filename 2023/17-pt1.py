from itertools import chain
filePath = "D:/repos/Testbed/AdventOfCode/2023/17-input.txt"

# Get input from file
lines = []
with open(filePath, "r") as f:
    lines = f.readlines()

lines = [x.strip('\n') for x in lines]

# Sample input
lines = '''2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533'''.split('\n')


class MasterMap:
    def __init__(self):
        self.nodes = []
        self.maxHeight = 0
        self.maxWidth = 999
        self.visitedNodes = []
        self.unvisitedNodes = []
        # self.shortestDistanceToEachNode = [] # Grid, each (i,j) represents its shortest distance so far

    def SetNodes(self, nodes):
        self.nodes = nodes

    def AddRowOfNodes(self, nodes):
        self.nodes.append(nodes)
        self.maxHeight += 1
        self.maxWidth = min(self.maxWidth, len(nodes)- 1) 
        self.unvisitedNodes += nodes
        # self.shortestDistanceToEachNode.append([99999999]*len(nodes))

    def GetNode(self, row, column):
        return self.nodes[row][column]
    
    
class Node:
    def __init__(self, row, column, masterMap, heatValue):
        self.row = row
        self.column = column
        self.masterMap = masterMap
        self.heatValue = heatValue
        self.distance = 99999999
        self.visited = False
        self.pathFromSource = []

    def MarkAsVisited(self):
        self.visited = True
        self.masterMap.visitedNodes.append(self)
        self.masterMap.unvisitedNodes.remove(self)

    def SetPathFromSource(self, path):
        self.pathFromSource = path + [(self.row, self.column)]

    def SetDistanceAndPath(self, distance, path):
        self.distance = distance
        self.SetPathFromSource(path)

    def GetPosition(self):
        return (self.row, self.column)

    def GetRightNode(self):
        if self.column == self.masterMap.maxWidth:
            return None
        else:
            return self.masterMap.GetNode(self.row, self.column + 1)
        
    def GetLeftNode(self):
        if self.column == 0:
            return None
        else:
            return self.masterMap.GetNode(self.row, self.column - 1)
        
    def GetUpNode(self):
        if self.row == 0:
            return None
        else:
            return self.masterMap.GetNode(self.row -1 , self.column)
        
    def GetDownNode(self):
        if self.row == self.masterMap.maxWidth:
            return None
        else:
            return self.masterMap.GetNode(self.row + 1 , self.column)
        
    def GetNeighbors(self):
        neighbors = [self.GetDownNode(), self.GetUpNode(), self.GetLeftNode(), self.GetRightNode()]
        return [node for node in neighbors if node != None]

masterMap = MasterMap()
for i, line in enumerate(lines):
    row = []
    for j, char in enumerate(line):
        row.append(Node(i, j, masterMap, int(char)))
    masterMap.AddRowOfNodes(row)



root = masterMap.GetNode(0, 0)
root.SetDistanceAndPath(0, [])
destinationNode = masterMap.GetNode(masterMap.maxHeight-1, masterMap.maxWidth-1)

currentNode = root

while len(masterMap.unvisitedNodes) != 0:
    nodeNeighbors = currentNode.GetNeighbors()
    for neighbor in nodeNeighbors:
        distance = currentNode.distance + neighbor.heatValue
        if distance < neighbor.distance:
            neighbor.SetDistanceAndPath(distance, currentNode.pathFromSource)

    currentNode.MarkAsVisited()

    # Pick smallest edge where the vertex hasn't been chosen
    shortest = Node(-1,-1, masterMap, 99999999999)
    for node in masterMap.unvisitedNodes:
        if node.distance < shortest.distance:
            shortest = node
    currentNode = shortest

print(f"Shortest path to corner: {destinationNode.distance}")