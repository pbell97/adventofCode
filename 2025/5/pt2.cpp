#include <algorithm>
#include <climits>
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

    // 3-5
    // 10-14
    // 12-18
    // 16-20

    vector<Range> combinedRanges;
    int currentRangeCount = combinedRanges.size();
    for (int i = 0; i < ranges.size(); i++) {
        Range currentRange = ranges[i];
        Range nextRange = i < (ranges.size() - 1) ? ranges[i + 1] : Range(LLONG_MAX, LLONG_MAX);
        Range previouslyCombinedRange =
            combinedRanges.size() != 0 ? combinedRanges[combinedRanges.size() - 1] : Range(0, 0);

        // If current range is already overlapping with previously combined range - Edit the end of the previously
        // combined range
        if (currentRange.start <= previouslyCombinedRange.end && currentRange.end >= previouslyCombinedRange.end) {
            combinedRanges[combinedRanges.size() - 1].end = currentRange.end;
        }

        // If Current range overlaps but doesn't exceed next range, combine the two and skip the next one
        else if (currentRange.end > nextRange.start && nextRange.end >= currentRange.end) {
            combinedRanges.push_back(Range(currentRange.start, nextRange.end));
            i++;
        }

        // If current range overlaps and exceeds next range - skip the next one
        else if (currentRange.end > nextRange.end) {
            i++;
        }

        // If current range is completely encompassing existing range - skip
        else if (currentRange.start <= previouslyCombinedRange.end && currentRange.end <= previouslyCombinedRange.end) {
            i++;
        }

        // If its completely on its own - add it
        else {
            combinedRanges.push_back(currentRange);
        }

        // Log the progress
        for (int i = 0; i < combinedRanges.size(); i++) {
            cout << combinedRanges[i].start << " - " << combinedRanges[i].end << endl;
        }
        cout << endl;
    }

    long long totalFresh = 0;
    for (int i = 0; i < combinedRanges.size(); i++) {
        long long difference = combinedRanges[i].end - combinedRanges[i].start + 1;
        totalFresh += difference;
        cout << combinedRanges[i].start << " - " << combinedRanges[i].end << " is " << difference << " items" << endl;
    }

    cout << "Total: " << totalFresh << endl;
}

// Answers
// 289051156279448
// 286445690950063
// 283745584309001

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
