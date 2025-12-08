#include <cmath>
#include <filesystem>
#include <fstream>
#include <iostream>
#include <map>
#include <string>
#include <unordered_map>
#include <vector>

#include "../Utilities.h"
using namespace std;

struct Coordinates {
    int x;
    int y;
    int z;

    Coordinates(int _x, int _y, int _z) : x(_x), y(_y), z(_z) {}

    string Key() { return to_string(x) + "," + to_string(y) + "," + to_string(z); }

    long Distance(Coordinates otherCoord) {
        return sqrt((pow((x - otherCoord.x), 2) + pow((y - otherCoord.y), 2) + pow((z - otherCoord.z), 2)));
    }
};

// TODO: Would it make any difference to start by finding the shortest pairs FIRST before combining them?

void PuzzleSolution(vector<string> input, vector<string> arguments) {
    // Your puzzle solution here
    vector<Coordinates> coords;
    for (const auto& line : input) {
        vector<string> split = SplitString(line, ",");
        coords.push_back(Coordinates(stoi(split[0]), stoi(split[1]), stoi(split[2])));
    }

    unordered_map<string, int> coordToCircuitMap;
    unordered_map<int, vector<string>> circuitToCoordsMap;

    for (int i = 0; i < coords.size(); i++) {
        Coordinates currentCoord = coords[i];
        long closestDistance = 999999999;
        Coordinates closestCoord = Coordinates(-999999999, -999999999, -999999999);

        for (int j = 0; j < coords.size(); j++) {
            if (j == i) {
                continue;
            }
            long distance = currentCoord.Distance(coords[j]);
            if (distance < closestDistance) {
                closestDistance = distance;
                closestCoord = coords[j];
            }
        }

        bool currentIsInCircuit = coordToCircuitMap.find(currentCoord.Key()) != coordToCircuitMap.end();
        bool closestIsInCircuit = coordToCircuitMap.find(closestCoord.Key()) != coordToCircuitMap.end();

        // If this coord already in circuit and closest isn't, add closest to circuit
        if (currentIsInCircuit && !closestIsInCircuit) {
            int circuitNumber = coordToCircuitMap[currentCoord.Key()];
            coordToCircuitMap[closestCoord.Key()] = circuitNumber;
            circuitToCoordsMap[circuitNumber].push_back(closestCoord.Key());
        }

        // If this coord not in a circuit and closest isn't, make a new circuit and add both
        if (!currentIsInCircuit && !closestIsInCircuit) {
            int circuitNumber = circuitToCoordsMap.size() + 1;
            coordToCircuitMap[currentCoord.Key()] = circuitNumber;
            coordToCircuitMap[closestCoord.Key()] = circuitNumber;
            circuitToCoordsMap[circuitNumber].push_back(currentCoord.Key());
            circuitToCoordsMap[circuitNumber].push_back(closestCoord.Key());
        }

        // If this coord already in circuit and closest is, combine circuits
        if (currentIsInCircuit && !closestIsInCircuit) {
            int circuitNumber = coordToCircuitMap[currentCoord.Key()];
            int circuitToCombineNumber = coordToCircuitMap[closestCoord.Key()];

            // Update each coord in old circuit to new one
            for (int k = 0; k < circuitToCoordsMap[circuitToCombineNumber].size(); k++) {
                coordToCircuitMap[circuitToCoordsMap[circuitToCombineNumber][k]] = circuitNumber;
            }

            // Combine new one and empty out the old one
            circuitToCoordsMap[circuitNumber].insert(circuitToCoordsMap[circuitNumber].end(),
                                                     circuitToCoordsMap[circuitToCombineNumber].begin(),
                                                     circuitToCoordsMap[circuitToCombineNumber].end());
            circuitToCoordsMap[circuitToCombineNumber].clear();
        }

        // If this coord not in a circuit and closests is, add currentCoord to existing circuit
        if (!currentIsInCircuit && closestIsInCircuit) {
            int circuitNumber = coordToCircuitMap[closestCoord.Key()];
            coordToCircuitMap[currentCoord.Key()] = circuitNumber;
            circuitToCoordsMap[circuitNumber].push_back(currentCoord.Key());
        }
    }

    for (const auto& item : circuitToCoordsMap) {
        cout << "Circuit #" << item.first << " contains " << item.second.size() << " items" << endl;
    }
}

int main(int argc, char* argv[]) {
    // Decide between sample or actual input
    bool readSample = false;
    vector<string> additionalArguments;
    if (argc > 1 && string(argv[1]) == "sample") {
        readSample = true;
        cout << "Using sample input\n";
    }

    // Gather additional inputs
    for (int i = (readSample ? 2 : 1); i < argc; i++) {
        additionalArguments.push_back(argv[i]);
    }

    // Read input files
    string currentPath = filesystem::current_path().string();
    string inputPath = currentPath + (readSample ? "/sampleInput.txt" : "/input.txt");
    vector<string> input = ReadFile(inputPath);

    // Run puzzle solution
    PuzzleSolution(input, additionalArguments);
}

// g++ -o pt1.exe .\pt1.cpp ..\Utilities.cpp
// g++ -std=c++23 -o pt1 ./pt1.cpp ../../2025/Utilities.cpp
