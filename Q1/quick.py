import time
import tracemalloc
import random

# Metrics
comparisons = 0
swaps = 0
basic_operations = 0

def quick_sort(array, p, r):
    global comparisons, swaps, basic_operations
    if p < r:
        q = partition(array, p, r)
        quick_sort(array, p, q - 1)
        quick_sort(array, q + 1, r)

def partition(array, p, r):
    global comparisons, swaps, basic_operations
    # Choose a random pivot index
    pivot_index = p + random.randint(0, r - p)
    
    # Swap pivot with the last element
    array[pivot_index], array[r] = array[r], array[pivot_index]
    swaps += 1

    pivot = array[r]
    i = p - 1

    for j in range(p, r):
        comparisons += 1  # Comparison in the loop
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
            swaps += 1

    array[i + 1], array[r] = array[r], array[i + 1]
    swaps += 1
    return i + 1

def evaluate_quick_sort(test_case_size):
    global comparisons, swaps, basic_operations
    
    # Generate test case
    array = [random.randint(0, 1000) for _ in range(test_case_size)]

    # Reset metrics
    comparisons = 0
    swaps = 0
    basic_operations = 0

    # Measure memory usage
    tracemalloc.start()

    # Measure execution time
    start_time = time.time()

    quick_sort(array, 0, len(array) - 1)

    execution_time = (time.time() - start_time) * 1000  # in milliseconds
    current, peak = tracemalloc.get_traced_memory()
    memory_usage = peak / 1024  # in KB

    tracemalloc.stop()

    print(f"Quick Sort - Test case size: {test_case_size}")
    print(f"Comparisons: {comparisons}")
    print(f"Swaps: {swaps}")
    print(f"Basic operations: {basic_operations}")
    print(f"Execution time: {execution_time:.2f} ms")
    print(f"Memory usage: {memory_usage:.2f} KB")
    print("-" * 40)

# Main method to evaluate the quick sort implementation
if __name__ == "__main__":
    for size in [100, 500, 1000]:
        evaluate_quick_sort(size)
