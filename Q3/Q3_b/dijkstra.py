import heapq

class Edge:
    """
    Class to represent an edge in the graph with a destination vertex and weight.
    """
    def __init__(self, dest, weight):
        self.dest = dest  # Target vertex of the edge
        self.weight = weight  # Weight of the edge

class Node:
    """
    Class to represent a node in the priority queue with a vertex and its distance.
    """
    def __init__(self, vertex, dist):
        self.vertex = vertex  # The vertex value
        self.dist = dist  # Distance from the starting node

    def __lt__(self, other):
        """
        Comparison method for the priority queue to order nodes by their distance.
        """
        return self.dist < other.dist

def dijkstra(vertices, graph, start):
    """
    Function to find the shortest paths from a starting vertex to all other vertices in a graph using Dijkstra's algorithm.

    Parameters:
    vertices (int): Number of vertices in the graph.
    graph (list of lists): Adjacency list where each list contains Edge objects representing the edges.
    start (int): The starting vertex for Dijkstra's algorithm.

    Returns:
    list of Node: A list of Node objects representing the shortest distances from the start vertex.
    """
    # Initialize distances to all vertices as infinity, and 0 for the start vertex
    nodes = [Node(i, float('inf')) for i in range(vertices)]
    nodes[start].dist = 0

    # Create a priority queue and add the start vertex
    pq = []
    heapq.heappush(pq, nodes[start])

    while pq:
        # Extract the node with the smallest distance from the priority queue
        current_node = heapq.heappop(pq)
        u = current_node.vertex

        # Traverse adjacent vertices
        for edge in graph[u]:
            v = edge.dest
            weight = edge.weight
            new_dist = current_node.dist + weight

            # Relax the edge if a shorter path is found
            if new_dist < nodes[v].dist:
                nodes[v].dist = new_dist
                heapq.heappush(pq, nodes[v])  # Add the updated node to the priority queue

    return nodes

def load_graph_from_file(filename):
    """
    Function to load the graph from a text file and create the adjacency list representation.

    Parameters:
    filename (str): The name of the file containing the graph edges.

    Returns:
    tuple: A tuple containing the number of vertices and the adjacency list of the graph.
    """
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Determine the number of vertices (can be inferred from edges if not given explicitly)
    vertices = 0
    edges = []
    for line in lines:
        source, dest, weight = map(int, line.split())
        edges.append((source, Edge(dest, weight)))
        vertices = max(vertices, source + 1, dest + 1)  # Update vertices count

    # Create adjacency list
    graph = [[] for _ in range(vertices)]
    for source, edge in edges:
        graph[source].append(edge)

    return vertices, graph

# Example usage
if __name__ == "__main__":
    filename = r"E:\OneDrive - Amrita Vishwa Vidyapeetham\B.Tech\SEMESTER-5\DAA Assignment\Q3\Q3_b\Q3_b_TC.txt"  # Use raw string to avoid escape issues
    vertices, graph = load_graph_from_file(filename)

    start = 0  # Starting vertex for Dijkstra's algorithm
    nodes = dijkstra(vertices, graph, start)

    # Print the shortest distances from the start vertex
    print("Distances from start node:")
    for node in nodes:
        if node.dist == float('inf'):
            print(f"Distance to node {node.vertex}: INFINITY")
        else:
            print(f"Distance to node {node.vertex}: {node.dist}")
