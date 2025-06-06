#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

// Function to merge two halves of the array
void merge(vector<int>& arr, int left, int mid, int right, vector<int>& temp) {
    // Copy the array elements within the range [left, right] to a temporary array for safe merging
    for (int i = left; i <= right; i++) {
        temp[i] = arr[i];
    }

    int i = left;      // Start index for the left subarray
    int j = mid + 1;   // Start index for the right subarray
    int k = left;      // Start index for the merged array

    // Merge the two subarrays back into the original array
    while (i <= mid && j <= right) {
        if (temp[i] <= temp[j]) {  // If the current element in the left subarray is smaller or equal
            arr[k++] = temp[i++];  // Copy it to the merged array
        } else {  // If the current element in the right subarray is smaller
            arr[k++] = temp[j++];  // Copy it to the merged array
        }
    }

    // Copy any remaining elements from the left subarray (if any)
    while (i <= mid) {
        arr[k++] = temp[i++];
    }
    // Note: Remaining elements from the right subarray (if any) are already in place
}

// Helper function to perform merge sort recursively
void mergeSortHelper(vector<int>& arr, int left, int right, vector<int>& temp) {
    // Base case: If the subarray has one or zero elements, it's already sorted
    if (left >= right) {
        return;
    }

    // Calculate the middle point to divide the array into two halves
    int mid = left + (right - left) / 2;

    // Recursively sort the left half
    mergeSortHelper(arr, left, mid, temp);

    // Recursively sort the right half
    mergeSortHelper(arr, mid + 1, right, temp);

    // Merge the two sorted halves
    merge(arr, left, mid, right, temp);
}

// Function to perform merge sort on the entire array
void mergeSort(vector<int>& arr) {
    // Check if the array is empty
    if (arr.empty()) {
        return;
    }

    // Temporary vector for merging operations
    vector<int> temp(arr.size());

    // Call the helper function to perform the recursive merge sort
    mergeSortHelper(arr, 0, arr.size() - 1, temp);
}

int main() {
    // Open the input file "input.txt" for reading the array data
    ifstream infile("q2_tc.txt");

    // Check if the file was successfully opened
    if (!infile.is_open()) {
        cerr << "Error opening file" << endl;  // Display error if file cannot be opened
        return 1;  // Exit the program with an error code
    }

    // Read the data from the file into a vector
    vector<int> arr;
    int num;
    while (infile >> num) {  // Read each integer from the file
        arr.push_back(num);  // Add it to the array vector
    }

    // Close the file after reading all the data
    infile.close();

    // Perform merge sort on the array
    mergeSort(arr);

    // Output the sorted array to the console
    for (int n : arr) {
        cout << n << " ";  // Print each element followed by a space
    }
    cout << endl;  // Print a newline at the end

    return 0;  // Exit the program successfully
}