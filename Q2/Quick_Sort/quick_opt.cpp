#include <iostream>
#include <vector>
#include <fstream>
#include <cstdlib>
#include <ctime>
#include <chrono>
#include <algorithm>

// Metrics
int comparisons = 0;
int swaps = 0;
int basic_operations = 0;

int median_of_three(const std::vector<int>& arr, int low, int high) {
    int mid = (low + high) / 2;
    int a = arr[low], b = arr[mid], c = arr[high];
    
    if (a > b) {
        if (a < c) return a;
        else if (b > c) return b;
        else return c;
    } else {
        if (a > c) return a;
        else if (b < c) return b;
        else return c;
    }
}

int partition(std::vector<int>& array, int low, int high) {
    int pivot = median_of_three(array, low, high);
    int i = low - 1;

    for (int j = low; j < high; ++j) {
        ++comparisons;
        if (array[j] < pivot) {
            ++i;
            std::swap(array[i], array[j]);
            ++swaps;
        }
    }

    std::swap(array[i + 1], array[high]);
    ++swaps;
    return i + 1;
}

void quick_sort(std::vector<int>& array, int low, int high) {
    while (low < high) {
        int pi = partition(array, low, high);
        if (pi - low < high - pi) {
            quick_sort(array, low, pi - 1);
            low = pi + 1;
        } else {
            quick_sort(array, pi + 1, high);
            high = pi - 1;
        }
    }
}

void evaluate_quick_sort(const std::vector<int>& array, size_t test_case_size) {
    std::vector<int> array_copy = array; // Create a copy to sort
    comparisons = swaps = basic_operations = 0;

    // Measure execution time
    auto start_time = std::chrono::high_resolution_clock::now();

    quick_sort(array_copy, 0, array_copy.size() - 1);

    auto end_time = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double, std::milli> execution_time = end_time - start_time;

    std::cout << "Quick Sort - Test case size: " << test_case_size << std::endl;
    std::cout << "Comparisons: " << comparisons << std::endl;
    std::cout << "Swaps: " << swaps << std::endl;
    std::cout << "Basic operations: " << basic_operations << std::endl;
    std::cout << "Execution time: " << execution_time.count() << " ms" << std::endl;
    std::cout << "Memory usage: Not measured in this implementation" << std::endl; // Memory usage not directly measured in this example
    std::cout << "----------------------------------------" << std::endl;
}

std::vector<int> read_array_from_file(const std::string& filename) {
    std::ifstream file(filename);
    if (!file) {
        std::cerr << "Error opening file: " << filename << std::endl;
        return {};
    }

    std::vector<int> array;
    int number;
    while (file >> number) {
        array.push_back(number);
    }

    return array;
}

int main() {
    // Seed the random number generator
    std::srand(static_cast<unsigned>(std::time(0)));

    // Specify the input file
    std::string filename = "D:\\DAA Assignment\\Q2\\q2_tc.txt"; // Use double backslashes for Windows paths

    // Read the array from the file
    std::vector<int> array = read_array_from_file(filename);
    
    // Evaluate quick sort
    evaluate_quick_sort(array, array.size());

    return 0;
}
