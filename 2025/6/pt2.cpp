#include <filesystem>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

#include "../Utilities.h"
using namespace std;

// NOTE: Manually adjust input/col for sample vs real input. Sample has 3 rows of nums and real input has 4
void PuzzleSolution(vector<string> input, vector<string> arguments) {
    // Your puzzle solution here
    long long runningTotal = 0;

    vector<long long> currentProblem;

    // Loop thru each col, starting at the back
    for (int i = input[0].size() - 1; i != -1; i--) {
        // Combine column into string
        string col = string(1, input[0].at(i)) + input[1].at(i) + input[2].at(i) + input[3].at(i);

        // If its an empty string skip
        if (col == "    ") {
            continue;
        }

        // Else convert col to number and push to list
        long long num = stoll(col);
        currentProblem.push_back(num);
        string symbol = string(1, input[4].at(i));

        // If symbol isn't blank then calculate
        if (symbol != " ") {
            long long total = symbol == "+" ? 0 : 1;
            for (const auto& item : currentProblem) {
                if (symbol == "+") {
                    total += item;
                } else {
                    total *= item;
                }
            }
            runningTotal += total;
            currentProblem.clear();
        }
    }
    cout << "Total: " << runningTotal << endl;
}

// 11099321285
// 4387670995909

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
