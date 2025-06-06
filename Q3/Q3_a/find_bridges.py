from collections import defaultdict
import time
import tracemalloc

class Bridges:
    def __init__(self):
        self.timer = 1  # Initialize timer to track discovery times
        self.primitive_ops = 0  # Counter for primitive operations

    def DFS(self, adj_list, server, parent, tin, low, visited, bridges):
        """
        Perform DFS to find bridges in the graph.
        
        Parameters:
        adj_list (defaultdict): Adjacency list representing the graph.
        server (int): The current node being explored.
        parent (int): The parent node in the DFS tree.
        tin (list): Discovery time of nodes.
        low (list): Lowest discovery time reachable from the node.
        visited (list): Tracks whether a node has been visited.
        bridges (list): List to store the bridges found.
        """
        visited[server] = True  # Mark the current node as visited
        tin[server] = low[server] = self.timer  # Set discovery and low time
        self.timer += 1  # Increment timer for the next node
        self.primitive_ops += 4  # Increment primitive operations counter
        
        # Explore all adjacent nodes
        for it in adj_list[server]:
            self.primitive_ops += 1  # Increment for each loop iteration
            if it == parent:  # Skip the parent node to avoid revisiting
                self.primitive_ops += 1  # Condition check
                continue
            
            if not visited[it]:
                self.primitive_ops += 1  # Condition check
                # If the node hasn't been visited, perform DFS on it
                self.DFS(adj_list, it, server, tin, low, visited, bridges)
                
                # Update the low-link value of the current node
                low[server] = min(low[server], low[it])
                self.primitive_ops += 1  # Min calculation
                
                # If the condition for a bridge is met, add it to the list
                if low[it] > tin[server]:
                    bridges.append([server, it])
                    self.primitive_ops += 2  # Condition check and append operation
            else:
                # Update low-link value for already visited nodes
                low[server] = min(low[server], tin[it])
                self.primitive_ops += 1  # Min calculation

    def criticalConnections(self, n, connections):
        """
        Main function to find all bridges in the graph.
        
        Parameters:
        n (int): Number of nodes in the graph.
        connections (list of lists): List of edges in the graph.
        
        Returns:
        list of lists: The bridges found in the graph.
        """
        # Initialize adjacency list
        adj_list = defaultdict(list)
        for u, v in connections:
            adj_list[u].append(v)
            adj_list[v].append(u)
            self.primitive_ops += 2  # Two append operations
        
        # Initialize auxiliary arrays
        low = [0] * (n + 1)
        tin = [0] * (n + 1)
        visited = [False] * (n + 1)
        bridges = []  # List to store the bridges
        
        self.primitive_ops += 3 * (n + 1)  # Initialization of arrays
        
        # Start DFS from the first node (node 1)
        self.DFS(adj_list, 1, -1, tin, low, visited, bridges)
        
        return bridges

if __name__ == "__main__":
    # Read input from a text file
    input_file = "E:\OneDrive - Amrita Vishwa Vidyapeetham\B.Tech\SEMESTER-5\DAA Assignment\Q3\Q3_a\\find_bridges_TC.txt" 
    connections = []
    n = 0

    try:
        with open(input_file, "r") as file:
            n = int(file.readline().strip())  # First line: number of nodes
            for line in file:
                u, v = map(int, line.strip().split())
                connections.append([u, v])
    except FileNotFoundError:
        print(f"File {input_file} not found.")
        exit(1)
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        exit(1)
    
    # Start memory tracking and time measurement
    tracemalloc.start()
    start_time = time.time()
    
    # Instantiate the Bridges class and find the critical connections
    obj = Bridges()
    bridges = obj.criticalConnections(n, connections)
    
    # End time measurement
    end_time = time.time()
    # End memory tracking and get memory usage
    _, peak_memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    # Print the results
    print("Bridges (Critical Connections) in the graph are:", bridges)
    print("Time taken:", (end_time - start_time) * 1000, "ms")
    print("Maximum memory used:", peak_memory / 1024, "KB")
    print("Primitive operations count:", obj.primitive_ops)
