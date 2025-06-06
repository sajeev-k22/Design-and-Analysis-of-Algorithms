from collections import defaultdict
import time
import tracemalloc

class ArticulationPoint:
    def __init__(self):
        # Initialize a timer variable to assign time of insertion (tin) values during DFS traversal
        self.timer = 1

    def dfs(self, node, parent, vis, tin, low, mark, adj):
        """
        Perform Depth-First Search (DFS) to find and mark articulation points in the graph.

        Parameters:
        node (int): Current node being visited.
        parent (int): Parent of the current node.
        vis (list): List to track visited nodes.
        tin (list): List to store the discovery times of visited nodes.
        low (list): List to store the lowest discovery times reachable from the node.
        mark (list): List to mark nodes as articulation points.
        adj (defaultdict): Adjacency list representing the graph.
        """
        vis[node] = 1  # Mark the current node as visited
        tin[node] = low[node] = self.timer  # Set the discovery time and low value for the node
        self.timer += 1  # Increment the timer for the next node
        child = 0  # Initialize a counter for the number of children in the DFS tree

        # Traverse all the adjacent nodes of the current node
        for it in adj[node]:
            if it == parent:
                continue  # If the adjacent node is the parent, skip it to avoid revisiting the parent

            if vis[it] == 0:
                # If the adjacent node has not been visited, perform DFS on it
                self.dfs(it, node, vis, tin, low, mark, adj)
                # Update the low value of the current node based on the DFS result
                low[node] = min(low[node], low[it])

                # Check if the current node is an articulation point
                if low[it] >= tin[node] and parent != -1:
                    mark[node] = 1  # Mark the current node as an articulation point
                child += 1  # Increment the child count

            else:
                # If the adjacent node is already visited, update the low value of the current node
                low[node] = min(low[node], tin[it])

        # Special case: If the current node is the root of the DFS tree and has more than one child,
        # then it is an articulation point
        if child > 1 and parent == -1:
            mark[node] = 1

    def articulation_points(self, n, adj):
        """
        Find all articulation points in the graph.

        Parameters:
        n (int): Number of nodes in the graph.
        adj (defaultdict): Adjacency list representing the graph.

        Returns:
        list: A list of all articulation points in the graph.
        """
        vis = [0] * n  # Initialize the visited list for all nodes
        tin = [0] * n  # Initialize the tin (discovery time) list for all nodes
        low = [0] * n  # Initialize the low list for all nodes
        mark = [0] * n  # Initialize the mark list to track articulation points

        # Perform DFS for each unvisited node to find all articulation points
        for i in range(n):
            if vis[i] == 0:
                self.dfs(i, -1, vis, tin, low, mark, adj)

        # Collect all nodes that are marked as articulation points
        ans = [i for i in range(n) if mark[i] == 1]

        # If no articulation points are found, return [-1] to indicate that
        if not ans:
            ans.append(-1)
        return ans

def read_graph_from_file(file_path):
    """
    Read a graph from a text file and return the number of vertices and adjacency list.

    Parameters:
    file_path (str): Path to the input file containing the graph.

    Returns:
    int, defaultdict: Number of vertices and the adjacency list of the graph.
    """
    adj = defaultdict(list)  # Initialize the adjacency list
    with open(file_path, 'r') as file:
        n = int(file.readline().strip())  # Read the number of vertices
        for line in file:
            u, v = map(int, line.strip().split())
            adj[u].append(v)  # Add edge u -> v
            adj[v].append(u)  # Add edge v -> u (since the graph is undirected)
    return n, adj

def main():
    # Start memory tracking and time measurement
    tracemalloc.start()
    start_time = time.time()

    # Read the graph from the input file
    n, adj = read_graph_from_file("E:\OneDrive - Amrita Vishwa Vidyapeetham\B.Tech\SEMESTER-5\DAA Assignment\Q3\Q3_a\\articulation_point_TC.txt")

    # Create an object of the ArticulationPoint class
    obj = ArticulationPoint()

    # Find the articulation points in the graph
    nodes = obj.articulation_points(n, adj)

    # End time measurement
    end_time = time.time()

    # End memory tracking and get memory usage
    _, peak_memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    # Output the articulation points found in the graph
    print("Articulation points in the graph are:", nodes)
    print("Time taken:", (end_time - start_time) * 1000, "ms")
    print("Maximum memory used:", peak_memory / 1024, "KB")

if __name__ == "__main__":
    main()