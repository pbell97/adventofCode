#include <algorithm>
#include <filesystem>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

#include "../Utilities.h"
using namespace std;

// Idea: Treat everything as bits, bitwise AND/OR the button pushes until you get the desired result

struct Machine {
    uint16_t DesiredBitOutCome;
    vector<vector<uint16_t>> Buttons;
    vector<uint16_t> ButtonActions;
    vector<uint16_t> Joltages;

    Machine(uint16_t desiredBitOutCome, vector<vector<uint16_t>> buttons, vector<uint16_t> buttonActions,
            vector<uint16_t> joltages)
        : DesiredBitOutCome(desiredBitOutCome), Buttons(buttons), ButtonActions(buttonActions), Joltages(joltages) {}
};

vector<Machine> ParseMachinesFromInput(vector<string> input) {
    vector<Machine> machines;

    for (const auto& line : input) {
        vector<string> sections = SplitString(line, " ");
        string state = sections[0].substr(1, sections[0].size() - 2);
        std::replace(state.begin(), state.end(), '.', '0');
        std::replace(state.begin(), state.end(), '#', '1');
        unsigned int desiredOutcome = std::stoul(state, nullptr, 2);
        vector<vector<uint16_t>> Buttons;
        vector<uint16_t> ButtonActions;
        vector<uint16_t> Joltages;
        int offset = 16 - state.size();

        for (int i = 1; i < sections.size() - 1; i++) {
            vector<string> numStrings = SplitString(sections[i].substr(1, sections[i].size() - 2), ",");
            vector<uint16_t> nums;
            string buttonPress = "0000000000000000";
            for (const auto& stringNum : numStrings) {
                int spot = stoi(stringNum) + offset;
                buttonPress[spot] = '1';
                nums.push_back(stoul(stringNum));
            }
            uint16_t buttonPressInt = std::stoul(buttonPress, nullptr, 2);
            ButtonActions.push_back(buttonPressInt);
            Buttons.push_back(nums);
        }

        vector<string> numStrings =
            SplitString(sections[sections.size() - 1].substr(1, sections[sections.size() - 1].size() - 2), ",");
        for (const auto& stringNum : numStrings) {
            Joltages.push_back(stoul(stringNum));
        }
        machines.push_back(Machine(desiredOutcome, Buttons, ButtonActions, Joltages));
    }

    return machines;
}

void PrintMachines(vector<Machine> machines) {
    for (const auto& machine : machines) {
        // Convert desiredBitOutcome to binary string
        string desiredStr = "";
        for (int i = 7; i >= 0; i--) {
            desiredStr += ((machine.DesiredBitOutCome >> i) & 1) ? '1' : '0';
        }
        cout << "Desired: " << desiredStr << endl;

        // Print buttons with their actions
        for (size_t i = 0; i < machine.Buttons.size(); i++) {
            cout << "Button [";
            for (size_t j = 0; j < machine.Buttons[i].size(); j++) {
                cout << (int)machine.Buttons[i][j];
                if (j < machine.Buttons[i].size() - 1) cout << ",";
            }
            cout << "] (";

            // Convert buttonAction to binary string
            for (int bit = 7; bit >= 0; bit--) {
                cout << ((machine.ButtonActions[i] >> bit) & 1);
            }
            cout << ")" << endl;
        }
        cout << endl;
    }
}

void generatePermutations(const vector<uint16_t>& nums, int maxLength, vector<uint16_t>& current,
                          vector<vector<uint16_t>>& result) {
    // Add current permutation if it's not empty and within max length
    if (!current.empty() && current.size() <= maxLength) {
        result.push_back(current);
    }

    // Stop if we've reached max length
    if (current.size() == maxLength) {
        return;
    }

    for (int num : nums) {
        current.push_back(num);
        generatePermutations(nums, maxLength, current, result);
        current.pop_back();
    }
}

vector<vector<uint16_t>> getAllPermutations(const vector<uint16_t>& nums, int maxLength) {
    vector<vector<uint16_t>> result;
    vector<uint16_t> current;
    generatePermutations(nums, maxLength, current, result);
    return result;
}

void PuzzleSolution(vector<string> input, vector<string> arguments) {
    vector<Machine> machines = ParseMachinesFromInput(input);
    // PrintMachines(machines);
    long buttonPresses = 0;

    for (const auto& machine : machines) {
        vector<vector<uint16_t>> perms = getAllPermutations(machine.ButtonActions, 7);
        sort(perms.begin(), perms.end(), [](const auto& a, const auto& b) { return a.size() < b.size(); });
        int buttonPushes = 0;
        for (const auto& perm : perms) {
            uint16_t currentNum = 0;
            for (const auto& num : perm) {
                currentNum = currentNum ^ num;
            }
            if (currentNum == machine.DesiredBitOutCome) {
                cout << "Found match! Size: " << perm.size() << " Perm: [";
                for (size_t i = 0; i < perm.size(); i++) {
                    cout << (int)perm[i];
                    if (i < perm.size() - 1) cout << ",";
                }
                cout << "] " << (int)currentNum << " == " << (int)machine.DesiredBitOutCome << endl;
                buttonPresses += perm.size();
                break;
            }
        }
        if (buttonPresses == 0) {
            cout << "NEVER FOUND A MATCH FOR " << machine.DesiredBitOutCome << endl;
        }
    }

    cout << "Total button presses: " << buttonPresses << endl;
}

// 483 To Low

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
