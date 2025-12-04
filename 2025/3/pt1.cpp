#include <filesystem>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

#include "../Utilities.h"
using namespace std;

string GetLargestNumFromString(string input) {
    // cout << "Given input: " << input << endl;
    vector<int> digits;
    for (int i = 0; i < input.size(); i++) {
        digits.push_back(input.at(i) - '0');
        // cout << "Char: " << input.at(i) - '0' << endl;
    }
    int largest = 0;
    for (int i = 0; i < digits.size(); i++) {
        if (digits[i] > largest) {
            largest = digits[i];
        }
    }

    return to_string(largest);
}

void PuzzleSolution(vector<string> input, vector<string> arguments) {
    // Your puzzle solution here
    long total = 0;

    for (int i = 0; i < input.size(); i++) {
        cout << "On: " << input[i] << endl;
        // Get largest number from the subset of 0 - n-1 numbers
        string firstDigit = GetLargestNumFromString(input[i].substr(0, input[i].size() - 1));
        int firstDigitIndex = input[i].find(firstDigit);
        // Then get the largest number from result^Index - end numbers
        string secondDigit = GetLargestNumFromString(input[i].substr(firstDigitIndex + 1, input[i].size()));
        int largest = stoi(firstDigit + secondDigit);
        cout << "Largest number combo: " << largest << endl;
        total += largest;
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
