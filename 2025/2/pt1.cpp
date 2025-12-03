#include <filesystem>
#include <format>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

#include "../Utilities.h"
using namespace std;

bool IsPattern(long givenNum) {
    // Check for repeating starting with begining up thru half the length of the string
    string num = to_string(givenNum);
    if (num.size() % 2 != 0) {
        return false;
    }
    int size = num.size();
    return num.substr(0, size / 2) == num.substr(size / 2, size);
}

void PuzzleSolution(vector<string> input, vector<string> arguments) {
    // Your puzzle solution here

    long total = 0;
    vector<string> ranges = SplitString(input[0], ",");
    for (int i = 0; i < ranges.size(); i++) {
        vector<string> range = SplitString(ranges[i], "-");
        cout << "Starting range: " << range[0] << " - " << range[1] << endl;
        for (long j = stol(range[0]); j < stol(range[1]) + 1; j++) {
            if (to_string(j).size() % 2 != 0) {
                continue;
            }
            if (IsPattern(j)) {
                cout << "\t- " << j << " is a pattern" << endl;
                total += j;
            }
        }
    }
    cout << "Total: " << total << endl;
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

// 6666660033 - 6666677850
// 6666666666 - 6666666666
