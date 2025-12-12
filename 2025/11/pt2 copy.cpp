#include <filesystem>
#include <fstream>
#include <iostream>
#include <mutex>
#include <string>
#include <thread>
#include <unordered_map>
#include <vector>

#include "../Utilities.h"
using namespace std;

// aaa: you hhh
// you: bbb ccc
// bbb: ddd eee
// ccc: ddd eee fff
// ddd: ggg
// eee: out
// fff: out
// ggg: out
// hhh: ccc fff iii
// iii: out

int pathsToOut = 0;
mutex pathsToOutMutex;

// Probably can memoize if slow? Have it pass back vector of successful paths

string RecursiveFunc(unordered_map<string, vector<string>>& servers, string currentPath) {
    string latestNode = SplitString(currentPath, ",").back();
    for (const auto& server : servers[latestNode]) {
        if (currentPath.contains(server)) {
            continue;
        } else if (server == "out") {
            if (currentPath.contains("fft") && currentPath.contains("dac")) {
                lock_guard<mutex> lock(pathsToOutMutex);
                pathsToOut += 1;
            } else {
                return currentPath + "," + server;
            }
        } else {
            string returnedString = RecursiveFunc(servers, currentPath + "," + server);
                }
    }
}

void PuzzleSolution(vector<string> input, vector<string> arguments) {
    // Parse input
    unordered_map<string, vector<string>> servers;
    for (const auto& line : input) {
        vector<string> stuff = SplitString(line, ": ");
        servers[stuff[0]] = SplitString(stuff[1].substr(1), " ");
    }

    vector<string> startingNodes = servers["svr"];
    vector<thread> threads;
    for (int i = 0; i < startingNodes.size(); i++) {
        threads.emplace_back([&servers, &startingNodes, i]() { RecursiveFunc(servers, "svr," + startingNodes[i]); });
    }
    for (auto& t : threads) {
        t.join();
    }

    cout << "Paths to out: " << pathsToOut << endl;
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
