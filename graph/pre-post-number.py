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
    aList = {[i]: set() for i in range(n)}

    pre = [0] * n
    post = [0] * n

    # visitedited array
    visited = [0] * n

    # Edges
    aList[0].append(1)
    aList[0].append(2)
    aList[1].append(0)
    aList[1].append(3)
    aList[2].append(0)
    aList[2].append(3)
    aList[2].append(4)
    aList[3].append(1)
    aList[3].append(2)
    aList[4].append(2)
    aList[4].append(5)
    aList[5].append(4)

    # DFS starting at Node 1
    dfs(1, aList, pre, post, visited)

    # Number of nodes in graph
    for i in range(1, n + 1):
        print("Node " + str(i) +
              " Pre number " + str(pre[i]) +
              " Post number " + str(post[i]))

# This code is contributed by rutvik_56
