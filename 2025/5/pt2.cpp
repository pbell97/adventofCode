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
    sort(ranges.begin(), ranges.end(),
         [](Range a, Range b) { return a.start != b.start ? a.start < b.start : a.end < b.start; });

    vector<Range> combinedRanges;
    int currentRangeCount = combinedRanges.size();
    for (int i = 0; i < ranges.size(); i++) {
        Range currentRange = ranges[i];
        Range previouslyCombinedRange =
            combinedRanges.size() != 0 ? combinedRanges[combinedRanges.size() - 1] : Range(0, 0);

        // cStart < comEnd && cEnd > comEnd = change comEnd to cEnd
        if (currentRange.start < previouslyCombinedRange.end && currentRange.end > previouslyCombinedRange.end) {
            combinedRanges[combinedRanges.size() - 1].end = currentRange.end;
        }
        // cStart < comEnd && cEnd <= comEnd = do nothing
        else if (currentRange.start < previouslyCombinedRange.end && currentRange.end <= previouslyCombinedRange.end) {
            continue;
        }
        // cStart == comEnd = change comEnd to cEnd
        else if (currentRange.start == previouslyCombinedRange.end) {
            combinedRanges[combinedRanges.size() - 1].end = currentRange.end;
        }
        // cStart > comEnd = addToList
        else if (currentRange.start > previouslyCombinedRange.end) {
            combinedRanges.push_back(currentRange);
        }
        // else addToList
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
// 278239308095537
// 342433357244012 <- Correct

// 3-8 x
// 3-10 x
// 4-6 x
// 4-10 x
// 5-11 x
// 11-12 x
// 14-16 x
// 16-16 x
// 18-18

// 3-12, 14-16, 18-18
// cStart < comEnd && cEnd > comEnd = change comEnd
// cStart < comEnd && cEnd <= comEnd = do nothing
// cStart == comEnd = change comEnd to cEnd
// cStart > comEnd = addToList
// else addToList

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
