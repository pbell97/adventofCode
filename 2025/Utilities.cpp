#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

// Returns vector of each line
vector<string> ReadFile(string filePath) {
    vector<string> lines = vector<string>();

    ifstream inFile;
    inFile.open(filePath);

    string currentLine;
    while (getline(inFile, currentLine)) {
        lines.push_back(currentLine);
    };

    inFile.close();
    return lines;
}

vector<string> SplitString(string inputString, string delimiter) {
    size_t index = inputString.find(delimiter);

    if (index == string::npos) {
        return {inputString};
    }

    vector<string> outVector;
    string remainingString = inputString;

    while (index != string::npos) {
        outVector.push_back(remainingString.substr(0, index));
        remainingString = remainingString.substr(index + 1, remainingString.length() - 1);
        index = remainingString.find(delimiter);
    }
    outVector.push_back(remainingString);
    return outVector;
}

int main() {
    // Read a file into a vector of strings per line
    const string filePath = "D:/repos/Testbed/adventofCode/2025/sample.txt";
    vector<string> lines = ReadFile(filePath);
    for (int i = 0; i < lines.size(); i++) {
        string line = lines.at(i);
    }

    // Split a string
    string sampleString = ",Abc,,123,One,Two,Three";
    vector<string> split = SplitString(sampleString, "-");
    cout << "size of vector split " << split.size() << "\n";
    for (int i = 0; i < split.size(); i++) {
        cout << split.at(i) + " \n";
    }

    return 0;
}