#include <filesystem>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

#include "./Utilities.h"

using namespace std;

// Creates empty sampleInput.txt
void CreateSampleFile(string rootPath) {
    string path = rootPath + "/" + "sampleInput.txt";
    ofstream newFile(path);
    newFile.close();
}

// Create empty input.txt
void CreateActualInputFile(string rootPath) {
    string path = rootPath + "/" + "input.txt";
    ofstream newFile(path);
    newFile.close();
}

void CreatePart1File(string rootPath) {
    string path = rootPath + "/" + "pt1.cpp";
    ofstream newFile(path);

    vector<string> sampleDay = ReadFile(rootPath + "/../sample/sampleDay.cpp");

    for (int i = 0; i < sampleDay.size(); i++) {
        newFile << sampleDay[i] << "\n";
    }

    newFile.close();
}

void CreatePart2File(string rootPath) {
    string path = rootPath + "/" + "pt2.cpp";
    ofstream newFile(path);

    vector<string> sampleDay = ReadFile(rootPath + "/../sample/sampleDay.cpp");

    for (int i = 0; i < sampleDay.size(); i++) {
        newFile << sampleDay[i] << "\n";
    }

    newFile.close();
}

int main(int argc, char* argv[]) {
    if (argc < 2) {
        cout << "Incorrect arguments. Please provide the number of the day/puzzle.\n";
        return 0;
    }

    string currentPath = filesystem::current_path();
    string newFolderPath = currentPath + "/" + argv[1];

    if (filesystem::exists(newFolderPath)) {
        cout << "Day " << argv[1] << " already exists at " << newFolderPath << "\n";
    } else {
        cout << "Creating Day " << argv[1] << " at " << newFolderPath << "\n";
        filesystem::create_directory(newFolderPath);
        CreateSampleFile(newFolderPath);
        CreateActualInputFile(newFolderPath);
        CreatePart1File(newFolderPath);
        CreatePart2File(newFolderPath);
    }

    return 0;
}

// g++ -std=c++17 -o setup ./aocsetup.cpp ./Utilities.cpp
// ./setup 1