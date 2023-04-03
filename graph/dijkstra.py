# https://bradfieldcs.com/algos/graphs/dijkstras-algorithm/
# https://www.geeksforgeeks.org/difference-between-minimum-spanning-tree-and-shortest-path/
"""
Dijkstra's Algorithm basically starts at the node that you choose (the source node) and it analyzes the graph to find the shortest path between that node and all the other nodes in the graph.
The algorithm keeps track of the currently known shortest distance from each node to the source node and it updates these values if it finds a shorter path.
Once the algorithm has found the shortest path between the source node and another node, that node is marked as "visited" and added to the path.
The process continues until all the nodes in the graph have been added to the path. This way, we have a path that connects the source node to all other nodes following the shortest path possible to reach each node.
"""
import heapq

def calculate_distances(graph, starting_vertex):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[starting_vertex] = 0

    pq = [(0, starting_vertex)]
    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)

        # Nodes can get added to the priority queue multiple times. 
        # This is done to allow negative weight edges (but not cycles) in the graph
        # If there's neg edges, the algorithm may still execute correctly.
        # See https://stackoverflow.com/a/6799344 for explanation of dij on graph w/ neg weights
        # We only process a vertex the first time we remove it from the priority queue.
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Relaxation Process:
            # https://stackoverflow.com/a/12782820
            # Only consider this new path if it's better than any path we've
            # already found.
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances


example_graph = {
    'U': {'V': 2, 'W': 5, 'X': 1},
    'V': {'U': 2, 'X': 2, 'W': 3},
    'W': {'V': 3, 'U': 5, 'X': 3, 'Y': 1, 'Z': 5},
    'X': {'U': 1, 'V': 2, 'W': 3, 'Y': 1},
    'Y': {'X': 1, 'W': 1, 'Z': 1},
    'Z': {'W': 5, 'Y': 1},
}
print(calculate_distances(example_graph, 'X'))
# => {'U': 1, 'W': 2, 'V': 2, 'Y': 1, 'X': 0, 'Z': 2}

#       A
#       / \
#      /   \
#     /     \
#   5       2
#   ↙         ↘
#   B--(-10)-->C
example_graph = {
    'A': {'C': 2, 'B': 5 },
    'B': {'C': -99},
    'C': {}
}
print(calculate_distances(example_graph, 'A'))
# => {'A': 0, 'B': 5, 'C': -94}
