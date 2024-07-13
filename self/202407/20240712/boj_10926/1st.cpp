#include <iostream>
#include <vector>
#include <string>

int main () {
    std::string line;
    std::getline(std::cin, line);
    
    std::cout << line + "??!" << std::endl;

    return 0;
}