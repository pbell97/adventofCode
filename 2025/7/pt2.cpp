#include <chrono>
#include <filesystem>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

#include "../Utilities.h"
using namespace std;

// Every time it hits one,

// Recursive function
// Every time it hits one first go left, then go right, if its the bottom then increment a pointer value count

// Row and col are where it is right now when passed in
void Search(vector<string>& input, int row, int col, long long& finalCount) {
    if (finalCount % 100000000 == 0) {
        auto now = chrono::system_clock::now();
        auto time_t = chrono::system_clock::to_time_t(now);
        cout << "Current Count: " << finalCount << " at " << ctime(&time_t);
    }

    if (row == input.size() - 1) {
        finalCount += 1;
        return;
    }
    if (input[row + 1][col] == '.') {
        Search(input, row + 1, col, finalCount);
    } else if (input[row + 1][col] == '^') {
        Search(input, row + 1, col - 1, finalCount);  // Left
        Search(input, row + 1, col + 1, finalCount);  // Right
    }
}

void PuzzleSolution(vector<string> input, vector<string> arguments) {
    // Your puzzle solution here
    int startingCol = input[0].find('S');
    input[1][startingCol] = '|';
    long long combinations = 0;
    int runs = 0;

    Search(input, 1, startingCol, combinations);

    cout << "Combos: " << combinations << endl;
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
