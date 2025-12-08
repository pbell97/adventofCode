#include <filesystem>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

#include "../Utilities.h"
using namespace std;

void PuzzleSolution(vector<string> input, vector<string> arguments) {
    // Your puzzle solution here
    int startingCol = input[0].find('S');
    input[1][startingCol] = '|';
    int timesSplit = 0;
    for (int i = 2; i < input.size(); i++) {
        for (int j = 0; j < input[i].size(); j++) {
            if (input[i - 1][j] == '|') {
                if (input[i][j] == '^') {
                    input[i][j - 1] = '|';
                    input[i][j + 1] = '|';
                    timesSplit += 1;
                } else {
                    input[i][j] = '|';
                }
            }
        }
    }
    cout << "Times split: " << timesSplit << endl;
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
