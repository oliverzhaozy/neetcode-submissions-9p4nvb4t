class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n != len(edges) + 1:
            return False
        
        visited = set()
        adj = defaultdict(list)
        for par, child in edges:
            adj[par].append(child)
            adj[child].append(par)
        
        def dfs(node):
            # Base case
            if node in visited:
                return

            visited.add(node)
            for neighbour in adj[node]:
                if neighbour not in visited:
                    dfs(neighbour)

        dfs(0)
        return True if len(visited) == n else False
        