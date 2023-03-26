# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        G = {i: set() for i in range(n)}
        for u, v in edges:
            G[u].add(v)
            G[v].add(u)
        
        visited = [False] * n
        def dfs(node):
            visited[node] = True
            for v in G[node]:
                if not visited[v]:
                    dfs(v)
        
        count = 0
        for i in range(n):
            if not visited[i]:
                count +=1
                dfs(i)
        return count

edges = [[0,1],[0,2],[2,3],[2,4]]
# graph = {
#     0: set([1,2]),
#     1: set([0]),
#     2: set([0,3,4]),
#     3: set([2]),
#     4: set([2])
# }
print(Solution().countComponents(5, edges)) # Output 1