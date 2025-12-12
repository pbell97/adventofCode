#include <filesystem>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

#include "../Utilities.h"
using namespace std;

struct Coordinate {
    long long x;
    long long y;

    Coordinate(long long _x, long long _y) : x(_x), y(_y) {}

    long long BoxArea(Coordinate otherCoord) const { return abs(x - otherCoord.x + 1.0) * abs(y - otherCoord.y + 1.0); }
};

void PuzzleSolution(vector<string> input, vector<string> arguments) {
    // Your puzzle solution here
    long long largestArea = 0;
    vector<Coordinate> coords;
    for (long long i = 0; i < input.size(); i++) {
        vector<string> coord = SplitString(input[i], ",");
        coords.push_back(Coordinate(stoll(coord[0]), stoll(coord[1])));
    }

    for (const auto& coord : coords) {
        for (const auto& otherCoord : coords) {
            long long area = coord.BoxArea(otherCoord);
            if (area > largestArea) {
                largestArea = area;
                cout << area << " is larger" << endl;
            }
        }
    }

    cout << "Largest area: " << largestArea << endl;
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
