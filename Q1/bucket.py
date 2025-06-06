import time
import tracemalloc
import random

# Metrics
comparisons = 0
swaps = 0
basic_operations = 0

def insertion_sort_for_bucket(bucket):
    global comparisons, swaps, basic_operations
    for j in range(1, len(bucket)):
        key = bucket[j]
        i = j - 1
        while i >= 0 and bucket[i] > key:
            comparisons += 1
            bucket[i + 1] = bucket[i]
            i -= 1
            swaps += 1
        bucket[i + 1] = key
        basic_operations += 1  # for bucket[i + 1] = key
        comparisons += 1  # for the last comparison in the while loop

def bucket_sort(array):
    global comparisons, swaps, basic_operations
    n = len(array)
    
    # Create n empty buckets
    buckets = [[] for _ in range(n)]
    
    # Put array elements into different buckets
    for value in array:
        index = min(int(n * value), n - 1)  # Clamp index to [0, n-1]
        buckets[index].append(value)
        basic_operations += 1  # for appending elements
    
    # Sort individual buckets using insertion sort
    for bucket in buckets:
        insertion_sort_for_bucket(bucket)
    
    # Concatenate all buckets into the original array
    k = 0
    for bucket in buckets:
        for value in bucket:
            array[k] = value
            k += 1
            basic_operations += 1  # for moving elements back to the array

def evaluate_bucket_sort(test_case_size):
    global comparisons, swaps, basic_operations
    
    # Generate test case
    array = [random.random() for _ in range(test_case_size)]

    # Reset metrics
    comparisons = 0
    swaps = 0
    basic_operations = 0

    # Measure memory usage
    tracemalloc.start()

    # Measure execution time
    start_time = time.time()

    bucket_sort(array)

    execution_time = (time.time() - start_time) * 1000  # in milliseconds
    current, peak = tracemalloc.get_traced_memory()
    memory_usage = peak / 1024  # in KB

    tracemalloc.stop()

    print(f"Test case size: {test_case_size}")
    print(f"Comparisons: {comparisons}")
    print(f"Swaps: {swaps}")
    print(f"Basic operations: {basic_operations}")
    print(f"Execution time: {execution_time:.2f} ms")
    print(f"Memory usage: {memory_usage:.2f} KB")
    print("-" * 40)

# Main method to evaluate the bucket sort implementation
if __name__ == "__main__":
    for size in [100, 500, 1000]:
        evaluate_bucket_sort(size)
