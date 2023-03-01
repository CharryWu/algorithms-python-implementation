def graphTraverse(graph, s):
    n = len(graph)
    # record nodes visited so far, prevent cycles
    visited = [False] * n # len(visited) always > len(path)
    # record paths from the starting vertex till current node so far
    path = []

    # graph traverse function framework (general)
    # general graph traversal is different from trees: in trees, once you visited
    # parent node, you cannot go back; in general graphs, you might be able to revisit
    # the same node, if there exist cycles in the graph.
    def traverse(graph, node):
        if visited[node]: # Cycle detected!
            return
        # mark current node visited
        visited[node] = True
        # make the decision: visit node and add it to path
        path.append(node)

        for neighbor in graph[node]:
            traverse(graph, neighbor)
        # cancel the choice: remove node from path
        path.pop() # similar to backtracking, undo the earlier setup
        # However, different from backtracking: the do and undo is outside
        # for-loop, because we're visiting all NODES in graph dfs, while we visit
        # all EDGES in the decision tree of backtracking

    traverse(graph, s)

graph = {
    'A': set(['B', 'C']),
    'B': set(['A', 'D', 'E']),
    'C': set(['A', 'F']),
    'D': set(['B']),
    'E': set(['B', 'F']),
    'F': set(['C', 'E'])
}

graphTraverse(graph, 'A')