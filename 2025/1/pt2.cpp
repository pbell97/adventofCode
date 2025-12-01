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

    cout << "Starting at 50\n";

    for (int i = 0; i < input.size(); i++) {
        string line = input[i];
        char direction = line.at(0);
        int moves = stoi(line.substr(1));
        int prev = currentPosition;
        int startedAtZeroOffset = currentPosition == 0 ? -1 : 0;
        if (direction == 'L') {
            currentPosition -= moves;
        } else {
            currentPosition += moves;
        }

        string extraLog = "";

        if (currentPosition < 0) {
            int timesPassZero = abs(currentPosition / 100) + 1 + startedAtZeroOffset;
            timesAtZero += timesPassZero;
            extraLog = " - Less than zero, adding " + to_string(timesPassZero) + " \n";

            int remainder = currentPosition % 100;
            if (remainder == 0) {
                remainder = -100;  // For if its eg -100, remainder would be 0 when the currentPosition needs to be set
                                   // to 0 instead of 100
            }
            currentPosition = 100 + remainder;
        } else if (currentPosition > 99) {
            int timesPassZero = abs(currentPosition / 100);
            timesAtZero += timesPassZero;
            extraLog = " - Greater than 99, adding " + to_string(timesPassZero) + " \n";

            int remainder = currentPosition % 100;
            currentPosition = remainder;
        } else if (currentPosition == 0) {
            timesAtZero += 1;
            extraLog = " - At position 0, adding 1\n";
        }

        cout << "Moving " << direction << " " << moves << " times. Was " << prev << " and now " << currentPosition
             << "\n";
        if (extraLog != "") {
            cout << extraLog;
        }
    }

    // 6489 < answer < 6589
    // 6420
    // 6530 -> Correct!

    cout << "Times crossed 0: " << timesAtZero << "\n";
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

// Moving R 529 times. Was 71 and now 0
//   - Greater than 99, adding 6

// 71(529)->0(500)->0(400)->0(300)->0(200)->0(100)->0(0)

// What about starting with R50 and the R100...