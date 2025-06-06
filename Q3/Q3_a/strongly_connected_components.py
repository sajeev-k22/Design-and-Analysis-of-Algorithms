'''
Caution:
This '''




from collections import defaultdict, deque
import time
import tracemalloc





class SCC:
    def __init__(self):
        self.primitive_ops = 0  # Counter for primitive operations

    def get_sorted_order(self, adj, vertex, visited, sorted_order):
        """
        Perform a Depth-First Search (DFS) to determine the finishing order of vertices.

        Parameters:
        adj (defaultdict): The adjacency list of the original graph.
        vertex (int): The current vertex to start the DFS from.
        visited (list): A list to keep track of visited vertices.
        sorted_order (deque): A stack to store the vertices in their finishing order.
        """
        visited[vertex] = True  # Mark the current vertex as visited
        self.primitive_ops += 1  # Increment operation for assignment
        # Explore all adjacent vertices that haven't been visited yet
        for node in adj[vertex]:
            self.primitive_ops += 1  # Increment for each loop iteration
            if not visited[node]:
                self.primitive_ops += 1  # Increment for condition check
                self.get_sorted_order(adj, node, visited, sorted_order)
        # Once all adjacent vertices are visited, push the current vertex to the stack
        sorted_order.append(vertex)
        self.primitive_ops += 1  # Increment for append operation

    def DFS(self, adj_list, vertex, visited):
        """
        Perform a DFS on the reversed graph to mark all vertices in the current SCC.

        Parameters:
        adj_list (defaultdict): The adjacency list of the reversed graph.
        vertex (int): The current vertex to start the DFS from.
        visited (list): A list to keep track of visited vertices.
        """
        visited[vertex] = True  # Mark the current vertex as visited
        self.primitive_ops += 1  # Increment operation for assignment
        # Recursively visit all adjacent vertices that haven't been visited yet
        for node in adj_list[vertex]:
            self.primitive_ops += 1  # Increment for each loop iteration
            if not visited[node]:
                self.primitive_ops += 1  # Increment for condition check
                self.DFS(adj_list, node, visited)

    def kosaraju(self, V, adj):
        """
        Implementation of Kosaraju's Algorithm to find the number of Strongly Connected Components (SCCs) in a graph.

        Parameters:
        V (int): The number of vertices in the graph.
        adj (defaultdict): The adjacency list representing the original graph.

        Returns:
        int: The number of SCCs in the graph.
        """
        sorted_order = deque()  # Stack to hold vertices in the order of their finishing times
        visited = [False] * V   # List to keep track of visited vertices during DFS
        self.primitive_ops += V  # Initialization of visited list

        # Step 1: Perform DFS to determine the finishing order of vertices
        for i in range(V):
            self.primitive_ops += 1  # Increment for each loop iteration
            if not visited[i]:
                self.primitive_ops += 1  # Increment for condition check
                self.get_sorted_order(adj, i, visited, sorted_order)

        # Step 2: Reverse the original graph to prepare for the second DFS pass
        reversed_adj = defaultdict(list)
        for i in range(V):
            self.primitive_ops += 1  # Increment for each loop iteration
            for j in adj[i]:
                reversed_adj[j].append(i)  # Reverse the direction of the edges
                self.primitive_ops += 1  # Increment for append operation

        # Step 3: Perform DFS on the reversed graph in the order of finishing times
        visited = [False] * V  # Reset the visited list for the second DFS
        self.primitive_ops += V  # Resetting visited list
        num_scc = 0  # Initialize the count of SCCs

        while sorted_order:
            self.primitive_ops += 1  # Increment for each loop iteration
            curr_vertex = sorted_order.pop()  # Get the next vertex in the finishing order
            self.primitive_ops += 1  # Increment for pop operation
            if not visited[curr_vertex]:
                num_scc += 1  # Each DFS from an unvisited vertex identifies a new SCC
                self.primitive_ops += 2  # Increment for condition check and addition
                self.DFS(reversed_adj, curr_vertex, visited)

        return num_scc  # Return the total number of SCCs found

if __name__ == "__main__":
    solution = SCC()

    # Read input from a text file
    input_file = "E:\OneDrive - Amrita Vishwa Vidyapeetham\B.Tech\SEMESTER-5\DAA Assignment\Q3\Q3_a\\strongly_connected_components_TC.txt"  # Replace with your file name
    adj = defaultdict(list)  # Adjacency list representation of the graph
    V = 0

    try:
        with open(input_file, "r") as file:
            V = int(file.readline().strip())  # First line: number of vertices
            for line in file:
                u, v = map(int, line.strip().split())
                adj[u].append(v)
    except FileNotFoundError:
        print(f"File {input_file} not found.")
        exit(1)
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        exit(1)

    # Start memory tracking and time measurement
    tracemalloc.start()
    start_time = time.time()
    
    # Run Kosaraju's algorithm to find the number of SCCs
    result = solution.kosaraju(V, adj)
    
    # End time measurement
    end_time = time.time()
    # End memory tracking and get memory usage
    _, peak_memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    # Output the result
    print(f"Number of Strongly Connected Components (SCCs): {result}")
    print("Time taken:", (end_time - start_time) * 1000, "ms")
    print("Maximum memory used:", peak_memory / 1024, "KB")
    print("Primitive operations count:", solution.primitive_ops)
