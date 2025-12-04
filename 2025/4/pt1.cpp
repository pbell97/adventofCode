#include <filesystem>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

#include "../Utilities.h"
using namespace std;

void PuzzleSolution(vector<string> input, vector<string> arguments) {
    int totalRolls = 0;
    for (int rowNum = 0; rowNum < input.size(); rowNum++) {
        string row = input[rowNum];
        for (int colNum = 0; colNum < row.size(); colNum++) {
            if (row.at(colNum) != '@') {
                continue;
            }
            string upperRow = rowNum == 0 ? "" : input[rowNum - 1];
            string lowerRow = rowNum == (input.size() - 1) ? "" : input[rowNum + 1];
            int adjacentRolls = 0;
            adjacentRolls += (colNum != 0 && row.at(colNum - 1) == '@') ? 1 : 0;                         // Left
            adjacentRolls += (colNum != (row.size() - 1) && row.at(colNum + 1) == '@') ? 1 : 0;          // Right
            adjacentRolls += (upperRow != "" && upperRow.at(colNum) == '@') ? 1 : 0;                     // Up
            adjacentRolls += (lowerRow != "" && lowerRow.at(colNum) == '@') ? 1 : 0;                     // Down
            adjacentRolls += (upperRow != "" && colNum != 0 && upperRow.at(colNum - 1) == '@') ? 1 : 0;  // UpperLeft
            adjacentRolls +=
                (upperRow != "" && colNum != (row.size() - 1) && upperRow.at(colNum + 1) == '@') ? 1 : 0;  // UpperRight
            adjacentRolls += (lowerRow != "" && colNum != 0 && lowerRow.at(colNum - 1) == '@') ? 1 : 0;    // LowerLeft
            adjacentRolls +=
                (lowerRow != "" && colNum != (row.size() - 1) && lowerRow.at(colNum + 1) == '@') ? 1 : 0;  // LowerRight

            totalRolls += adjacentRolls < 4 ? 1 : 0;
        }
    }
    cout << "Total: " << totalRolls << endl;
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
