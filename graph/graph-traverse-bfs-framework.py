from collections import deque # use deque popleft() to speed up exec time

def graphTraverse(graph, s):
    visited = set() # store all the nodes that we've visited
    queue = deque([]) # store all nodes which are waiting to be processed
    step = 0 # number of steps neeeded from root to current node

    # initialize
    queue.append(s)
    visited.add(s)

    while len(queue) > 0:
        sz = len(queue)
        # iterate the nodes which are already in the queue
        for i in range(sz):
            cur = queue.popleft()
            # NOTE: ADD OPERATION HERE, e.g. check if node is target

            for neighbor in graph[cur]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

        step += 1

graph = {
    'A': set(['B', 'C']),
    'B': set(['A', 'D', 'E']),
    'C': set(['A', 'F']),
    'D': set(['B']),
    'E': set(['B', 'F']),
    'F': set(['C', 'E'])
}

graphTraverse(graph, 'A')
