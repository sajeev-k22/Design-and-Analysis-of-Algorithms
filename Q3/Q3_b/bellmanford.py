import sys

class Edge:
    """
    Class to represent an edge in the graph with a source vertex, destination vertex, and weight.
    """
    def __init__(self, source, dest, weight):
        self.source = source  # Source vertex of the edge
        self.dest = dest  # Destination vertex of the edge
        self.weight = weight  # Weight of the edge

def bellman_ford(vertices, edges, start):
    """
    Function to find the shortest paths from a starting vertex to all other vertices in a graph using the Bellman-Ford algorithm.

    Parameters:
    vertices (int): Number of vertices in the graph.
    edges (list of Edge): List of edges in the graph.
    start (int): The starting vertex for the Bellman-Ford algorithm.

    Returns:
    str: A message indicating whether a negative-weight cycle exists or not.
    """
    # Initialize distances to all vertices as infinity, and 0 for the start vertex
    dist = [float('inf')] * vertices
    dist[start] = 0

    # Relax edges up to (vertices - 1) times
    for _ in range(vertices - 1):
        updated = False  # Flag to track if any distance was updated
        for edge in edges:
            u = edge.source
            v = edge.dest
            weight = edge.weight

            # Relaxation: if a shorter path is found, update the distance
            if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                updated = True  # Mark that an update has been made
        if not updated:
            break  # No updates means no negative-weight cycle, exit early

    # Check for negative-weight cycles
    for edge in edges:
        u = edge.source
        v = edge.dest
        weight = edge.weight

        # If a shorter path is found in this step, a negative-weight cycle exists
        if dist[u] != float('inf') and dist[u] + weight < dist[v]:
            return "Graph contains a negative-weight cycle"

    # Print the shortest distances from the start vertex to all other vertices
    print("Distances from start node:")
    for i in range(vertices):
        if dist[i] == float('inf'):
            print(f"Distance to node {i}: ∞")
        else:
            print(f"Distance to node {i}: {dist[i]}")

    return "No negative-weight cycles detected"

def load_graph_from_file(filename):
    """
    Function to load the graph from a text file and create the list of edges.

    Parameters:
    filename (str): The name of the file containing the graph edges.

    Returns:
    tuple: A tuple containing the number of vertices and the list of edges.
    """
    edges = []
    vertices = 0

    with open(filename, 'r') as file:
        for line in file:
            parts = line.split()
            source, dest, weight = map(int, parts)
            edges.append(Edge(source, dest, weight))
            vertices = max(vertices, source, dest + 1)  # Update vertices count

    return vertices, edges

# Example usage
if __name__ == "__main__":
    filename =  r"E:\OneDrive - Amrita Vishwa Vidyapeetham\B.Tech\SEMESTER-5\DAA Assignment\Q3\Q3_b\Q3_b_TC.txt"  # Name of the file containing the graph edges
    vertices, edges = load_graph_from_file(filename)

    start = 0  # Starting vertex
    result = bellman_ford(vertices, edges, start)
    print(result)