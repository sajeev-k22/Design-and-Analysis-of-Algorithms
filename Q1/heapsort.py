import math
import time
import tracemalloc
import random
# Metrics
comparisons = 0
swaps = 0
basic_operations = 0

def heapify(arr, n, i):
    global comparisons, swaps, basic_operations
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # Left child
    right = 2 * i + 2  # Right child

    # If left child is larger than root
    if left < n:
        comparisons += 1  # Comparison for left child
        if arr[left] > arr[largest]:
            largest = left

    # If right child is larger than the largest so far
    if right < n:
        comparisons += 1  # Comparison for right child
        if arr[right] > arr[largest]:
            largest = right

    # If largest is not root
    if largest != i:
        # Swap root with the largest element
        arr[i], arr[largest] = arr[largest], arr[i]
        swaps += 1

        # Recursively heapify the affected subtree
        heapify(arr, n, largest)

def heap_sort(arr):
    global comparisons, swaps, basic_operations
    n = len(arr)

    # Build a maxheap (rearrange array)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        # Move current root to the end
        arr[0], arr[i] = arr[i], arr[0]
        swaps += 1

        # Call heapify on the reduced heap
        heapify(arr, i, 0)

def evaluate_heap_sort(test_case_size):
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

    heap_sort(array)

    execution_time = (time.time() - start_time) * 1000  # in milliseconds
    current, peak = tracemalloc.get_traced_memory()
    memory_usage = peak / 1024  # in KB

    tracemalloc.stop()

    print(f"Heap Sort - Test case size: {test_case_size}")
    print(f"Comparisons: {comparisons}")
    print(f"Swaps: {swaps}")
    print(f"Basic operations: {basic_operations}")
    print(f"Execution time: {execution_time:.2f} ms")
    print(f"Memory usage: {memory_usage:.2f} KB")
    print("-" * 40)

# Main method to evaluate the heap sort implementation
if __name__ == "__main__":
    for size in [100, 500, 1000]:
        evaluate_heap_sort(size)
