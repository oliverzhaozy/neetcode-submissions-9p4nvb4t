class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        par = {}
        rank = {}

        for i in range(1, n + 1):
            par[i] = i
            rank[i] = 0
        
        def find(node):
            if node != par[node]:
                par[node] = find(par[node])
            return par[node]
        
        def union(node1, node2):
            p1, p2 = find(node1), find(node2)
            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True

        for node1, node2 in edges:
            if not union(node1, node2):
                return [node1, node2]