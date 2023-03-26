def dfsCycleCheck(G, node, visited, stack):
    visited[node] = True
    stack[node] = True
    for neighbor in G[node]:
        if not visited[neighbor]:
            if dfsCycleCheck(G,neighbor,visited,stack):
                return True
        elif stack[neighbor]:
            return True

    stack[node] = False
    return False

def isCyclic(G, N):
    visited = [False] * N
    stack = [False] * N

    for node in range(N):
        if not visited[node] and dfsCycleCheck(G, node, visited, stack):
            return True
    return False

graph = {
    0: set([1,2]),
    1: set([2]),
    2: set([0,3]),
    3: set([3])
}

print(isCyclic(graph, 4)) # Output: True

graph = {
    0: set([1,2]),
    1: set([2]),
    2: set([3]),
    3: set()
}
print(isCyclic(graph, 4)) # Output: False