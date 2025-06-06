import math
import time
import tracemalloc
import random

# Metrics to track performance
comparisons = 0
swaps = 0
basic_operations = 0

def merge(array, chunks):
    """
    Merges sorted chunks into a single sorted array.
    """
    global comparisons, swaps, basic_operations
    k = len(chunks)  # Number of chunks to merge
    indices = [0] * k  # Array to keep track of current index in each chunk
    idx = 0  # Index for the current position in the result array
    n = len(array)  # Total length of the array to be sorted

    while idx < n:
        min_index = -1  # Index of the chunk with the smallest element
        min_value = float('inf')  # Initialize min_value with infinity

        # Find the minimum value among the k chunks
        for i in range(k):
            if indices[i] < len(chunks[i]):
                comparisons += 1  # Comparison to find the minimum value
                if chunks[i][indices[i]] < min_value:
                    min_value = chunks[i][indices[i]]
                    min_index = i

        # Place the minimum value into the result array
        if min_index != -1:
            array[idx] = min_value
            indices[min_index] += 1
            idx += 1
            basic_operations += 1  # Counting the operation of placing the value

def three_way_merge_sort(array):
    """
    Performs a 3-way merge sort on the array.
    """
    global comparisons, swaps, basic_operations
    if len(array) < 2:
        return  # Base case: Array is already sorted

    n = len(array)
    chunk_size = math.ceil(n / 3)  # Size of each chunk for 3-way split

    # Divide the array into 3 chunks
    chunks = [array[i * chunk_size:min((i + 1) * chunk_size, n)] for i in range(3)]

    # Sort each chunk individually
    for i in range(3):
        chunks[i].sort()  # Sort each chunk using built-in sort
        basic_operations += len(chunks[i]) * math.log(len(chunks[i]), 2)  # Estimate operations for sorting

    # Merge all chunks
    merge(array, chunks)

def evaluate_three_way_merge_sort(test_case_size):
    """
    Evaluates the performance of the 3-way merge sort with a given test case size.
    """
    global comparisons, swaps, basic_operations
    
    # Generate a random test case
    array = [random.randint(0, 1000) for _ in range(test_case_size)]

    # Reset performance metrics
    comparisons = 0
    swaps = 0
    basic_operations = 0

    # Measure memory usage
    tracemalloc.start()

    # Measure execution time
    start_time = time.time()

    three_way_merge_sort(array)  # Sorting with 3-way merge sort

    execution_time = (time.time() - start_time) * 1000  # Convert execution time to milliseconds
    current, peak = tracemalloc.get_traced_memory()
    memory_usage = peak / 1024  # Convert memory usage to KB

    tracemalloc.stop()

    print(f"3-Way Merge Sort - Test case size: {test_case_size}")
    print(f"Comparisons: {comparisons}")
    print(f"Swaps: {swaps}")
    print(f"Basic operations: {basic_operations}")
    print(f"Execution time: {execution_time:.2f} ms")
    print(f"Memory usage: {memory_usage:.2f} KB")
    print("-" * 40)

# Main method to evaluate the 3-way merge sort implementation
if __name__ == "__main__":
    for size in [100, 500, 1000]:
        evaluate_three_way_merge_sort(size)
