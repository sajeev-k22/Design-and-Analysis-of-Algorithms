import time
import tracemalloc

class Edge:
    """
    Class to represent an edge in the graph with source vertex, destination vertex, and weight.
    """
    def __init__(self, u, v, weight):
        self.u = u  # Source vertex of the edge
        self.v = v  # Destination vertex of the edge
        self.weight = weight  # Weight of the edge

class UnionFind:
    """
    Union-Find data structure for tracking components and performing union and find operations.
    """
    def __init__(self, size):
        self.parent = list(range(size))  # Initialize parent array where each node is its own parent
        self.rank = [0] * size  # Rank array for union by rank

    def find(self, u):
        """
        Find the representative (root) of the set containing u with path compression.

        Parameters:
        u (int): The vertex to find the representative of.

        Returns:
        int: The root of the set containing u.
        """
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        """
        Union the sets containing u and v using union by rank.

        Parameters:
        u (int): One vertex of the set to union.
        v (int): The other vertex of the set to union.
        """
        root_u = self.find(u)  # Find root of the set containing u
        root_v = self.find(v)  # Find root of the set containing v
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def boruvka_mst(vertices, edges):
    """
    Method to find the Minimum Spanning Tree (MST) using Borůvka's algorithm.

    Parameters:
    vertices (int): Number of vertices in the graph.
    edges (list of Edge): List of edges in the graph.

    Returns:
    list of Edge: List of edges in the Minimum Spanning Tree.
    """
    mst = []  # List to store the MST edges
    uf = UnionFind(vertices)  # Create Union-Find data structure to manage components
    primitive_ops = 0  # Counter for primitive operations

    # Continue until we have vertices - 1 edges in the MST
    while len(mst) < vertices - 1:
        # Initialize the minimum edge array for each component
        min_edge = [None] * vertices
        primitive_ops += vertices  # Initializing the min_edge array

        # Find the cheapest edge for each component
        for edge in edges:
            root_u = uf.find(edge.u)  # Find root of the component containing u
            root_v = uf.find(edge.v)  # Find root of the component containing v
            primitive_ops += 2  # For the find operations

            if root_u != root_v:  # Only consider edges between different components
                if min_edge[root_u] is None or min_edge[root_u].weight > edge.weight:
                    min_edge[root_u] = edge  # Update minimum edge for component of u
                    primitive_ops += 1  # Update operation

                if min_edge[root_v] is None or min_edge[root_v].weight > edge.weight:
                    min_edge[root_v] = edge  # Update minimum edge for component of v
                    primitive_ops += 1  # Update operation

        # Add the cheapest edges to the MST
        for edge in min_edge:
            if edge is not None:
                root_u = uf.find(edge.u)  # Find root of the component containing u
                root_v = uf.find(edge.v)  # Find root of the component containing v
                primitive_ops += 2  # For the find operations

                if root_u != root_v:  # Only add edge if it connects different components
                    uf.union(root_u, root_v)  # Union the components
                    mst.append(edge)  # Add edge to MST
                    primitive_ops += 1  # For the append operation

    return mst, primitive_ops

# Example usage
if __name__ == "__main__":
    vertices = 23  # Number of vertices in the graph
    edges = [
        Edge(0, 1, 10),
        Edge(0, 2, 5),
        Edge(1, 3, 2),
        Edge(1, 4, 1),
        Edge(2, 5, 2),
        Edge(2, 6, 7),
        Edge(3, 7, 4),
        Edge(3, 8, 6),
        Edge(4, 9, 3),
        Edge(4, 10, 2),
        Edge(5, 11, 8),
        Edge(5, 12, 3),
        Edge(6, 13, 1),
        Edge(6, 14, 4),
        Edge(7, 15, 9),
        Edge(7, 16, 5),
        Edge(8, 17, 2),
        Edge(8, 18, 7),
        Edge(9, 19, 6),
        Edge(10, 20, 3),
        Edge(11, 21, 4),
        Edge(12, 22, 5),
        Edge(13, 14, 2),
        Edge(14, 15, 1),
        Edge(15, 16, 4),
        Edge(16, 17, 3),
        Edge(17, 18, 6),
        Edge(18, 19, 5),
        Edge(19, 20, 2),
        Edge(20, 21, 7),
        Edge(21, 22, 4)
    ]

    # Start measuring time and memory
    start_time = time.time()
    tracemalloc.start()

    # Compute the Minimum Spanning Tree (MST)
    mst, primitive_ops = boruvka_mst(vertices, edges)

    # Stop measuring time and memory
    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    # Print the edges in the MST and the total weight
    print("Edges in the Minimum Spanning Tree:")
    total_weight = 0
    for edge in mst:
        print(f"Edge: ({edge.u}, {edge.v}) Weight: {edge.weight}")
        total_weight += edge.weight
    print(f"Total weight of MST: {total_weight}")

    # Print the performance metrics
    print(f"Time taken: {end_time - start_time:.6f} seconds")
    print(f"Current memory usage: {current / 10**6:.6f} MB; Peak memory usage: {peak / 10**6:.6f} MB")
    print(f"Number of primitive operations: {primitive_ops}")
