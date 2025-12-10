#include <algorithm>
#include <bitset>
#include <chrono>
#include <filesystem>
#include <fstream>
#include <functional>
#include <future>
#include <iostream>
#include <mutex>
#include <set>
#include <string>
#include <thread>
#include <vector>

#include "../../2025/Utilities.h"
using namespace std;

struct iNum {
    uint32_t Num;
    string BinaryForm;
    int BitsAway;

    string ToBinary(uint32_t givenNum) { return bitset<32>(givenNum).to_string(); }

    iNum(uint32_t _num, int _bitsAway) : Num(_num), BitsAway(_bitsAway) { BinaryForm = ToBinary(_num); }
};

// Thread-safe permutation generation function
set<uint32_t> generatePermutationsThreaded(uint32_t original, int required_flips, int num_threads = 4) {
    if (required_flips == 0) {
        return {original};
    }

    set<uint32_t> all_permutations;
    mutex result_mutex;

    // Calculate total combinations to distribute work
    auto factorial = [](int n) -> long long {
        long long result = 1;
        for (int i = 2; i <= n; i++) result *= i;
        return result;
    };

    auto combinations = [&factorial](int n, int k) -> long long {
        if (k > n || k < 0) return 0;
        return factorial(n) / (factorial(k) * factorial(n - k));
    };

    long long total_combinations = combinations(32, required_flips);

    // If too few combinations, just use single thread
    if (total_combinations < 1000 || num_threads == 1) {
        function<void(uint32_t, int, int)> generate = [&](uint32_t current, int flips_left, int start_bit) {
            if (flips_left == 0) {
                all_permutations.insert(current);
                return;
            }
            if (start_bit + flips_left > 32) return;

            for (int bit = start_bit; bit <= 32 - flips_left; bit++) {
                generate(current ^ (1u << bit), flips_left - 1, bit + 1);
            }
        };
        generate(original, required_flips, 0);
        return all_permutations;
    }

    // Divide work among threads by distributing starting bit ranges
    vector<future<set<uint32_t>>> futures;
    int bits_per_thread = max(1, (32 - required_flips + 1) / num_threads);

    for (int thread_id = 0; thread_id < num_threads; thread_id++) {
        int start_bit = thread_id * bits_per_thread;
        int end_bit = min(32 - required_flips + 1, (thread_id + 1) * bits_per_thread);

        if (start_bit >= end_bit) break;

        futures.push_back(async(launch::async, [=]() -> set<uint32_t> {
            set<uint32_t> thread_results;

            function<void(uint32_t, int, int)> generate = [&](uint32_t current, int flips_left, int start) {
                if (flips_left == 0) {
                    thread_results.insert(current);
                    return;
                }
                if (start + flips_left > 32) return;

                for (int bit = start; bit <= 32 - flips_left; bit++) {
                    generate(current ^ (1u << bit), flips_left - 1, bit + 1);
                }
            };

            // Generate permutations starting with each bit in this thread's range
            for (int first_bit = start_bit; first_bit < end_bit; first_bit++) {
                if (required_flips == 1) {
                    thread_results.insert(original ^ (1u << first_bit));
                } else {
                    generate(original ^ (1u << first_bit), required_flips - 1, first_bit + 1);
                }
            }

            return thread_results;
        }));
    }

    // Collect results from all threads
    for (auto& future : futures) {
        set<uint32_t> thread_result = future.get();
        all_permutations.insert(thread_result.begin(), thread_result.end());
    }

    return all_permutations;
}

// Function to check if a candidate is compatible with a number (has the correct Hamming distance)
bool isCompatible(uint32_t candidate, uint32_t target_num, int required_flips) {
    return __builtin_popcount(candidate ^ target_num) == required_flips;
}

void PuzzleSolution(vector<string> input, vector<string> arguments) {
    vector<iNum> nums;
    for (const auto& line : input) {
        if (line.empty()) continue;  // Skip empty lines

        vector<string> split = SplitString(line, " -> ");
        if (split.size() != 2) {
            cout << "Error: Invalid line format: " << line << endl;
            continue;
        }

        try {
            // Remove any leading/trailing whitespace and "-> " from split[1]
            string number_str = split[1];
            // If split[1] starts with "-> ", remove it
            if (number_str.substr(0, 3) == "-> ") {
                number_str = number_str.substr(3);
            }
            nums.push_back(iNum(stoul(split[0]), stoi(number_str)));
        } catch (const exception& e) {
            cout << "Error parsing line: " << line << endl;
            cout << "Split[0]: '" << split[0] << "', Split[1]: '" << split[1] << "'" << endl;
            throw;
        }
    }

    // Sort numbers by their BitsAway (ascending order of permutation counts)
    sort(nums.begin(), nums.end(), [](const iNum& a, const iNum& b) { return a.BitsAway < b.BitsAway; });

    cout << "Processing numbers in order of permutation count:" << endl;
    for (const auto& num : nums) {
        cout << "Number " << num.Num << " requires " << num.BitsAway << " bit flips" << endl;
    }
    cout << endl;

    set<uint32_t> valid_candidates;

    // Process first number - generate all its permutations (this is the only time we generate full permutations)
    const auto& first_num = nums[0];
    cout << "Processing first number: " << first_num.Num << " (" << first_num.BitsAway << " flips)" << endl;

    auto start_time = chrono::high_resolution_clock::now();
    valid_candidates = generatePermutationsThreaded(first_num.Num, first_num.BitsAway);
    auto end_time = chrono::high_resolution_clock::now();
    auto duration = chrono::duration_cast<chrono::milliseconds>(end_time - start_time);

    cout << "Initial candidates: " << valid_candidates.size() << " (generated in " << duration.count() << "ms)" << endl;

    // For each subsequent number, filter existing candidates instead of generating new permutations
    for (int i = 1; i < nums.size(); i++) {
        const auto& current_num = nums[i];
        cout << "\nProcessing number " << (i + 1) << ": " << current_num.Num << " (" << current_num.BitsAway
             << " flips)" << endl;

        auto filter_start = chrono::high_resolution_clock::now();

        // Filter existing candidates: keep only those that are compatible with current number
        set<uint32_t> filtered_candidates;
        for (uint32_t candidate : valid_candidates) {
            if (isCompatible(candidate, current_num.Num, current_num.BitsAway)) {
                filtered_candidates.insert(candidate);
            }
        }

        auto filter_end = chrono::high_resolution_clock::now();
        auto filter_duration = chrono::duration_cast<chrono::milliseconds>(filter_end - filter_start);

        cout << "Filtered " << valid_candidates.size() << " candidates down to " << filtered_candidates.size()
             << " (in " << filter_duration.count() << "ms)" << endl;

        valid_candidates = filtered_candidates;

        // If we're down to one candidate, we found the answer
        if (valid_candidates.size() == 1) {
            cout << "Found unique answer!" << endl;
            break;
        } else if (valid_candidates.empty()) {
            cout << "No valid candidates found! Something went wrong." << endl;
            return;
        }
    }

    if (valid_candidates.size() == 1) {
        uint32_t answer = *valid_candidates.begin();
        cout << "\nAnswer: " << answer << endl;
        cout << "Binary: " << bitset<32>(answer) << endl;

        // Verify the solution by checking Hamming distances
        cout << "\nVerification:" << endl;
        bool all_correct = true;
        for (const auto& num : nums) {
            int hamming_distance = __builtin_popcount(answer ^ num.Num);
            cout << "Number " << num.Num << " - Expected: " << num.BitsAway << ", Actual: " << hamming_distance;
            if (hamming_distance == num.BitsAway) {
                cout << " ✓";
            } else {
                cout << " ✗";
                all_correct = false;
            }
            cout << endl;
        }

        if (all_correct) {
            cout << "\nAll constraints satisfied! Answer is correct." << endl;
        } else {
            cout << "\nSome constraints not satisfied. Answer may be incorrect." << endl;
        }
    } else {
        cout << "\nMultiple candidates remain: " << valid_candidates.size() << endl;
        cout << "Candidates: ";
        for (uint32_t candidate : valid_candidates) {
            cout << candidate << " ";
        }
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

// g++ -o pt2.exe .\pt2.cpp ..\Utilities.cpp
// g++ -std=c++23 -o pt2 ./pt2.cpp ../../2025/Utilities.cpp