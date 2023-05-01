# Python program to find single source shortest paths
# for Directed Acyclic Graphs Complexity :O(V+E)
from collections import deque

# The function to do Topological Sort. It uses recursive
# topologicalSortUtil()
def topologicalSort(graph):
    # Mark all the vertices as not visited
    visited = [False] * len(graph)
    stack = []

    def dfsPostOrder(node):
        # Mark the current node as visited.
        visited[node] = True

        # Recur for all the vertices adjacent to this vertex
        for neighbor, weight in graph[node]:
            if not visited[neighbor]:
                dfsPostOrder(neighbor)

        # Push current vertex to stack which stores result
        stack.append(node)

    # Call the recursive helper function to store Topological
    # Sort starting from all vertices one by one
    for key in graph:
        if not visited[key]:
            dfsPostOrder(key)

    res = deque()
    for i in range(len(stack)-1,-1,-1):
        res.append(stack[i])
    # Print contents of the stack
    return res  # return list in reverse order

def shortestPathDAG(graph, s):
    topo_order = topologicalSort(graph)
    dist = [float('inf')] * len(graph)
    dist[s] = 0
    while topo_order:
        top = topo_order.popleft()
        for neighbor, weight in graph[top]:
            if dist[neighbor] > dist[top] + weight:
                    dist[neighbor] = dist[top] + weight

    for i in range(len(graph)):
        print(("%d" % dist[i]) if dist[i] != float("inf") else "Inf" ,end=" ")


# Graph is represented using adjacency list. Every
# node of adjacency list contains vertex number of
# the vertex to which edge connects. It also contains
# weight of the edge
graph = {
    0: set([(1,5),(2,3)]),
    1: set([(3,6),(2,2)]),
    2: set([(4,4),(5,2),(3,7)]),
    3: set([(4,-1)]),
    4: set([(5,-2)]),
    5: set(),
}

# source = 1
shortestPathDAG(graph, 1)
