#include <iostream>
#include <sstream>
#include <vector>

int main() {
    std::string line;
    std::getline(std::cin, line);

    std::istringstream iss(line);
    std::vector<int> numbers;
    int number;
    while (iss >> number) {
        numbers.push_back(number);
    }

    int sum = 0;
    for (int num : numbers) {
        sum += num;
    }

    std::cout << sum << std::endl;

    return 0;
}