#include <filesystem>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

#include "../Utilities.h"
using namespace std;

vector<string> FilterEmptyFromVector(const vector<string>& input) {
    vector<string> newVec;
    for (const auto& item : input) {
        if (item != "") {
            newVec.push_back(item);
        }
    }
    return newVec;
}

// NOTE: Manually adjust input/col for sample vs real input. Sample has 3 rows of nums and real input has 4
void PuzzleSolution(vector<string> input, vector<string> arguments) {
    // Your puzzle solution here
    vector<string> firstNum = FilterEmptyFromVector(SplitString(input[0], " "));
    vector<string> secondNum = FilterEmptyFromVector(SplitString(input[1], " "));
    vector<string> thirdNum = FilterEmptyFromVector(SplitString(input[2], " "));
    vector<string> fourthNum = FilterEmptyFromVector(SplitString(input[3], " "));
    vector<string> symbol = FilterEmptyFromVector(SplitString(input[4], " "));

    long long runningTotal = 0;

    cout << firstNum.size() << endl;
    cout << secondNum.size() << endl;
    cout << thirdNum.size() << endl;
    cout << fourthNum.size() << endl;

    for (int i = 0; i < firstNum.size(); i++) {
        if (symbol[i] == "+") {
            runningTotal += (stoll(firstNum[i]) + stoll(secondNum[i]) + stoll(thirdNum[i]) + stoll(fourthNum[i]));
        } else if (symbol[i] == "*") {
            runningTotal += (stoll(firstNum[i]) * stoll(secondNum[i]) * stoll(thirdNum[i]) * stoll(fourthNum[i]));
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
