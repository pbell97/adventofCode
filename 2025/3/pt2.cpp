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

// 898181911112111
string RecursiveFunction(string num, int distanceOut) {
    // 15 - (12 - 1) = 4? Or 3?
    int subStLength = num.size() - (distanceOut - 1);
    // 898      181911112111
    string subStr = num.substr(0, subStLength);
    // 9
    string firstDigit = GetLargestNumFromString(subStr);
    // 1
    int firstDigitIndex = num.find(firstDigit);

    // 89 8181911112111
    string secondHalf = "";
    if (distanceOut != 1) {
        string subStr2 = num.substr(firstDigitIndex + 1, num.size());
        secondHalf = RecursiveFunction(subStr2, distanceOut - 1);
    }

    return firstDigit + secondHalf;
}

void PuzzleSolution(vector<string> input, vector<string> arguments) {
    // Your puzzle solution here
    long long total = 0;

    for (int i = 0; i < input.size(); i++) {
        string num = input[i];
        cout << "On: " << num << endl;
        string result = RecursiveFunction(num, 12);
        cout << "\tResult: " << result << endl;
        long long converted = stoll(result);
        total += converted;
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
