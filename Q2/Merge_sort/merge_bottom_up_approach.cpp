#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>

class BottomUpMergeSort {
public:
    static void bottomUpMergeSort(std::vector<int>& arr) {
        // If the array is empty or contains one or no elements, no sorting is needed.
        if (arr.empty() || arr.size() <= 1) {
            return;
        }

        int n = arr.size(); // Determine the size of the array.
        std::vector<int> temp(n); // Create a temporary array to hold sorted elements.

        // Iterate over sizes that double each iteration (1, 2, 4, 8,...).
        for (int size = 1; size < n; size *= 2) {
            // Iterate over the array in blocks defined by the current size.
            for (int start = 0; start < n - size; start += 2 * size) {
                int mid = start + size - 1; // Calculate the midpoint of the current block.
                int end = std::min(start + 2 * size - 1, n - 1); // Calculate the end of the block.
                merge(arr, start, mid, end, temp); // Merge the current block.
            }
        }
    }

private:
    static void merge(std::vector<int>& arr, int left, int mid, int right, std::vector<int>& temp) {
        // Copy the relevant portion of the array into the temporary array.
        for (int i = left; i <= right; i++) {
            temp[i] = arr[i];
        }

        int i = left; // Pointer for the left subarray.
        int j = mid + 1; // Pointer for the right subarray.
        int k = left; // Pointer for placing sorted elements back into the array.

        // Merge elements back into the original array based on order.
        while (i <= mid && j <= right) {
            if (temp[i] <= temp[j]) {
                arr[k++] = temp[i++];
            } else {
                arr[k++] = temp[j++];
            }
        }

        // Copy any remaining elements from the left subarray.
        while (i <= mid) {
            arr[k++] = temp[i++];
        }
    }
};

int main() {
    // Use a relative path or ensure the file is in the same directory as the executable
    std::ifstream file("q2_tc.txt");
    if (!file) {
        std::cerr << "Unable to open file q2_tc.txt" << std::endl;
        return 1; // Return with error code
    }

    std::string line;
    if (std::getline(file, line)) { // Read the first line from the file.
        std::istringstream iss(line);
        std::vector<int> arr;
        int number;

        // Convert the strings into integers and store them in the array.
        while (iss >> number) {
            arr.push_back(number);
        }

        // Call the bottomUpMergeSort function with the array.
        BottomUpMergeSort::bottomUpMergeSort(arr);

        // Output the sorted array.
        for (const int& num : arr) {
            std::cout << num << " ";
        }
        std::cout << std::endl; // Print newline for better readability
    } else {
        std::cerr << "The file is empty or could not read from it." << std::endl;
        return 1; // Return with error code
    }

    return 0;
}
