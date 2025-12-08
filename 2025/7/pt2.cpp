#include <chrono>
#include <filesystem>
#include <fstream>
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

#include "../Utilities.h"
using namespace std;

// Memoization - if already been to a node, just save its' # of unqiue combos beneath it

unordered_map<string, long long> memoed;

// Row and col are where it is right now when passed in
long long Search(vector<string>& input, int row, int col) {
    string key = to_string(row) + "," + to_string(col);

    if (memoed.find(key) != memoed.end()) {
        return memoed[key];
    }

    if (row == (input.size() - 1)) {
        memoed[key] = 1;
        return 1;
    }

    long long currentTotal = 0;
    if (input[row + 1][col] == '.') {
        currentTotal += Search(input, row + 1, col);
    } else if (input[row + 1][col] == '^') {
        currentTotal += Search(input, row + 1, col - 1);  // Left
        currentTotal += Search(input, row + 1, col + 1);  // Right
    }

    memoed[key] = currentTotal;
    return currentTotal;
}

void PuzzleSolution(vector<string> input, vector<string> arguments) {
    // Your puzzle solution here
    int startingCol = input[0].find('S');
    input[1][startingCol] = '|';
    int runs = 0;

    long long result = Search(input, 1, startingCol);

    cout << "Combos: " << result << endl;
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

// Answer: 13883459503480