#include <algorithm>
#include <filesystem>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

#include "../Utilities.h"
using namespace std;

struct Range {
    long long start;
    long long end;

    Range(long long _start, long long _end) : start(_start), end(_end) {}
};

void PuzzleSolution(vector<string> input, vector<string> arguments) {
    // Your puzzle solution here
    // Sort ranges into list based on first ID in range
    vector<Range> ranges;
    vector<long long> availableIngredients;
    bool gettingRanges = true;
    for (int i = 0; i < input.size(); i++) {
        if (input[i] == "" || input[i] == "\n") {
            gettingRanges = false;
            continue;
        }
        if (gettingRanges) {
            vector<string> range = SplitString(input[i], "-");
            ranges.push_back(Range(stoll(range[0]), stoll(range[1])));
        } else {
            availableIngredients.push_back(stoll(input[i]));
        }
    }
    sort(ranges.begin(), ranges.end(), [](Range a, Range b) { return a.start < b.start; });

    for (int i = 0; i < ranges.size(); i++) {
        cout << ranges[i].start << endl;
    }
    int totalFresh = 0;
    for (int i = 0; i < availableIngredients.size(); i++) {
        long long ingredient = availableIngredients[i];
        bool isFresh = false;
        for (int j = 0; j < ranges.size(); j++) {
            Range range = ranges[j];
            if (range.start > ingredient) {
                break;
            } else if (range.start <= ingredient && ingredient <= range.end) {
                isFresh = true;
                cout << ingredient << " is in range: " << range.start << " - " << range.end << endl;
                break;
            }
        }
        totalFresh += isFresh ? 1 : 0;
    }

    cout << "Total: " << totalFresh << endl;

    // Loop thru available Ids
    // For each range, if range[0] <= x <= range[1] Mark as fresh
    // If range[0] > x 'continue'
    // Else try next one
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
