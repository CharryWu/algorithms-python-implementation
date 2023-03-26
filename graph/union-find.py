class UnionFind:
    def __init__(self, n):
        self.u = [i for i in range(n)]

    def find(self, v):
        while self.u[v] != v:
            v = self.u[v]
        return v

    def union(self, u, v):
        if self.u[u] != self.u[v]:
            self.u[u] = self.u[v]
