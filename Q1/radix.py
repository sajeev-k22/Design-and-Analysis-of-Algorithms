import sys
import time

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class RadixSortLinkedList:
    @staticmethod
    def insert_node(head, value):
        """
        Insert a new node with the given value at the end of the linked list.
        """
        new_node = Node(value)
        if head[0] is None:
            head[0] = new_node
        else:
            temp = head[0]
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node

    @staticmethod
    def print_list(head):
        """
        Print all the elements in the linked list.
        """
        temp = head
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    @staticmethod
    def get_max(head, basic_operations):
        """
        Find the maximum value in the linked list.
        """
        max_value = head.data
        basic_operations[0] += 1  # For initial assignment
        temp = head
        while temp is not None:
            if temp.data > max_value:
                max_value = temp.data
            temp = temp.next
            basic_operations[0] += 3  # For comparison, assignment, and pointer traversal
        return max_value

    @staticmethod
    def count_sort(head_ref, exp, comparisons, swaps, basic_operations, memory_usage):
        """
        Perform counting sort on the linked list based on the digit represented by exp.
        """
        output = [None] * 10  # Output list array
        count = [0] * 10  # Count array
        basic_operations[0] += 20  # For initializing output array (10 assignments) and count array (10 assignments)
        memory_usage[0] += (len(output) * 4) + (len(count) * 4)  # Track memory usage for arrays

        temp = head_ref[0]
        while temp is not None:
            index = (temp.data // exp) % 10
            new_head = [None]
            RadixSortLinkedList.insert_node(new_head, temp.data)
            output[index] = RadixSortLinkedList.merge(output[index], new_head[0])
            count[index] += 1
            basic_operations[0] += 4  # For the arithmetic operations and index calculation
            temp = temp.next

        # Reconstruct the linked list
        head_ref[0] = None
        for i in range(10):
            while output[i] is not None:
                RadixSortLinkedList.insert_node(head_ref, output[i].data)
                to_delete = output[i]
                output[i] = output[i].next
                to_delete = None  # No explicit delete needed, Python handles garbage collection
                swaps[0] += 1  # Increment for each node moved
                basic_operations[0] += 3  # For node deletion and pointer updates

    @staticmethod
    def merge(a, b):
        """
        Merge two linked lists.
        """
        if a is None:
            return b
        if b is None:
            return a
        temp = a
        while temp.next is not None:
            temp = temp.next
        temp.next = b
        return a

    @staticmethod
    def radix_sort(head_ref, comparisons, swaps, basic_operations, memory_usage):
        """
        Perform radix sort on the linked list.
        """
        max_value = RadixSortLinkedList.get_max(head_ref[0], basic_operations)
        memory_usage[0] += 4  # Track memory usage for max variable

        exp = 1
        while max_value // exp > 0:
            basic_operations[0] += 1  # For the exp initialization
            RadixSortLinkedList.count_sort(head_ref, exp, comparisons, swaps, basic_operations, memory_usage)
            exp *= 10
            basic_operations[0] += 1  # For exp *= 10

if __name__ == "__main__":
    try:
        head_ref = [None]  # Using a list to pass by reference
        memory_usage = 4 * 3  # Initial memory usage for head_ref and pointers

        # Read data from file and build the linked list
        with open("D:\DAA Assignment\Q1\\radix_input.txt", "r") as file:
            counter = 0
            while counter < 25:
                line = file.readline().strip()
                if not line:
                    break
                values = map(int, line.split())
                for value in values:
                    RadixSortLinkedList.insert_node(head_ref, value)
                    memory_usage += 8  # Memory usage for each node (4 bytes for int data, 4 bytes for next pointer)
                    counter += 1
                    if counter >= 25:
                        break

        comparisons = [0]  # Initialize comparison counter
        swaps = [0]  # Initialize swap counter
        basic_operations = [0]  # Initialize basic operations counter
        memory_usage_arr = [memory_usage]  # Array for memory usage to be updated

        start_time = time.time_ns()  # Start time measurement
        RadixSortLinkedList.radix_sort(head_ref, comparisons, swaps, basic_operations, memory_usage_arr)
        end_time = time.time_ns()  # End time measurement
        execution_time = end_time - start_time  # Calculate execution time

        RadixSortLinkedList.print_list(head_ref[0])

        # Print the performance metrics
        print(f"Number of Comparisons: {comparisons[0]}")
        print(f"Number of Swaps: {swaps[0]}")
        print(f"Number of Basic Operations: {basic_operations[0]}")
        print(f"Memory Usage: {memory_usage_arr[0]} bytes")
        print(f"Execution Time: {execution_time} ns")

        # Cleanup
        head_ref[0] = None  # Python handles garbage collection automatically

    except FileNotFoundError:
        print("Error: Could not open the file.", file=sys.stderr)
