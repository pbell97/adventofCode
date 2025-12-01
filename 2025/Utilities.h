#ifndef UTILITIES_H
#define UTILITIES_H

#include <string>
#include <vector>

// Function declarations
std::vector<std::string> ReadFile(std::string filePath);
std::vector<std::string> SplitString(std::string inputString, std::string delimiter);
void WriteToFile(std::vector<std::string> inputText, std::string filePath);

#endif  // UTILITIES_H