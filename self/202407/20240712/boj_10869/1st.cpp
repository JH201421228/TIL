#include <iostream>
#include <sstream>
#include <vector>

int main () {
    std::string line;
    std::getline(std::cin, line);

    std::istringstream iss(line);
    std::vector<int> numbers;

    int number;
    while (iss >> number) {
        numbers.emplace_back(number);
    }

    std::cout << numbers[0]+numbers[1] << std::endl;
    std::cout << numbers[0]-numbers[1] << std::endl;
    std::cout << numbers[0]*numbers[1] << std::endl;
    std::cout << numbers[0]/numbers[1] << std::endl;
    std::cout << numbers[0]%numbers[1] << std::endl;

    return 0;
}