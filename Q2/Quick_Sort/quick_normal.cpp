#include <iostream>
#include <vector>
#include <fstream>
#include <cstdlib>
#include <ctime>
#include <chrono>

// Metrics
int comparisons = 0;
int swaps = 0;
int basic_operations = 0;

int partition(std::vector<int>& array, int p, int r) {
    // Choose a random pivot index
    int pivot_index = p + rand() % (r - p + 1);
    
    // Swap pivot with the last element
    std::swap(array[pivot_index], array[r]);
    swaps++;

    int pivot = array[r];
    int i = p - 1;

    for (int j = p; j < r; ++j) {
        comparisons++;  // Comparison in the loop
        if (array[j] <= pivot) {
            ++i;
            std::swap(array[i], array[j]);
            swaps++;
        }
    }

    std::swap(array[i + 1], array[r]);
    swaps++;
    return i + 1;
}

void quick_sort(std::vector<int>& array, int p, int r) {
    if (p < r) {
        int q = partition(array, p, r);
        quick_sort(array, p, q - 1);
        quick_sort(array, q + 1, r);
    }
}

void evaluate_quick_sort(const std::string& filename) {
    std::vector<int> array;
    std::ifstream infile(filename);

    if (!infile) {
        std::cerr << "Error opening file: " << filename << std::endl;
        return;
    }

    int number;
    while (infile >> number) {
        array.push_back(number);
    }

    infile.close();

    // Reset metrics
    comparisons = 0;
    swaps = 0;
    basic_operations = 0;

    // Measure execution time
    auto start_time = std::chrono::high_resolution_clock::now();

    quick_sort(array, 0, array.size() - 1);

    auto end_time = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double, std::milli> execution_time = end_time - start_time;

    std::cout << "Quick Sort - Test case size: " << array.size() << std::endl;
    std::cout << "Comparisons: " << comparisons << std::endl;
    std::cout << "Swaps: " << swaps << std::endl;
    std::cout << "Basic operations: " << basic_operations << std::endl;
    std::cout << "Execution time: " << execution_time.count() << " ms" << std::endl;
    std::cout << "Memory usage: Not measured in this implementation" << std::endl; // Memory usage not directly measured in this example
    std::cout << "----------------------------------------" << std::endl;
}

int main() {
    // Seed the random number generator
    std::srand(static_cast<unsigned>(std::time(0)));

    // Specify the input file
    std::string filename = "D:\\DAA Assignment\\Q2\\q2_tc.txt"; // Use double backslashes for Windows paths
    evaluate_quick_sort(filename);

    return 0;
}
