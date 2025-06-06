#include <iostream>
#include <vector>
#include <fstream>
#include <chrono>
#include <algorithm>

// Metrics
int comparisons = 0;
int swaps = 0;
int basic_operations = 0;

// Function to heapify a subtree rooted at index i
void heapify(std::vector<int>& arr, int n, int i) {
    int largest = i; // Initialize largest as root
    int left = 2 * i + 1; // Left child
    int right = 2 * i + 2; // Right child

    // Check if the left child exists and is greater than the root
    if (left < n) {
        comparisons++; // Comparison for left child
        if (arr[left] > arr[largest]) {
            largest = left;
        }
    }

    // Check if the right child exists and is greater than the root
    if (right < n) {
        comparisons++; // Comparison for right child
        if (arr[right] > arr[largest]) {
            largest = right;
        }
    }

    // If largest is not root, swap it with the root
    if (largest != i) {
        std::swap(arr[i], arr[largest]); // Swap
        swaps++; // Increment swap count

        heapify(arr, n, largest); // Recursively heapify the affected subtree
    }
}

// Function to build a max heap from the input array using the bottom-up approach
void buildHeap(std::vector<int>& arr) {
    int n = arr.size();
    
    // Start from the last internal node and heapify each node
    for (int i = n / 2 - 1; i >= 0; --i) {
        heapify(arr, n, i);
    }
}

// Function to perform heap sort on the input array
void heapSort(std::vector<int>& arr) {
    int n = arr.size();
    
    // Build a max heap
    buildHeap(arr);
    
    // Extract elements one by one from the heap
    for (int i = n - 1; i > 0; --i) {
        std::swap(arr[0], arr[i]); // Move current root to end
        swaps++; // Increment swap count

        heapify(arr, i, 0); // Call heapify on the reduced heap
    }
}

// Function to evaluate heap sort
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

    std::cout << "Heap Sort - Test case size: " << array.size() << std::endl;
    std::cout << "Comparisons: " << comparisons << std::endl;
    std::cout << "Swaps: " << swaps << std::endl;
    std::cout << "Basic operations: " << basic_operations << std::endl; // Placeholder for future operations
    std::cout << "Execution time: " << execution_time.count() << " ms" << std::endl;
    std::cout << "Memory usage: Not measured" << std::endl; // Memory usage is not measured directly in C++
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
