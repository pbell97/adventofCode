#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Person {
   private:
    string name;
    int age;

   public:
    // Constructor
    Person(string n, int a) : name(n), age(a) {}

    // Getter methods
    string getName() const { return name; }
    int getAge() const { return age; }

    // Method
    void introduce() const { cout << "Hi, I'm " << name << " and I'm " << age << " years old." << endl; }
};

int main() {
    // Basic output
    cout << "Welcome to C++!" << endl;

    // Variables
    int number = 42;
    string message = "Hello from C++";

    cout << message << " Number: " << number << endl;

    // Collections
    vector<int> numbers = {1, 2, 3, 4, 5};
    cout << "Numbers: ";
    for (int num : numbers) {  // Range-based for loop (like foreach)
        cout << num << " ";
    }
    cout << endl;

    // Objects
    Person person("Alice", 30);
    person.introduce();

    // Pointers (basic example)
    int* ptr = &number;
    cout << "Value through pointer: " << *ptr << endl;

    return 0;
}

// Compile and run:
// g++ -o HelloWorld HelloWorld.cpp

// # Compile a single file
// g++ -o myprogram main.cpp

// # Compile multiple files
// g++ -o myprogram main.cpp MyClass.cpp

// # With debugging info
// g++ -g -o myprogram main.cpp

// # With optimizations

// g++ -O2 -o myprogram main.cpp

// Refresher: https://www.mauriciopoppe.com/notes/computer-science/programming-languages/cpp-refresher/
// Template setup: https://github.com/Bogdanp/awesome-advent-of-code?tab=readme-ov-file#project-templates
