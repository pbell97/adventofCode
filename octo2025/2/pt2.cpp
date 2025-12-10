#include <bitset>
#include <filesystem>
#include <fstream>
#include <functional>
#include <iostream>
#include <set>
#include <string>
#include <vector>

#include "../../2025/Utilities.h"
using namespace std;

struct iNum {
    uint8_t Num;
    string BinaryForm;
    int BitsAway;

    string ToBinary(uint8_t givenNum) { return bitset<8>(givenNum).to_string(); }

    iNum(uint8_t _num, int _bitsAway) : Num(_num), BitsAway(_bitsAway) { BinaryForm = ToBinary(_num); }
};

void PuzzleSolution(vector<string> input, vector<string> arguments) {
    vector<iNum> nums;
    for (const auto& line : input) {
        if (line.empty()) continue;  // Skip empty lines

        vector<string> split = SplitString(line, " -> ");
        try {
            nums.push_back(iNum((uint8_t)stoul(split[0]), stoi(split[1].substr(2))));
        } catch (const exception& e) {
            cout << "Error parsing line: " << line << endl;
            cout << "Split[0]: '" << split[0] << "', Split[1]: '" << split[1] << "'" << endl;
            throw;
        }
    }

    // For small inputs, try a more systematic approach
    set<uint8_t> all_candidates;

    // Generate candidates by trying all possible numbers at the exact required distance
    for (const auto& num : nums) {
        uint8_t original = num.Num;
        int required_flips = num.BitsAway;

        // Only do exhaustive search for reasonable flip counts
        if (required_flips <= 10) {
            // Generate all combinations of 'required_flips' bits from 8 bits
            function<void(uint8_t, int, int)> generate = [&](uint8_t current, int flips_left, int start_bit) {
                if (flips_left == 0) {
                    all_candidates.insert(current);
                    return;
                }
                if (start_bit + flips_left > 8) return;

                for (int bit = start_bit; bit <= 8 - flips_left; bit++) {
                    generate(current ^ (1u << bit), flips_left - 1, bit + 1);
                }
            };

            generate(original, required_flips, 0);
        } else {
            // For high flip counts, add the original and some random variations
            all_candidates.insert(original);
            for (int i = 0; i < 1000; i++) {
                uint8_t candidate = original;
                // Flip random bits
                for (int j = 0; j < required_flips; j++) {
                    int random_bit = rand() % 8;
                    candidate ^= (1u << random_bit);
                }
                all_candidates.insert(candidate);
            }
        }
    }

    cout << "Testing " << all_candidates.size() << " candidates..." << endl;

    uint8_t best_answer = 0;
    int best_error = INT_MAX;

    for (uint8_t candidate : all_candidates) {
        int total_error = 0;

        for (const auto& num : nums) {
            int hamming_distance = __builtin_popcount(candidate ^ num.Num);
            total_error += abs(hamming_distance - num.BitsAway);
        }

        if (total_error < best_error) {
            best_error = total_error;
            best_answer = candidate;

            if (total_error == 0) {
                cout << "Found exact solution: " << candidate << endl;
                break;
            }
        }
    }

    uint8_t answer = best_answer;
    cout << "Best error achieved: " << best_error << endl;
    cout << "Answer: " << (int)answer << endl;
    cout << "Binary: " << bitset<8>(answer) << endl;

    // Verify the solution by checking Hamming distances
    cout << "\nVerification:" << endl;
    for (const auto& num : nums) {
        int hamming_distance = __builtin_popcount(answer ^ num.Num);
        cout << "Original: " << (int)num.Num << ", Expected: " << num.BitsAway << ", Actual: " << hamming_distance;
        if (hamming_distance == num.BitsAway)
            cout << " ✓";
        else
            cout << " ✗";
        cout << endl;
    }
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
// 287468019