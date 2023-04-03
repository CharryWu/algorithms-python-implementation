# https://www.geeksforgeeks.org/topological-sorting/
# https://leetcode.com/problems/course-schedule/
# Python program to print topological sorting of a DAG
# The reverse of post-order traversal is topological sort

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
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfsPostOrder(neighbor)

        # Push current vertex to stack which stores result
        stack.append(node)

    # Call the recursive helper function to store Topological
    # Sort starting from all vertices one by one
    for key in graph:
        if not visited[key]:
            dfsPostOrder(key)

    # Print contents of the stack
    return stack[::-1]  # return list in reverse order


# Driver Code
if __name__ == '__main__':
    graph = {
        0: set(),
        1: set(),
        2: set([3]),
        3: set([1]),
        4: set([0, 1]),
        5: set([0, 2]),
    }

    print("Following is a Topological Sort of the given graph")

    print(topologicalSort(graph))
