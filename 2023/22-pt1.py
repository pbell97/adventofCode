import time
filePath = "D:/repos\Testbed\AdventOfCode/2023/22-input.txt"

# Get input from file
lines = []
with open(filePath, "r") as f:
    lines = f.readlines()

lines = [x.strip('\n') for x in lines]

# Sample input
lines = '''1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9'''.split('\n')

maxZLevel = max([int(x.split(',')[-1]) for x in lines])

# MasterList - List of lists each list is a z level
    # If a brick is on multiple z levels then it is repeated in all the lists
levels = [[[]]*(maxZLevel+1)][0]


# Brick object
    # DoesIntersect - Given another brick, check if they intersect
    # MoveBrick - references the masterList and updates all ones that contain me. Likely just means moving it down one and removing the top most reference 

class Location:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class Brick:
    def __init__(self, startingFrontCoords, startingEndCoords, levels):
        self.startingFrontCoords = startingFrontCoords
        self.startingEndCoords = startingEndCoords

        self.currentFrontCoords = startingFrontCoords
        self.currentEndCoords = startingEndCoords

        self.levels = levels

    def GetMyOccupyingLocations(self):
        mySpots = [(self.currentFrontCoords.x, self.currentFrontCoords.y, self.currentFrontCoords.z)]
        if (self.currentFrontCoords.x != self.currentEndCoords.x):
            for i in range(self.currentEndCoords.x - self.currentFrontCoords.x):
                mySpots.append((self.currentFrontCoords.x + i + 1, self.currentFrontCoords.y, self.currentFrontCoords.z))
        elif (self.currentFrontCoords.y != self.currentEndCoords.y):
            for i in range(self.currentEndCoords.y - self.currentFrontCoords.y):
                mySpots.append((self.currentFrontCoords.x, self.currentFrontCoords.y + i + 1, self.currentFrontCoords.z))
        elif (self.currentFrontCoords.z != self.currentEndCoords.z):
            for i in range(self.currentEndCoords.z - self.currentFrontCoords.z):
                mySpots.append((self.currentFrontCoords.x, self.currentFrontCoords.y, self.currentFrontCoords.z + i + 1))
        return mySpots

    def DoesIntersect(self, otherBrick):
        mySpots = self.GetMyOccupyingLocations()
        otherSpots = otherBrick.GetMyOccupyingLocations()
        for spot in mySpots:
            if spot in otherSpots:
                return True
        return False

brick = Brick(Location(5,5,5), Location(5,5,7), [])

print(brick.GetMyOccupyingLocations())




# Make nest arrays or array of objects and seed it

# Start at bottom most brick and see if it can move down, if so move it, do so for all bricks from bottom up
    # Repeat until bricks are stationary

# Then one by one, starting at the bottom temporarily remove a brick and then repeat the above process and see if any can move, if any can then break out of the loop and count that was as so