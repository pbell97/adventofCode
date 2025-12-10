#include <algorithm>
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

    double ClosestCoordDistance = 99999999.0;
    string ClosestCoord;

    Coordinates(int _x, int _y, int _z) : x(_x), y(_y), z(_z) {}

    string Key() { return to_string(x) + "," + to_string(y) + "," + to_string(z); }

    double Distance(Coordinates otherCoord) {
        return sqrt((pow((x - otherCoord.x), 2) + pow((y - otherCoord.y), 2) + pow((z - otherCoord.z), 2)));
    }
};

// ERROR: NEED TO GET LIST OF ALL CONNECTIONS POSSIBLE. IF YOU GET TO A JUNCTION AND ITS ALREADY BEEN CONNECTED
// PREVIUSLY THEN CONNECT IT TO THE NEXT CLOSEST NEED TO LOOP THROUGH POSSILBE CONNECTION INSTEAD OF JUST COORDS

void PuzzleSolution(vector<string> input, vector<string> arguments) {
    // Your puzzle solution here
    vector<Coordinates> coords;
    for (const auto& line : input) {
        vector<string> split = SplitString(line, ",");
        coords.push_back(Coordinates(stoi(split[0]), stoi(split[1]), stoi(split[2])));
    }

    // Find closest coord for each coord
    for (int i = 0; i < coords.size(); i++) {
        Coordinates& currentCoord = coords[i];

        for (int j = 0; j < coords.size(); j++) {
            if (j == i) {
                continue;
            }
            double distance = currentCoord.Distance(coords[j]);
            if (distance < currentCoord.ClosestCoordDistance) {
                currentCoord.ClosestCoordDistance = distance;
                currentCoord.ClosestCoord = coords[j].Key();
            }
        }
    }

    // Find shortest pair
    sort(coords.begin(), coords.end(),
         [](const Coordinates& a, const Coordinates& b) { return a.ClosestCoordDistance < b.ClosestCoordDistance; });

    for (int i = 0; i < coords.size(); i++) {
        cout << coords[i].Key() << " is " << coords[i].ClosestCoordDistance << " away from " << coords[i].ClosestCoord
             << endl;
    }

    cout << endl;

    // Make some circuits
    unordered_map<string, int> coordToCircuitMap;
    unordered_map<int, vector<string>> circuitToCoordsMap;
    int limit = 10;
    for (int i = 0; i < coords.size(); i++) {
        Coordinates currentCoord = coords[i];
        Coordinates* closestCoord = nullptr;
        for (auto& potentialMatch : coords) {
            if (potentialMatch.Key() == coords[i].ClosestCoord) {
                closestCoord = &potentialMatch;
                break;
            }
        }

        bool currentIsInCircuit = coordToCircuitMap.find(currentCoord.Key()) != coordToCircuitMap.end();
        bool closestIsInCircuit = coordToCircuitMap.find(closestCoord->Key()) != coordToCircuitMap.end();

        // If in same circuit already, skip
        if (currentIsInCircuit && closestIsInCircuit &&
            coordToCircuitMap[currentCoord.Key()] == coordToCircuitMap[closestCoord->Key()]) {
            cout << "Skipping " << currentCoord.Key() << " and " << closestCoord->Key() << " - already in same circuit"
                 << endl;
            continue;
        }

        // If this coord already in circuit and closest isn't, add closest to circuit
        if (currentIsInCircuit && !closestIsInCircuit) {
            int circuitNumber = coordToCircuitMap[currentCoord.Key()];
            cout << "Adding " << closestCoord->Key() << " to existing circuit " << circuitNumber << " (connected to "
                 << currentCoord.Key() << ")" << endl;
            coordToCircuitMap[closestCoord->Key()] = circuitNumber;
            circuitToCoordsMap[circuitNumber].push_back(closestCoord->Key());
        }

        // If this coord not in a circuit and closest isn't, make a new circuit and add both
        if (!currentIsInCircuit && !closestIsInCircuit) {
            int circuitNumber = circuitToCoordsMap.size() + 1;
            cout << "Creating new circuit " << circuitNumber << " connecting " << currentCoord.Key() << " to "
                 << closestCoord->Key() << endl;
            coordToCircuitMap[currentCoord.Key()] = circuitNumber;
            coordToCircuitMap[closestCoord->Key()] = circuitNumber;
            circuitToCoordsMap[circuitNumber].push_back(currentCoord.Key());
            circuitToCoordsMap[circuitNumber].push_back(closestCoord->Key());
        }

        // If this coord already in circuit and closest is, combine circuits
        if (currentIsInCircuit && closestIsInCircuit) {
            int circuitNumber = coordToCircuitMap[currentCoord.Key()];
            int circuitToCombineNumber = coordToCircuitMap[closestCoord->Key()];
            cout << "Combining circuits " << circuitNumber << " and " << circuitToCombineNumber << " (connecting "
                 << currentCoord.Key() << " to " << closestCoord->Key() << ")" << endl;

            // Update each coord in old circuit to new one
            for (int k = 0; k < circuitToCoordsMap[circuitToCombineNumber].size(); k++) {
                coordToCircuitMap[circuitToCoordsMap[circuitToCombineNumber][k]] = circuitNumber;
            }

            // Combine new one and empty out the old one
            circuitToCoordsMap[circuitNumber].insert(circuitToCoordsMap[circuitNumber].end(),
                                                     circuitToCoordsMap[circuitToCombineNumber].begin(),
                                                     circuitToCoordsMap[circuitToCombineNumber].end());
            circuitToCoordsMap[circuitToCombineNumber].clear();
            circuitToCoordsMap.erase(circuitToCombineNumber);
        }

        // If this coord not in a circuit and closests is, add currentCoord to existing circuit
        if (!currentIsInCircuit && closestIsInCircuit) {
            int circuitNumber = coordToCircuitMap[closestCoord->Key()];
            cout << "Adding " << currentCoord.Key() << " to existing circuit " << circuitNumber << " (connected to "
                 << closestCoord->Key() << ")" << endl;
            coordToCircuitMap[currentCoord.Key()] = circuitNumber;
            circuitToCoordsMap[circuitNumber].push_back(currentCoord.Key());
        }

        int currentNumOfConnections = 0;
        for (const auto& circuit : circuitToCoordsMap) {
            currentNumOfConnections += circuit.second.size() - 1;
        }
        if (currentNumOfConnections == limit) {
            cout << "BREAKING" << endl;
            break;
        } else {
            cout << "Current num of connections: " << currentNumOfConnections << endl;
        }
    }

    cout << endl;
    for (const auto& item : circuitToCoordsMap) {
        cout << "Circuit #" << item.first << " contains " << item.second.size() << " items" << endl;
        for (const auto& item2 : item.second) {
            cout << "\t- " << item2 << endl;
        }
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
