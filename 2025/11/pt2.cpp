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

// svr: aaa bbb
// aaa: fft
// fft: ccc
// bbb: tty
// tty: ccc
// ccc: ddd eee
// ddd: hub
// hub: fff
// eee: dac
// dac: fff
// fff: ggg hhh
// ggg: out
// hhh: out

int pathsToOut = 0;
mutex pathsToOutMutex;
unordered_map<string, int> nodeToCountMap;

// Probably can memoize if slow? Have it pass back vector of successful paths

void RecursiveFunc(unordered_map<string, vector<string>>& servers, string currentPath) {
    string latestNode = SplitString(currentPath, ",").back();

    vector<string> outNodes;  // Nodes that immeidately point to out
    for (const auto& pair : servers) {
        for (const auto& server : pair.second) {
            if (server == latestNode) {
                outNodes.push_back(pair.first);
            }
        }
    }

    for (const auto& server : outNodes) {
        if (currentPath.contains(server)) {
            continue;
        } else if (server == "svr") {
            if (currentPath.contains("fft") && currentPath.contains("dac")) {
                pathsToOut += 1;
            } else {
                // return currentPath + "," + server;
                return;
            }
        } else {
            RecursiveFunc(servers, currentPath + "," + server);
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

    vector<string> outNodes;  // Nodes that immeidately point to out
    for (const auto& pair : servers) {
        for (const auto& server : pair.second) {
            if (server == "out") {
                outNodes.push_back(pair.first);
            }
        }
    }

    for (const auto& server : outNodes) {
        RecursiveFunc(servers, server);
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
