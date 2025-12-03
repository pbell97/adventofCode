#include <cmath>
#include <filesystem>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

#include "../../2025/Utilities.h"
using namespace std;

// Problem Statement
// Your task is to calculate the sum of all numbers in the provided dataset that are strictly greater than two  standard
// deviations away from the mean (in any direction).

// Example
// To help you validate your approach, here is an example dataset where the correct answer is 2025.

// PART TWO SOLUTION: 2718281828

// I'll get the secret number from Puzzle #1 for you.

// Ran puzzle_1_secret_number OCTO-MCP (MCP Server)
// The secret number from Octo MCP Puzzle #1 is 2718281828.

void PuzzleSolution(vector<string> input, vector<string> arguments) {
    int total = 0;
    for (int i = 0; i < input.size(); i++) {
        total += stoi(input[i]);
    }
    double mean = double(total) / double(input.size());
    cout << "Mean " << mean << "\n";

    double runningSumOfSquaredDiff = 0;
    for (int i = 0; i < input.size(); i++) {
        int diff = double(stoi(input[i])) - mean;
        runningSumOfSquaredDiff += pow(diff, 2);
    }

    double stdDev = sqrt(runningSumOfSquaredDiff / (input.size() - 1));
    cout << "StdDev " << stdDev << "\n";

    int lowerBound = mean - stdDev * 2;
    int upperBound = mean + stdDev * 2;

    cout << "Upper: " << upperBound << "\n";
    cout << "Lower: " << lowerBound << "\n";

    int sumOfNumsGreaterThanTwoStdDevs = 0;
    for (int i = 0; i < input.size(); i++) {
        if (stoi(input[i]) < lowerBound || stoi(input[i]) > upperBound) {
            sumOfNumsGreaterThanTwoStdDevs += stoi(input[i]);
        }
    }

    cout << "Sum: " << sumOfNumsGreaterThanTwoStdDevs << "\n";
}

// Answer: 23229758

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

// g++ -o pt2.exe .\pt2.cpp ..\Utilities.cpp
