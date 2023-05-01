# https://www.geeksforgeeks.org/printing-pre-and-post-visitedited-times-in-dfs-of-a-graph/

# Variable to keep track of time
time = 1

# Function to perform DFS starting
# from node u


def dfs(u, aList, pre, post, visited):

    global time

    # Storing the pre number whenever
    # the node comes into recursion stack
    pre[u] = time

    # Increment time
    time += 1

    visited[u] = 1

    for v in aList[u]:
        if (visited[v] == 0):
            dfs(v, aList, pre, post, visited)

    # Storing the post number whenever
    # the node goes out of recursion stack
    post[u] = time
    time += 1


# Driver code
if __name__ == '__main__':

    # Number of nodes in graph
    n = 6

    # Adjacency list
    aList = { i: set() for i in range(n)}

    pre = [0] * n
    post = [0] * n

    # visitedited array
    visited = [0] * n

    # Edges
    aList[0].add(1)
    aList[0].add(2)
    aList[1].add(0)
    aList[1].add(3)
    aList[2].add(0)
    aList[2].add(3)
    aList[2].add(4)
    aList[3].add(1)
    aList[3].add(2)
    aList[4].add(2)
    aList[4].add(5)
    aList[5].add(4)

    # DFS starting at Node 1
    dfs(1, aList, pre, post, visited)

    # Number of nodes in graph
    for i in range(n):
        print("Node " + str(i) +
              " Pre number " + str(pre[i]) +
              " Post number " + str(post[i]))

# This code is contributed by rutvik_56
