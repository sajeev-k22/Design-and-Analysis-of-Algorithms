#include <iostream>
#include <vector>
#include <fstream>
#include <chrono>
#include <algorithm>
#include <random>

// Metrics
int comparisons = 0;
int swaps = 0;
int basic_operations = 0;

// Function to heapify a subtree rooted at index i
void heapify(std::vector<int>& arr, int n, int i) {
    int largest = i; // Initialize largest as root
    int left = 2 * i + 1; // Left child
    int right = 2 * i + 2; // Right child

    // If left child is larger than root
    if (left < n) {
        comparisons++; // Comparison for left child
        if (arr[left] > arr[largest]) {
            largest = left;
        }
    }

    // If right child is larger than the largest so far
    if (right < n) {
        comparisons++; // Comparison for right child
        if (arr[right] > arr[largest]) {
            largest = right;
        }
    }

    // If largest is not root
    if (largest != i) {
        // Swap root with the largest element
        std::swap(arr[i], arr[largest]);
        swaps++; // Increment swap count

        // Recursively heapify the affected subtree
        heapify(arr, n, largest);
    }
}

// Function to perform heap sort on the input array
void heapSort(std::vector<int>& arr) {
    int n = arr.size();

    // Build a maxheap (rearrange array)
    for (int i = n / 2 - 1; i >= 0; --i) {
        heapify(arr, n, i);
    }

    // Extract elements from heap one by one
    for (int i = n - 1; i > 0; --i) {
        // Move current root to the end
        std::swap(arr[0], arr[i]);
        swaps++; // Increment swap count

        // Call heapify on the reduced heap
        heapify(arr, i, 0);
    }
}

// Function to evaluate heap sort with a test case from file
void evaluateHeapSort(const std::vector<int>& array) {
    // Copy the array to avoid modifying the original input
    std::vector<int> sortedArray = array;

    // Reset metrics
    comparisons = 0;
    swaps = 0;
    basic_operations = 0;

    // Measure execution time
    auto start_time = std::chrono::high_resolution_clock::now();

    heapSort(sortedArray);

    auto end_time = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double, std::milli> execution_time = end_time - start_time;

    // Memory usage is approximated since C++ does not directly measure it like Python's tracemalloc
    size_t memory_usage = sizeof(int) * array.size();

    std::cout << "Heap Sort - Test case size: " << array.size() << std::endl;
    std::cout << "Comparisons: " << comparisons << std::endl;
    std::cout << "Swaps: " << swaps << std::endl;
    std::cout << "Basic operations: " << basic_operations << std::endl; // Placeholder for future operations
    std::cout << "Execution time: " << execution_time.count() << " ms" << std::endl;
    std::cout << "Memory usage: " << memory_usage / 1024.0 << " KB" << std::endl;
    std::cout << "----------------------------------------" << std::endl;
}

// Function to read array from file
std::vector<int> readArrayFromFile(const std::string& filename) {
    std::ifstream file(filename);
    std::vector<int> array;
    int value;
    if (file.is_open()) {
        while (file >> value) {
            array.push_back(value);
        }
        file.close();
    } else {
        std::cerr << "Error opening file: " << filename << std::endl;
    }
    return array;
}

// Main method
int main() {
    std::string filename = "D:\\DAA Assignment\\Q2\\q2_tc.txt"; // Change this to your input file name

    // Read array from file
    std::vector<int> array = readArrayFromFile(filename);

    // Evaluate heap sort with the read array
    evaluateHeapSort(array);

    return 0;
}
