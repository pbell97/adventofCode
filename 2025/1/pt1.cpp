#include <filesystem>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

#include "../Utilities.h"
using namespace std;

void PuzzleSolution(vector<string> input, vector<string> arguments) {
    int currentPosition = 50;
    int timesAtZero = 0;

    cout << "Size: " << input.size() << "\n";

    for (int i = 0; i < input.size(); i++) {
        string line = input[i];
        char direction = line.at(0);
        int moves = stoi(line.substr(1));
        int prev = currentPosition;
        if (direction == 'L') {
            cout << "subtracting " << moves << " from " << currentPosition << "\n";
            currentPosition -= moves;
        } else {
            cout << "adding " << moves << " to " << currentPosition << "\n";
            currentPosition += moves;
        }

        // Ex. -5 == 95
        if (currentPosition < 0) {
            int remainder = currentPosition % 100;
            currentPosition = 100 + remainder;
        }

        // 105 == 5?
        if (currentPosition > 99) {
            int remainder = currentPosition % 100;
            currentPosition = remainder;
        }

        if (currentPosition == 0) {
            timesAtZero += 1;
        }

        cout << "Moving " << direction << " " << moves << " times. Was " << prev << " and now " << currentPosition
             << "\n";
    }

    cout << "Times finished at 0: " << timesAtZero << "\n";
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