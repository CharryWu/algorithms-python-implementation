from collections import defaultdict, deque

class Graph:
    def init(self, n):
        self.graph = defaultdict(list)
        self.n = n
        self.index = 0
        self.stack = []
        self.indices = [-1] * n
        self.lowlink = [-1] * n
        self.on_stack = [False] * n
        self.sccs = []

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def tarjan_scc(self, v):
        """
        A recursive function to find strongly connected components using
        Tarjan's algorithm.

        :param v: The current vertex being processed.
        :type v: int
        """
        self.indices[v] = self.index
        self.lowlink[v] = self.index
        self.index += 1
        self.stack.append(v)
        self.on_stack[v] = True

        for w in self.graph[v]:
            if self.indices[w] == -1:
                self.tarjan_scc(w)
                self.lowlink[v] = min(self.lowlink[v], self.lowlink[w])
            elif self.on_stack[w]:
                self.lowlink[v] = min(self.lowlink[v], self.indices[w])

        if self.lowlink[v] == self.indices[v]:
            scc = []
            while True:
                w = self.stack.pop()
                self.on_stack[w] = False
                scc.append(w)
                if w == v:
                    break
            self.sccs.append(scc)

    def get_sccs(self):
        for v in range(self.n):
            if self.indices[v] == -1:
                self.tarjan_scc(v)
        return self.sccs

def topologically_sorted_sccs(graph, weights):
    # Get the SCCs
    """
    Sorts the strongly connected components (SCCs) of a weighted cyclic graph
    topologically, and within each SCC, sorts the nodes by weight in descending
    order.

    :param graph: A Graph object representing the weighted cyclic graph.
    :type graph: Graph
    :param weights: A list of weights associated with each node in the graph.
    :type weights: List[int]
    :return: A list of nodes, sorted topologically by SCC and within each SCC,
             sorted by weight in descending order.
    :rtype: List[int]
    """
    sccs = graph.get_sccs()

    # Create a mapping from node to its SCC index
    scc_index = {}
    for idx, scc in enumerate(sccs):
        for node in scc:
            scc_index[node] = idx

    # Build SCC DAG
    scc_graph = defaultdict(set)
    for v in range(graph.n):
        for w in graph.graph[v]:
            if scc_index[v] != scc_index[w]:
                scc_graph[scc_index[v]].add(scc_index[w])

    # Perform topological sort on the SCC DAG
    def topological_sort(scc_graph):
        """
        Performs a topological sort on the strongly connected component (SCC) directed acyclic graph (DAG).

        :param scc_graph: A dictionary representing the SCC DAG. The keys are SCC indices and the values are sets of SCC indices representing the SCCs that are reachable from the key SCC.
        :type scc_graph: Dict[int, Set[int]]
        :return: A list of integers representing the SCC indices in topological order.
        :rtype: List[int]
        """
        in_degree = defaultdict(int)
        for u in scc_graph:
            for v in scc_graph[u]:
                in_degree[v] += 1

        queue = deque(u for u in scc_graph if in_degree[u] == 0)
        sorted_scc = []

        while queue:
            u = queue.popleft()
            sorted_scc.append(u)
            for v in scc_graph[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)

        return sorted_scc

    sorted_scc_indices = topological_sort(scc_graph)

    # Within each SCC, sort nodes by weight
    sorted_nodes = []
    for scc_index in sorted_scc_indices:
        scc = sccs[scc_index]
        scc_sorted = sorted(scc, key=lambda x: weights[x], reverse=True)
        sorted_nodes.extend(scc_sorted)

    return sorted_nodes

# Example usage
n = 5
edges = [(0,2), (1,3), (2, 4), (3,2), (4,0),]
weights = [5,6,7,8,9]

graph = Graph(n)
for u, v in edges:
    graph.add_edge(u, v)

sorted_nodes = topologically_sorted_sccs(graph, weights)
print("Sorted nodes by weights within their SCCs:", sorted_nodes)



# Example usage
n = 6
edges = [(0,5), (1,2), (2, 3), (3,1), (4,2),(5,1)]
weights = [18,8,6,27,25,7]

graph = Graph(n)
for u, v in edges:
    graph.add_edge(u, v)

sorted_nodes = topologically_sorted_sccs(graph, weights)
print("Sorted nodes by weights within their SCCs:", sorted_nodes)
