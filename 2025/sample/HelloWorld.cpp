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

int* createNumber() {
    int num = 42;  // ❌ Dies when function ends
    return &num;   // ❌ Dangling pointer!

    int* num = new int(42);  // ✅ Lives on heap
    return num;              // ✅ Valid (but remember to delete!)

    // Large array on stack - might cause stack overflow
    int largeArray[1000000];  // ❌ Stack space limited (~1-8MB)

    // Large array on heap - uses system memory
    int* largeArray = new int[1000000];  // ✅ Heap space much larger

    void processData(int size) {
        int arr[size];  // ❌ Not standard C++

        int* arr = new int[size];  // ✅ Dynamic allocation
        // ... use arr
        delete[] arr;
    }

    // Dynamic memory allocation (that isn't a vector) can't be done without pointers because
    // something like int arr[numberHere] needs to know numberHere at compileTime. So instead
    // provision via pointers. It also puts it on heap insted of stack
}

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

// vscode: $env:PATH = "C:\msys64\ucrt64\bin;$env:PATH"; g++ --version

// Refresher: https://www.mauriciopoppe.com/notes/computer-science/programming-languages/cpp-refresher/
// Template setup: https://github.com/Bogdanp/awesome-advent-of-code?tab=readme-ov-file#project-templates
